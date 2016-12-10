# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters: filters ={}
	columns = ["Date and Time:Datetime:150","Purpose:Link/Purpose:100","Description:Text:200","Start Odometer Reading:Float:100","Destination::200","End Odometer Reading:Float:100","Mileage (End - Start)"]
	conditions = ""
	if filters.get("from_date"):
		conditions += " AND dvmld.date_and_time >= %(from_date)s"
	if filters.get("to_date"):
		conditions += " AND dvmld.date_and_time <= %(to_date)s"
	if filters.get("vehicle"):
		conditions += " AND dvml.vehicle = %(vehicle)s"
	if filters.get("driver"):
		conditions += " AND dvml.driver = %(driver)s"
	if filters.get("purpose"):
		conditions += " AND dvmld.purpose = %(purpose)s"
	data = frappe.db.sql("SELECT dvmld.date_and_time,dvmld.purpose,dvmld.description,dvmld.start_odometer_reading,dvmld.destination,dvmld.end_odometer_reading,(dvmld.end_odometer_reading-dvmld.start_odometer_reading) FROM `tabDaily Vehicle Mileage Log` dvml LEFT JOIN `tabDaily Vehicle Mileage Log Detail` dvmld ON (dvml.name = dvmld.parent) WHERE dvml.docstatus=1 {0}".format(conditions),filters)
	return columns, data

