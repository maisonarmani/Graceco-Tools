# -*- coding: utf-8 -*-
# Copyright (c) 2015, masonarmani38@gmail.com and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

# test_records = frappe.get_test_records('Accident Report Form')

class TestAccidentReportForm(unittest.TestCase):
	def test_get_employee_experience(self):
		employee_id = "GCL-EMP/0089"
		employee, experience = [], []
		if employee_id:
			employee = frappe.get_doc('Employee', employee_id)
			if employee:
				experience = {
					'internal': employee.internal_work_history,
					'external': employee.external_work_history
				}

	def test_get_employee_experience(self):
		print(frappe.get_user().name)
