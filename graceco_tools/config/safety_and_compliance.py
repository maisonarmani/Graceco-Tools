from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Forms"),
			"items": [
				{
					"type": "doctype",
					"name": "Accident",
					"description": _("Accident")
				},	
				{
					"type": "doctype",
					"name": "Fire Extinguisher",
					"description": _("Fire Extinguisher")
				},
				{
					"type": "doctype",
					"name": "Health Survey",
					"description": _("Health Survey")
				},
				{
					"type": "doctype",
					"name": "Head Count",
					"description": _("Head Count")
				},
				{
					"type": "doctype",
					"name": "Safety Loan",
					"description": _("Safety Loan")
				},
			]
		},
		{
			"label": _("Inspections"),
			"items": [
				{
					"type": "doctype",
					"name": "Fire Extinguisher Inspection",
					"description": _("Fire Extinguisher Inspection")
				},
				{
					"type": "doctype",
					"name": "Fire Extinguisher Inspection Car",
					"description": _("Fire Extinguisher Inspection Car")
				},
				{
					"type": "doctype",
					"name": "Vehicle Inspection Checklist",
					"description": _("Vehicle Inspection Checklist")
				},
				{
					"type": "doctype",
					"name": "Safety Inspection Checklist",
					"description": _("Safety Inspection Checklist")
				},
				{
					"type": "doctype",
					"name": "Safety Checklist",
					"description": _("Safety Checklist")
				},
			]
		},
		{
			"label": _("Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Fire Accident Report",
					"doctype":'Accident',
					"description": _("Fire Accident Report")
				},
			]
		},
		{
			"label": _("Other Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": False,
					"name": "Accident Report",
					"doctype":'Accident',
					"description": _("Accident Report")
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Head Count Report",
					"doctype":'Head Count',
					"description": _("Head Count Report")
				},
			]
		}
	]









				 



