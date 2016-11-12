# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	#Date	Generator Name	Start time	Stop time	Running time
	columns, data = ["Date:Date:150","Generator Name::200","Start Time:Datetime:200","Stop Time:Datetime:200","Total Time:Float:200"], []
	asset=""
	if filters.get("asset"):
		asset=""" and generator = "{}" """.format(filters.get("asset"))
	data = frappe.db.sql("""select date,generator,start,stop,total_time
	from `tabDaily Generator Activity Log` where docstatus=1 and (date between "{}" and "{}") {} """.format(filters.get("from"),filters.get("to"),asset),as_list=1)
	return columns, data
