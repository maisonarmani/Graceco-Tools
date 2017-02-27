# -*- coding: utf-8 -*-
# Copyright (c) 2015, masonarmani38@gmail.com and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

# test_records = frappe.get_test_records('Accident Report Form')

class TestAccidentReportForm(unittest.TestCase):
	def tt_get_employee_experience(self):
		employee_id = "GCL-EMP/0089"
		employee, experience = [], []
		if employee_id:
			employee = frappe.get_doc('Employee', employee_id)
			if employee:
				experience = {
					'internal': employee.internal_work_history,
					'external': employee.external_work_history
				}

	def test_standard(self):

		'''frappe.sendmail(
			recipients= ['masonarmani38@gmail.com','masonarmani38@outlook.com'],
			as_markdown=False,
			content="Hello People",
			message="Maison Armani is testing this guy but what can i say",
			subject="Maison Armani"
		)
		frappe.get_list("Employee")
		'''
		printed = ""
		frappe.set_user("ese.egbevwie@graceco.com.ng") #Simulate login user
		printed = frappe.as_json(
			frappe.get_all("Employee", fields="*", filters=[["modified_by", "=", "Administrator"]], limit_page_length=1,order_by='modified asc'),)
		frappe.has_permission(doctype="Employee", ptype=('cancel'), throw=False)

		print(printed)