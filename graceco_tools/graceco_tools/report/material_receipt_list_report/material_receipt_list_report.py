# Copyright (c) 2013, bobzz.zone@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = ["Date:Date:200","Purchase Order:Link/Purchase Order:200","Supplier:Link/Supplier:200",
	"Item:Link/Item:200","Item Name:Data:200","Description:Data:200",
	"Qty Received:Float:200","Qty Accepted:Float:200","Qty Rejected:Float:200","Amount:Currency:200"], []
	item=""
	supplier=""
	if filters.get("item"):
		item = """ and poi.item_code = '{}' """.format(filters.get("item"))
	if filters.get("supplier"):
		supplier = """ and po.supplier = '{}' """.format(filters.get("supplier"))
	return columns, data
