# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters: filters ={}
	columns = ["Date:Date:100","VFC Doc ID:Link/Vehicle Fuel Consumption log:130","Vehicle:Link/Vehicle:100","Driver:Link/Driver:100","Fuel Type::100","Liters:Float:100","Amount:Currency:100"]
	conditions = ""
	if filters.get("from_date"):
		conditions += " AND date >= %(from_date)s"
	if filters.get("to_date"):
		conditions += " AND date <= %(to_date)s"
	if filters.get("vehicle"):
		conditions += " AND vehicle = %(vehicle)s"
	if filters.get("driver"):
		conditions += " AND driver = %(driver)s"
	if filters.get("fuel_type"):
		conditions += " AND fuel_type = %(fuel_type)s"
	data = frappe.db.sql("SELECT date,name,vehicle,driver,fuel_type,liters,amount FROM `tabVehicle Fuel Consumption log` WHERE docstatus=1 {0}".format(conditions),filters)
	return columns, data
