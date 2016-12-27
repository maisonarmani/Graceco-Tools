// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Loan Application Form', {
	refresh: function(frm) {
		frm.add_fetch("employee","employee_name","employee_name");
		frm.add_fetch("employee","designation","designation");
	}
});
