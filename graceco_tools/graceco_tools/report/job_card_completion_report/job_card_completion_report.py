# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Date:Date:200","Doc id:Link/Job Card:200","Vendor:Link/Supplier:200","Completion Date:Date:200","Verified By:Link/Employee:200"], []
	#Date	doc id	Vendor	Completion date	Job verified by
	vendor=""
	if filters.get("vendor"):
		status = """ and vendor = "{}" """.format(filters.get("vendor"))
	data = frappe.db.sql("""select job_card_date,name,vendor,job_completion_date,job_completion_verified_by
		from `tabJob Card` where (posting_date between "{}" and "{}") {}
	 """.format(filters.get("from"),filters.get("to"),vendor),as_list=1)

	return columns, data
