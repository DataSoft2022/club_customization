// Copyright (c) 2023, Ahmed and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["حافظة يومية 3"] = {
  filters: [
    {
      fieldname: "name",
      label: __("Name"),
      fieldtype: "Link",
      options: "Payment Entry",
    },
    {
      fieldname: "party_name",
      label: __("Party Name"),
      fieldtype: "Data",
    },
    {
      fieldname: "party",
      label: __("Party"),
      fieldtype: "Data",
    },
  ],
};
