// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Vehicle Mileage Report"] = {
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
                        fieldname: "vehicle",
                        label: __("Vehicle"),
                        fieldtype: "Link",
                        options: "Vehicle",
                },
        {
                        fieldname: "driver",
                        label: __("Driver"),
                        fieldtype: "Link",
                        options: "Driver",
                },
        {
                        fieldname: "purpose",
                        label: __("Purpose"),
                        fieldtype: "Link",
                        options: "Purpose",
                },

	]
}
