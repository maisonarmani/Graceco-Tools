# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Item:Link/Item:200","Item Name:Data:200","Total Ordered:Currency:200","Total Delivered:Currency:200","Variance:Currency:200"], []
	item=""
	item_group=""
	if filters.get("item"):
		item = """ and soi.item_code = '{}' """.format(filters.get("item")
	if filters.get("item_group"):
		item_group = """ and soi.item_group = '{}' """.format(filters.get("item_group"))
	data=frappe.db.sql("""select soi.item_code, soi.item_name, sum(soi.amount) 
		from `tabSales Order Item` soi join `tabSales Order` so on soi.parent=so.name 
		where so.docstatus=1 and (so.posting_date between '{}' and '{}') {} {} group by item_code"""
		.format(filters.get("from"),filters.get("to"),item,item_group),as_list=1)
	return columns, data
