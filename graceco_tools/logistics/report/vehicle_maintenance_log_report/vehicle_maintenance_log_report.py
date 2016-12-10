# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters: filters ={}
	columns = ["Date:Date:100","VM Doc ID:Link/Vehicle Maintenance Log:200","Vehicle:Link/Vehicle:100","Work Performed:Text:200","Cost (Parts and Labour):Currency:100","Notes:Text:200"]
	conditions = ""
	if filters.get("from_date"):
		conditions = """ AND p.date >= "{}" """.format(filters.get("from_date"))
	if filters.get("to_date"):
		conditions = """ {} AND p.date <= "{}" """.format(conditions,filters.get("to_date"))
	if filters.get("vehicle"):
		conditions += """ {} AND p.vehicle = "{}" """.format(conditions,filters.get("vehicle"))
	#data = frappe.db.sql("SELECT date,name,vehicle,mileage,work_performed,cost,notes FROM `tabVehicle Maintenance Log` WHERE docstatus=1 {0}".format(conditions),filters)
	data = frappe.db.sql("""select p.date,p.name,p.vehicle,d.description,d.cost,p.notes 
from `tabVehicle Maintenance Log Items` d 
join `tabVehicle Maintenance Log` p on p.name = d.parent WHERE p.docstatus=1 {} """.format(conditions),as_list=1)
	return columns, data

