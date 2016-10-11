# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Date:Date:200","Item:Link/Item:200","Item Name:Data:200","Receipt Ref No:Data:200","Receipt Qty:Float:100","Issues Ref No:Data:200","Issues Qty:Float:100","Balance Qty:Float:200"], []
	item=""
	ref_no=""
	item2=""
	ref_no2=""
	if filters.get("item"):
		item = """ and ii.item_code = '{}' """.format(filters.get("item"))
		item2 = """ and i.item_code = '{}' """.format(filters.get("item"))
	if filters.get("ref_no"):
		ref_no = """ and ii.ref_no = '{}' """.format(filters.get("ref_no"))
		ref_no2 = """ and i.ref_no = '{}' """.format(filters.get("ref_no"))
	frappe.throw("""select pp.name , pp.date as "date" , ii.item_code,ii.item_name,ii.ref_no,ii.qty,"","",ii.balance_qty
		from `tabStore Bin Card Item` ii 
		join `tabStore Bin Card` pp on ii.parent=pp.name 
		where pp.docstatus=1 and (pp.date between "{0}" and  "{1}") {2} {3}
		UNION
		select p.name , p.date as "date" , i.item_code,i.item_name,"","",i.ref_no,i.qty,i.balance_qty
		from `tabStore Bin Card Issue Item` i 
		join `tabStore Bin Card` p on i.parent=p.name 
		where p.docstatus=1 and (p.date between "{0}" and  "{1}") {4} {5} 
		order by date""".format(filters.get("from"),filters.get("to"),item,ref_no,item2,ref_no2))
	data = frappe.db.sql("""select pp.name , pp.date as "date" , ii.item_code,ii.item_name,ii.ref_no,ii.qty,"","",ii.balance_qty
		from `tabStore Bin Card Item` ii 
		join `tabStore Bin Card` pp on ii.parent=pp.name 
		where pp.docstatus=1 and (pp.date between "{0}" and  "{1}") {2} {3}
		UNION
		select p.name , p.date as "date" , i.item_code,i.item_name,"","",i.ref_no,i.qty,i.balance_qty
		from `tabStore Bin Card Issue Item` i 
		join `tabStore Bin Card` p on i.parent=p.name 
		where p.docstatus=1 and (p.date between "{0}" and  "{1}") {4} {5} 
		order by date""".format(filters.get("from"),filters.get("to"),item,ref_no,item2,ref_no2),as_list=1)
	return columns, data
