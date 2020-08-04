import frappe

def make_journal_entry(self):
    journal_entry = frappe.new_doc('Journal Entry')
    journal_entry.flags.ignore_permissions  = True
    journal_entry.voucher_type = 'Journal Entry'
    default_payroll_payable_account = self.get_default_payroll_payable_account()

    accounts.append({
        "account": 'Salary - X',
        "debit_in_account_currency": self.net_pay,
        "party_type": '',
    })

    accounts.append({
        "account": default_payroll_payable_account,
        "credit_in_account_currency": self.net_pay,
        "party_type": '',
    })

    journal_entry.user_remark = _('Journal Entry for salaries from {0} to {1}')\
        .format(self.start_date, self.end_date)

    journal_entry.save()
    journal_entry.submit()

    journal_entry_1 = frappe.new_doc('Journal Entry')
    journal_entry_1.flags.ignore_permissions  = True
    journal_entry_1.voucher_type = 'Journal Entry'
    default_payroll_payable_account = self.get_default_payroll_payable_account()

    accounts.append({
        "account": default_payroll_payable_account,
        "debit_in_account_currency": self.net_pay,
        "party_type": '',
    })

    accounts.append({
        "account": 'SBI - X',
        "credit_in_account_currency": self.net_pay,
        "party_type": '',
    })

    journal_entry_1.user_remark = _('payment Entry for salaries from {0} to {1}')\
        .format(self.start_date, self.end_date)

    journal_entry_1.save()
    journal_entry_1.submit()

    frappe.msgprint(msg = 'Journal entries created for this salary slip',
       title = 'Notification',
       indicator = 'green'
    )

    return journal_entry,journal_entry_1

def get_default_payroll_payable_account(self):
	payroll_payable_account = frappe.get_cached_value('Company',
		{"company_name": self.company},  "default_payroll_payable_account")

	if not payroll_payable_account:
		frappe.throw(_("Please set Default Payroll Payable Account in Company {0}")
			.format(self.company))

		return payroll_payable_account
