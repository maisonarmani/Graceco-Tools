# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Item Code:Link/Item:200","Item Name::200","Current Level:Float:100","Re-order Level:Float:100","Re-order Qty:Float:100","Lead Time:Int:100"], []
	#Item code	Item Name	Current Level	Re-order level	Re-order Qty	Lead time
	#					<from stock ledger>	<from item>		<from item>	<from item>
	data = frappe.db.sql("""select s.item_code,it.item_name, s.qty_after_transaction,i.warehouse_reorder_level,i.warehouse_reorder_qty,it.lead_time_days
		from `tabStock Ledger Entry` s 
		join (
			select ss.item_code,max(addtime(ss.posting_date,ss.posting_time)) as "latest"
			from `tabStock Ledger Entry` ss where ss.warehouse="{0}" group by ss.item_code  
			) sd on s.item_code=sd.item_code and addtime(s.posting_date,s.posting_time)=sd.latest
		join `tabItem Reorder` i on i.parent=s.item_code and i.warehouse = "{0}"
		join `tabItem` it on it.item_code=s.item_code
		""".format(filters.get("warehouse")), as_list=1)
	return columns, data

