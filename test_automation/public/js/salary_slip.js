frappe.ui.form.on('Salary Slip', {
    refresh: function(frm) {
		if (frm.doc.docstatus == 1) {
				frm.add_custom_button(__("Make Payment"),
						frm.events.make_journal(frm)
				);
        }
	},
	
    make_journal: function (frm) {
		return frappe.call({
			doc: frm.doc,
			method: 'make_journal_entry',
			callback: function(r) {
				alert('success');
			}
		})
	}
});