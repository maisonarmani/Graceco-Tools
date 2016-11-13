// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Fixed Asset Inspection Checklist', {
	refresh: function(frm) {

	},
	setup: function(frm) {
		cur_frm.set_query("fixed_asset", function() {
			return {
				"filters": {
					"docstatus":1
				}
			};
		});
		
	},
});
