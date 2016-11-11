# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
#Date 	Doc-id	Supplier Name	Ref doc	Amount	Mode of Payment	Bank Name	Ref No
def execute(filters=None):
	columns, data = ["Date:Date:200","Payment Voucher Form:Link/Payment Voucher Form:200",
	"Supplier:Link/Supplier:200","Ref doc::200","Amount:Currency:200","Mode of Payment:Link/Mode Of Payment:200","Bank Name::200","Ref No::200"], []
	supplier,mop,bank="","",""
	if filters.get("supplier"):
		supplier=""" """
	if filters.get("mop"):
		mop=""" """
	if filters.get("bank"):
		bank=""" """
	
	data=frappe.db.sql(""" """,as_list=1)
	return columns, data
