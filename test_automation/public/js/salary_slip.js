frappe.ui.form.on('Salary Slip', {
    refresh: function(frm) {
		if (frm.doc.docstatus == 1) {
				frm.add_custom_button(__("Make Payment"),function(){
					frm.events.make_journal(frm);
				});
        }
	},
	
    make_journal: function (frm) {
		return frappe.call({
			method: "test_automation.test_automation.salary_slip.salary_slip.make_journal_entry",
			args: { 
				source_name: frm.doc.name
			},
			callback: function(r) {
				frappe.msgprint({
					title: __('Notification'),
					indicator: 'green',
					message: __('Journal entries created for this salary slip')
				});
			}
		})
	}
});