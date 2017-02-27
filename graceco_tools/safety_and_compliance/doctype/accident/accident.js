// Copyright (c) 2016, masonarmani38@gmail.com and contributors
// For license information, please see license.txt
var take = function(obj,param){
	var __self__ = this;
	if(typeof param !== 'string'){
		param.forEach(function(val){
			__self__[val] = obj[val] || "";
		});
	}else{
		__self__[param] = obj[param] || "";
	}
};

frappe.ui.form.on("Accident",{
	employee:function(frm,cdt,cdn){
		frappe.call({
			method:'graceco_tools.safety_and_compliance.api.get_employee_experience',
			args:{
				employee_id:frm.doc.employee
			},
			callback:function(ret){
				var message = ret.message || {};
				if(message.external /**&& !frm.doc.external_work_experience.length**/){
					// for external
					frm.doc.external_work_experience = [];
					message.external.forEach(function(val){
						var d = frappe.model.add_child(cur_frm.doc, "Victim External Work History", "external_work_experience");
						take.apply(d,[val,[
							'company_name','designation','salary','address','contact','total_experience'
						]]);
					});
				}
				if(message.internal /** && !frm.doc.internal_work_experience.length**/){
					// for internal
					frm.doc.internal_work_experience = []
					message.internal.forEach(function(val){
						var d = frappe.model.add_child(cur_frm.doc, "Victim Internal Work History", "internal_work_experience");
						take.apply(d,[val,[
							'branch','department','designation','from_date','to_date'
						]]);
					});

				}

				refresh_field('internal_work_experience');
				refresh_field('external_work_experience');
			}
		})
	},
	refresh: function(frm) {},
	onload:function(frm,cdt,cdn){
		// set prepared by and prepared date
		if(frm.doc.prepared_by == "" || frm.doc.prepared_by == undefined){
			frappe.model.set_value(cdt,cdn,'prepared_by',user_fullname);
		}
		if(frm.doc.prepared_date == "" || frm.doc.prepared_date == undefined){
			frappe.model.set_value(cdt,cdn,'prepared_date',frappe.datetime.now_datetime());
		}
	}

});


frappe.ui.form.on("Employee External Work History",{
    company_name: function (frm, cdt, cdn) {
		console.log(arguments);
    }
});
