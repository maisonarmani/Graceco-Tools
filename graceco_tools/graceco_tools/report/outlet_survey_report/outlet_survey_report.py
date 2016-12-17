# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	if not filters: filters ={}
	columns = ["Date:Datetime:110","Survey ID::100","Outlet Name:Data:200","Outlet Location:Data:200","Sales Rep:Link/Sales Person:200","Route:Link/Territory:200"]
        conditions = ""
        if filters.get("from_date"):
                conditions += " AND os.date >= %(from_date)s"
        if filters.get("to_date"):
                conditions += " AND os.date <= %(to_date)s"
        if filters.get("sales_rep"):
                conditions += " AND os.sales_rep = %(sales_rep)s"
        if filters.get("route"):
                conditions += " AND os.route = %(route)s"
        data = frappe.db.sql("""SELECT os.date,os.name,od.outlet_name,od.address,os.sales_rep,os.route FROM `tabOutlet Survey` os, `tabOutlet Details` od WHERE os.name = od.parent %s""" % conditions,filters)
        return columns, data
