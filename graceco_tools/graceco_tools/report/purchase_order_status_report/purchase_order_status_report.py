# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	#Date | Supplier | Item Description | Status Report | Updated By
	columns, data = ["Date:Date:100","Purchase Order:Link/Purchase Order:125","Supplier:Link/Supplier:150","Item Name:Data:400","Status:Data:200","Updated By:Data:200"], []
	supplier=""
	if filters.get("supplier"):
		supplier=""" and p.supplier = "{}" """.format(filters.get("supplier"))
	data = frappe.db.sql("""select s.modified,s.purchase_order,p.supplier,s.status,s.modified_by
	from `tabPurchase Order Status` s 
	join `tabPurchase Order` p on p.name = s.purchase_order
	where s.docstatus=1 and p.docstatus=1 and (s.modified between "{}" and "{}") {} """.format(filters.get("from"),filters.get("to"),supplier),as_list=1)
	return columns, data
