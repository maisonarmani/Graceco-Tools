# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Graceco Tools",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Production")
		},
		{
			"module_name": "Reports",
			"color": "#bdc3c7",
			"icon": "octicon octicon-checklist",
			"type": "module",
			"label": _("Reports")
		},
		{
			"module_name": "Logistics",
			"color": "#FF0084",
			"icon": "icon-checklist",
			"icon": "octicon octicon-checklist",
			"type": "module"
		},
		{
			"module_name": "Safety and Compliance",
			"color": "#FF0089",
			"icon": "icon-checklist",
			"icon": "octicon octicon-checklist",
			"type": "module"
		},
	]
