# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Store Bin Card No:Link/Store Bin Card:200","Date:Date:200","Item:Link/Item:200","Item Name:Data:200","Receipt Ref No:Data:200","Receipt Qty:Float:100","Issues Ref No:Data:200","Issues Qty:Float:100","Balance Qty:Float:200"], []
	rqty=0
	iqty=0
	receipt_qty = frappe.db.sql("""select sum(ii.qty)
		from `tabStore Bin Card Item` ii 
		join `tabStore Bin Card` pp on ii.parent=pp.name 
		where pp.docstatus=1 and pp.date < "{0}" ii.item_code = '{1}' group by ii.item_code """.format(filters.get("from"),filters.get("item")),as_list=1)
	for row in receipt_qty:
		rqty=row[0]
	issued_qty = frappe.db.sql("""select sum(ii.qty)
		from `tabStore Bin Card Issue Item` ii 
		join `tabStore Bin Card` pp on ii.parent=pp.name 
		where pp.docstatus=1 and pp.date < "{0}" ii.item_code = '{1}' group by ii.item_code """.format(filters.get("from"),filters.get("item")),as_list=1)
	for row in issued_qty:
		iqty=row[0]
	all_data = frappe.db.sql("""select pp.name , pp.date as "date" , ii.item_code,ii.item_name,ii.ref_no,ii.qty,"",""
		from `tabStore Bin Card Item` ii 
		join `tabStore Bin Card` pp on ii.parent=pp.name 
		where pp.docstatus=1 and (pp.date between "{0}" and  "{1}")  and ii.item_code = '{2}' 
		UNION
		select p.name , p.date as "date" , i.item_code,i.item_name,"","",ii.ref_no,i.qty
		from `tabStore Bin Card Issue Item` i 
		join `tabStore Bin Card` p on i.parent=p.name 
		where p.docstatus=1 and (p.date between "{0}" and  "{1}")  and i.item_code = '{2}' 
		order by date""".format(filters.get("from"),filters.get("to"),filters.get("item")),as_list=1)
	balance = rqty-iqty
	for row in all_data:
		data.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],balance+row[5]-row[7]])
	return columns, data