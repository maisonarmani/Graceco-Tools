# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	#Date	Doc-id	Generator Name	Fuel Qty	Amount
	columns, data = ["Date:Date:150","Generator Fuel Log:Link/Generator Fuel Consumption Log:150","Generator Name::200","Fuel Qty:Float:100","Amount:Currency:200"], []
	asset=""
	if filters.get("asset"):
		asset=""" and generator = "{}" """.format(filters.get("asset"))
	data = frappe.db.sql("""select date,name,generator,fuel_qty,total
	from `tabGenerator Fuel Consumption Log` where docstatus=1 and (date between "{}" and "{}") {} """.format(filters.get("from"),filters.get("to"),asset),as_list=1)
	return columns, data
