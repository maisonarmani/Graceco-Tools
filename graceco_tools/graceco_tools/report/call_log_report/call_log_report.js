// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.query_reports["Call Log Report"] = {
	"filters": [
		{
			"fieldname":"customer",
			"label": __("Customer"),
			"fieldtype": "Link",
			"options": "Customer",
			"reqd":1
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
