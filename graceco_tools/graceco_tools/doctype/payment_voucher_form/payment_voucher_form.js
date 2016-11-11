// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Payment Voucher Form', {
	refresh: function(frm) {

	},
	setup:function(frm) {
		cur_frm.set_query("bank_account", function() {
			return {
				"filters": [{
					["Account","account_type","in","Bank,Cash"],
					["Account", "is_group","in","0"]
				}]
			};
		});
		cur_frm.set_query("expense_account", function() {
			return {
				"filters": [{
					["Account","lft",">=","362"],
					//["Account","rgt","<=","561"],
					["Account", "is_group","in","0"]
				}]
			};
		});

	}
});
