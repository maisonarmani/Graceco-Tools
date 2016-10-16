from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"items": [
				{
					"type": "doctype",
					"name": "Raw Materials Return Form",
					"description": _("Raw Materials Return Form")
				},
				{
					"type": "doctype",
					"name": "Quality Control Material Acceptance Form",
					"description": _("Quality Control Material Acceptance Form")
				},
				{
					"type": "doctype",
					"name": "Production Yield Control Form",
					"description": _("Production Yield Control Form")
				},
				{
					"type": "doctype",
					"name": "Finished Goods Transfer Form",
					"description": _("Finished Goods Transfer Form")
				},
				{
					"type": "doctype",
					"name": "Weekly Production Order Form",
					"description": _("Weekly Production Order Form")
				},
				{
					"type": "doctype",
					"name": "Store Bin Card",
					"description": _("Store Bin Card")
				},
			]
		},
		{
			"label":_("Master"),
			"items": [
				{
					"type": "doctype",
					"name": "Production Unit",
					"description": _("Production Unit")
				}
			]
		},
		{
			"label": _("Report"),
			"items": [
				{
					"type": "report",
					"name": "Finished Goods Transfer Report",
					"doctype": "Finished Goods Transfer Form",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Production Order Report",
					"doctype": "Weekly Production Order Form",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Production Yield Variance Report",
					"doctype": "Production Yield Control Form",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Raw Materials Return Report",
					"doctype": "Raw Materials Return Form",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Sales Person-wise Transaction Summary",
					"doctype": "Sales Order",
					"is_query_report": True,
				}
			]
		}
	]









				 



