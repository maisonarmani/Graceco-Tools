# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	#Date | Supplier | Item Description | Status Report | Updated By
	columns, data = ["Date:Date:200","Purchase Order:Link/Purchase Order:200","Supplier:Link/Supplier:200","Item Name:Data:200","Status:Data:200","Updated By:Data:200"], []
	supplier=""
	if filters.get("supplier"):
		supplier=""" and p.supplier = "{}" """.format(filters.get("supplier"))
	data = frappe.db.sql("""select s.date,s.purchase_order,p.supplier,CONCAT("(", i.item_code,")","-",i.item_name),s.status,s.updated_by
	from `tabPurchase Order Item` i 
	join `tabPurchase Order` p on i.parent = p.name
	join `tabPurchase Order Status` s on i.parent = s.purchase_order
	where s.docstatus=1 and p.docstatus=1 and (s.date between "{}" and "{}") {} """.format(filters.get("from"),filters.get("to"),supplier),as_list=1)
	return columns, data
