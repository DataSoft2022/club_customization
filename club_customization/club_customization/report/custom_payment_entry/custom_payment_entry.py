# Copyright (c) 2023, Ahmed and contributors
# For license information, please see license.txt

import frappe

def get_columns():
    columns = [{
        'fieldname': "name",
        'label': 'Payment Entry',
        'fieldtype': 'Link',
        'options': 'Payment Entry',
    }, {
        'fieldname': 'reference_doctype',
        'label': 'Referece Type',
        'fieldtype': 'Data',
    }, {
        'fieldname': 'sales_name',
        'label': 'Sales Name',
        'fieldtype': 'Link',
        'options': 'Sales Invoice',
    }, {
        'fieldname': 'fee_name',
        'label': 'Fees Name',
        'fieldtype': 'Link',
        'options': 'Fees',
    }, {
        'fieldname': 'party',
        'label': 'Party',
        'fieldType': 'Data',
    }, {
        'fieldname': 'party_name',
        'label': 'Party Name',
        'fieldType': 'Data',
    }, {
        'fieldname': 'program',
        'label': 'Program',
        'fieldType': 'Data',
    },{
        'fieldname': 'paid_amount',
        'label': 'Paid Amount',
        'fieldType': 'Data',
    },{
        'fieldname': 'posting_date',
        'label': 'Posting Date',
        'fieldType': 'Date',
    },{
        'fieldname': 'mode_of_payment',
        'label': 'Mode of Payment',
        'fieldType': 'Data',
    }]
    return columns

def get_data(filters):
    query = f"""
    select pe_j_rf.name, pe_j_rf.reference_doctype, pe_j_rf.sales_name, pe_j_rf.fee_name,
    pe_j_rf.party, pe_j_rf.party_name, pe_j_rf.paid_amount, pe_j_rf.posting_date, pe_j_rf.mode_of_payment,  fee.program
    from
     (select pe.name, rf.reference_doctype,if(rf.reference_doctype='Sales Invoice',rf.reference_name, null) as sales_name, if(rf.reference_doctype='Fees', rf.reference_name, null) as fee_name, pe.party, pe.party_name, pe.paid_amount, pe.posting_date, pe.mode_of_payment
     from
     `tabPayment Entry` as pe join `tabPayment Entry Reference` as rf
     on
     pe.name=rf.parent)
    as pe_j_rf left
    join
    `tabFees` as fee
    on
    fee.name=pe_j_rf.fee_name
    where
    pe_j_rf.party_name like '%{filters.get("party_name", "")}%'
    and
    pe_j_rf.party like '%{filters.get("party", "")}%'
    and
    pe_j_rf.name like '%{filters.get("name", "")}%'
    """
    
    data = frappe.db.sql(query, as_dict=1)

    return data

def execute(filters=None):
    return get_columns(), get_data(filters)


