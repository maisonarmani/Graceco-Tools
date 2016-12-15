// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
cur_frm.add_fetch("assigned_to","employee_name","assigned_to_name");//,"employee_name")
frappe.ui.form.on("Helpdesk Ticket", "onload", function(frm) {
    cur_frm.set_query("equipment", function() {
        return {
            "filters": {
                "is_fixed_asset": "1"
            }
        };
    });
});
frappe.ui.form.on('Helpdesk Ticket', {
	refresh: function(frm) {
		cur_frm.add_custom_button('Make Job Card', function () {
			var jc = frappe.model.make_new_doc_and_get_name('Job Card');
			jc = locals['Job Card'][jc];
			jc.ticket_number = cur_frm.doc.name;
			//loaddoc('Job Card', jc.name);
			//frappe.route_options = { "customer": frm.doc.customer ... };
			frappe.set_route("Form", "Job Card", jc.name);
		});
//		cur_frm.fields_dict['equipment'].get_query = function(doc) {
//			return {
//				filters: {
//				"is_asset_item": true
//				}
//			}
//		};

                cur_frm.set_df_property("priority", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                cur_frm.set_df_property("request_type", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                cur_frm.set_df_property("equipment", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                cur_frm.set_df_property("subject", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                cur_frm.set_df_property("raised_by", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                cur_frm.set_df_property("description", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));

		if (!frappe.user.has_role(['Helpdesk Admin']))
		{
	                cur_frm.set_df_property("status", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
			cur_frm.set_df_property("first_responded_on", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                        cur_frm.set_df_property("assigned_to", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                        cur_frm.set_df_property("tech_administrator", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                        cur_frm.set_df_property("contact", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                        cur_frm.set_df_property("resolution", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
                        cur_frm.set_df_property("resolution_details", "read_only", (cur_frm.doc.status == "Assigned" || cur_frm.doc.status == "On-Hold" || cur_frm.doc.status == "Close"));
		}
	},
	
	raised_by: function(frm, cdt, cdn) {
		var ticket = frappe.model.get_doc(cdt, cdn);
		if (ticket.raised_by) {
			frappe.call({
				method: "graceco_tools.graceco_tools.doctype.helpdesk_ticket.helpdesk_ticket.get_full_name",
				args: {
					raised_by: ticket.raised_by
					},
				callback: function(r) {

				frappe.model.set_value(cdt, cdn, "raised_by_name", r.message);}
			});
		}
	},

});
