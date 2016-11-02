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
			"icon": "octicon octicon-file-checklist",
			"type": "module",
			"label": _("Reports")
		}
	]
