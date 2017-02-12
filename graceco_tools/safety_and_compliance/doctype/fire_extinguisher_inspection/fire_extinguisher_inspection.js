// Copyright (c) 2016, masonarmani38@gmail.com and contributors
// For license in*..formation, please see license.tx

frappe.ui.form.on("Fire Extinguisher Inspection",{
    refresh: function (frm) {
        cur_frm.add_custom_button("Request Refill", function () {
            //cur_frm.cscript.test_mapping();
            frappe.set_route("Form/Helpdesk Ticket/New Helpdesk Ticket 1", {
               priority: 'High',
               request_type: 'Fire Extinguisher Refill'
            });
        },__("Options"));
        cur_frm.page.set_inner_btn_group_as_primary(__("Options"));
        cur_frm.cscript.inspection_date = function (doc) {
            //console.log(doc,arguments);
            var ins_date = doc.inspection_date;
            if(ins_date < dateutil.get_today()){
                frappe.msgprint(__("Sorry the inspection can not be a day before today"));
                frappe.model.set_value(doc.doctype, doc.name,'inspection_date',dateutil.get_today());
            }
        };
    },
    onload: function (frm, cdt, cdn) {
        // set prepared by and prepared date
        if (frm.doc.safety_inspection_officer == "" || frm.doc.safety_inspection_officer == undefined) frappe.model.set_value(cdt, cdn, 'safety_inspection_officer',
            [frappe.boot.user.first_name, frappe.boot.user.last_name].join(" "));
    },
    inspection_date:function(frm, cdt, cdn){

    }
});

cur_frm.cscript.test_mapping = function() {
	frappe.model.open_mapped_doc({
		method: "graceco_tools.safety_and_compliance.api.map_test",
		frm: cur_frm
	})
};

frappe.ui.form.on("Inspected Fire Extinguisher",{
    onload:function(frm,cdt,cdn){
        console.log(frm)
    }
});

cur_frm.fields_dict.fire_extinguisher.grid.get_field('fire_extinguisher').get_query = function(doc){
    return{
        filter:{}
    }
};
