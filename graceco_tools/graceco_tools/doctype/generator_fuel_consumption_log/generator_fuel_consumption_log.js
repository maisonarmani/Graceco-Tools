// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Generator Fuel Consumption Log', {
	refresh: function(frm) {

	},
	setup: function(frm) {
		cur_frm.set_query("generator", function() {
			return {
				"filters": {
					"asset_category":"Plant and Machinery"
				}
			};
		});
		
	}
});
