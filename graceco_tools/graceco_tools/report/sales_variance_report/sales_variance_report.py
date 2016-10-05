# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Item:Link/Item:200","Item Name:Data:200","Total Ordered:Currency:200","Total Delivered:Currency:200","Variance:Currency:200"], []
	so_item=""
	dn_item=""
	so_item_group=""
	dn_item_group=""
	if filters.get("item"):
		dn_item = """ and dni.item_code = '{}' """.format(filters.get("item"))
		so_item = """ and soi.item_code = '{}' """.format(filters.get("item"))
	if filters.get("item_group"):
		so_item_group = """ and soi.item_group = '{}' """.format(filters.get("item_group"))
		dn_item_group = """ and dni.item_group = '{}' """.format(filters.get("item_group"))
	data=frappe.db.sql("""order.item_code, order.item_name,order.amount,delivery.amount,(order.amount-delivery.amount) 
		from (select soi.item_code, soi.item_name, sum(soi.amount) as amount
		from `tabSales Order Item` soi join `tabSales Order` so on soi.parent=so.name 
		where so.docstatus=1 and (so.transaction_date between '{0}' and '{1}') {2} {3} group by item_code) order
		join (select dni.item_code, dni.item_name, sum(dni.amount) as amount
		from `tabDelivery Note Item` dni join `tabDelivery Note` dn on dni.parent=dn.name 
		where dn.docstatus=1 and (dn.posting_date between '{0}' and '{1}') {4} {5} group by item_code) delivery on order.item_code = delivery.item_code
	"""
		.format(filters.get("from"),filters.get("to"),so_item,so_item_group,dn_item,dn_item_group),as_list=1)
	return columns, data
