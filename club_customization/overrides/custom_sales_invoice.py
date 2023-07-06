import frappe
import datetime
from copy import deepcopy

def try_to_print():
    print("\n\n\n\n\n\n\n\n\n hi \n\n\n\n\n\n\n\n")

def renew_members_subscriptions():
    customers = frappe.get_list('Customer', filters={"customer_group": "عضو عامل"})
    for customer in customers:
        new_sales_invoice_with_new_subscribtion(customer['name'])
    frappe.db.commit()
    

def new_sales_invoice_with_new_subscribtion(customer_name):
    invoice = frappe.new_doc("Sales Invoice")
    customer = frappe.get_doc("Customer", customer_name)
    product_bundle = frappe.get_doc("Product Bundle", "تجديد الأشتراك")

    invoice.customer = customer_name
    invoice.product_bundle = product_bundle.name

    invoice.taxes_and_charges = product_bundle.sales_taxes_and_charges_template
    invoice.items = get_product_bundle_items(product_bundle, customer_name)
    invoice.total_amount = sum(item.amount for item in invoice.items)
    invoice.sub_members = get_sub_members_items(customer_name)

    invoice.save()
    return invoice


def get_product_bundle_items(product_bundle, customer_name):
    items = []
    company = frappe.get_doc("Company", "The Club")

    for item in product_bundle.items:
        addresses = get_customer_address(customer_name, item.customer_group)
        quantity = 1
        if item.category == "Customer Group":
            if item.include_main_member == "Yes":
                quantity += len(addresses)

            else:
                quantity = len(addresses)
        elif item.category == 'all':
            quantity += len(get_customer_address(customer_name, None))

        elif item.category == 1:
            quantity = item.qty

        if quantity == 0: continue
        rate = frappe.db.get("Item Price",
                             filters={
                                 "item_code": item.item_code
                             }).price_list_rate
        item_details = frappe.get_doc("Item", item.item_code)
        sales_invoice_item = frappe.new_doc("Sales Invoice Item")
        sales_invoice_item.category = item.category
        sales_invoice_item.customer_group = item.customer_group
        sales_invoice_item.item_code = item_details.item_code
        sales_invoice_item.qty = quantity
        sales_invoice_item.rate = rate
        sales_invoice_item.amount = rate * quantity
        sales_invoice_item.item_name = item_details.item_name
        sales_invoice_item.uom = item_details.stock_uom
        sales_invoice_item.description = item.description
        sales_invoice_item.income_account = item_details.item_defaults[
            0].income_account
        sales_invoice_item.expense_account = company.default_expense_account
        sales_invoice_item.conversion_factor = item_details.uoms[
            0].conversion_factor
        sales_invoice_item.parentfield = "items"
        items.append(sales_invoice_item)
    return items


def get_customer_address(customer_name, customer_group, fields=None):
    filters = {}
    filters['member_no'] = customer_name
    if (customer_group): filters['customer_group'] = customer_group
    return frappe.db.get_list("Address", filters, fields)


def get_sub_members_items(customer_name):
    addresses = get_customer_address(customer_name, None, [
        'full_name', 'personal_identification_number', 'customer_group',
        'address_type'
    ])
    sub_members = []
    for address in addresses:
        sub_member = frappe.new_doc("Sub Member")
        sub_member.member_name = address.full_name
        sub_member.personal_id = address.personal_identification_number
        sub_member.customer_group = address.customer_group
        sub_member.type = address.address_type
        sub_member.parentfield = "sub_members"
        sub_members.append(sub_member)

    return sub_members
