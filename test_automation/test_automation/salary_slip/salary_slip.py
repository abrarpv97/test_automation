import frappe
from datetime import date 

@frappe.whitelist()
def make_journal_entry(source_name,target=None):
    if source_name:
        doc = frappe.get_doc("Salary Slip", source_name)
        start_date = doc.start_date
        end_date = doc.end_date
    #    default_payroll_payable_account = get_default_payroll_payable_account(doc.company)
        journal_entry = frappe.new_doc('Journal Entry')
        journal_entry.flags.ignore_permissions  = True
        journal_entry.voucher_type = 'Journal Entry'
        journal_entry.posting_date = date.today()

        journal_entry.append('accounts', {
            "account": 'Salary - X',
            "debit_in_account_currency": doc.net_pay,
            "party_type": '',
        })

        journal_entry.append('accounts', {
            "account": 'Payroll Payable - X',
            "credit_in_account_currency": doc.net_pay,
            "party_type": '',
        })

        journal_entry.user_remark = 'Journal Entry for salaries from '+start_date.strftime('%d/%m/%Y')+' to '+end_date.strftime('%d/%m/%Y')

        journal_entry.save()
        journal_entry.submit()

        journal_entry_1 = frappe.new_doc('Journal Entry')
        journal_entry_1.flags.ignore_permissions  = True
        journal_entry_1.voucher_type = 'Journal Entry'
        journal_entry_1.posting_date = date.today()

        journal_entry_1.append('accounts', {
            "account": 'Payroll Payable - X',
            "debit_in_account_currency": doc.net_pay,
            "party_type": '',
        })

        journal_entry_1.append('accounts', {
            "account": 'SBI - X',
            "credit_in_account_currency": doc.net_pay,
            "party_type": '',
        })

        journal_entry_1.user_remark = 'payment Entry for salaries from '+start_date.strftime('%d/%m/%Y')+' to '+end_date.strftime('%d/%m/%Y')

        journal_entry_1.save()
        journal_entry_1.submit()


        return journal_entry,journal_entry_1

#def get_default_payroll_payable_account(company):
#	payroll_payable_account = frappe.get_cached_value('Company',
#		{"company_name": company},  "default_payroll_payable_account")

#	if not payroll_payable_account:
#		frappe.throw(_("Please set Default Payroll Payable Account in Company {0}")
#			.format(company))

#		return payroll_payable_account
