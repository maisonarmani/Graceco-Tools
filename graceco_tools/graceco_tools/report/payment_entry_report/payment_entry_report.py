# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	#Date	Party (Name)	Payment Type (JV Status)	Amount	Reference	Voucher #
	columns, data = ["Date:Date:200","Party:Data:200","Payment Type:Data:200","Amount:Currency:200","Reference Voucher"], []
	data = frappe.db.sql("""select posting_date,party,payment_type,IF(party_type=="Customer",received_amount,paid_amount),reference_no 
		from `tabPayment Entry` where docstatus=1 and (posting_date between "{}" and "{}") """.format(filters.get("from"),filters.get("to")),as_list=1)
	return columns, data
