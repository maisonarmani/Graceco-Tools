from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Vehicle"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Vehicle Fuel Consumption log",
					"description": _("Vehicle Fuel Consumption log"),
				},
                                {
                                        "type": "doctype",
                                        "name": "Vehicle Schedule",
                                        "description": _("Vehicle Schedule"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Vehicle Maintenance Log",
                                        "description": _("Vehicle Maintenance Log"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Daily Vehicle Mileage Log",
                                        "description": _("Daily Vehicle Mileage Log"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Vehicle Inspection Checklist",
                                        "description": _("Vehicle Inspection Checklist"),
                                },
			]
		},
                {
                        "label": _("Expense"),
                        "icon": "icon-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Logistics Expense",
                                        "description": _("Logistics Expense"),
                                },
                        ]
                },
                {
                        "label": _("Setup"),
                        "icon": "icon-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Vehicle",
                                        "description": _("Vehicle"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Driver",
                                        "description": _("Driver"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Purpose",
                                        "description": _("Purpose"),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Logistics Expense Type",
                                        "description": _("Logistics Expense Type"),
                                },
                        ]
                },

	]
