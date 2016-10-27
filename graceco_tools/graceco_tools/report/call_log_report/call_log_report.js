// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.query_reports["Call Log Report"] = {
	"filters": [
		{
			"fieldname":"from",
			"label": __("From Date"),
			"fieldtype": "Datetime",
			"width": "80",
			"reqd":1
		},
		{
			"fieldname":"to",
			"label": __("To Date"),
			"fieldtype": "Datetime",
			"default": get_today(),
			"reqd":1
		},
		{
			"fieldname":"customer",
			"label": __("Customer"),
			"fieldtype": "Link",
			"options": "Customer",
			"reqd":0
		},
		{
			"fieldname":"call_type",
			"label": __("Call Type"),
			"fieldtype": "Link",
			"options": "Call Type",
			"reqd":0
		},
		{
			"fieldname":"call_purpose",
			"label": __("Call Purpose"),
			"fieldtype": "Link",
			"options": "Call Purpose",
			"reqd":0
		}
	]
}
