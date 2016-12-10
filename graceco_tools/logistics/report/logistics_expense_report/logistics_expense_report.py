# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters: filters ={}
	columns = ["Date:Date:100","Doc ID:Link/Expense Claim:150","Logistic Expense Type:Link/Expense Claim Type:100","Description:Text:200","Amount:Currency:150","Approver:Link/User:200"]
	conditions = ""
	if filters.get("from_date"):
		conditions += " AND led.expense_date >= %(from_date)s"
	if filters.get("to_date"):
		conditions += " AND led.expense_date <= %(to_date)s"
	if filters.get("approver"):
		conditions += " AND le.exp_approver = %(approver)s"
	if filters.get("expense_type"):
		conditions += " AND led.expense_type = %(expense_type)s"
	data = frappe.db.sql("SELECT led.expense_date,le.name,led.expense_type,led.description,led.sanctioned_amount,le.exp_approver FROM `tabLogistics Expense` le LEFT JOIN `tabLogistics Expense Detail` led ON (le.name = led.parent) WHERE le.docstatus=1 {0}".format(conditions),filters)
	return columns, data

