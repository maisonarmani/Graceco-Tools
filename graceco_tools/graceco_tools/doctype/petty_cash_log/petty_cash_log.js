// Copyright (c) 2016, bobzz.zone@gmail.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Petty Cash Log', {
	refresh: function(frm) {

	},
    validate:function(frm) {
        if (frm.doc.transaction_type == "Receipt") {
            frm.doc.buying=[];
            validated = true;
            $.each(frm.doc.sales,function(i,d){
                if (d.ref_doc!="Opening" && (!d.ref_no || d.ref_no=="")) {
                    msgprint("Please enter the Reference No except for the Opening Stock");
                    validated=false;
                };
            });
            
        }else{
            frm.doc.sales=[];
            validated = true;
        }
    }
});
