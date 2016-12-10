// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Maintenance Log', {
	refresh: function(frm) {

	}
});
frappe.ui.form.on("Vehicle Maintenance Log", {
    validate: function(frm) {
        // calculate incentives for each person on the deal
        total = 0;
        $.each(frm.doc.items, function(i, d) {
            total += flt(d.cost);
        });

        frm.doc.cost= total;
    }
});
