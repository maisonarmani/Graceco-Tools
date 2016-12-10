// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Logistics Expense Report"] = {
	"filters": [
        {
                        fieldname: "from_date",
                        label: __("From Date"),
                        fieldtype: "Date",
                },
        {
                        fieldname: "to_date",
                        label: __("To Date"),
                        fieldtype: "Date",
                },
        {
                        fieldname: "approver",
                        label: __("Approver"),
                        fieldtype: "Link",
                        options: "User",
                },
        {
                        fieldname: "expense_type",
                        label: __("Logistics Expense Type"),
                        fieldtype: "Link",
                        options: "Logistics Expense Type",
                },
	]
}
