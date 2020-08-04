import frappe
from dateutil.relativedelta import relativedelta
from datetime import date 
from calendar import monthrange
from frappe.utils import nowdate

def payroll_entry():
    paryroll_entry = frappe.new_doc('Payroll Entry')
    paryroll_entry.payroll_frequency = 'Monthly'
    paryroll_entry.validate_attendance = 1
    today = date.today()
    d = today - relativedelta(months = 2)
    first_day = date(d.year,d.month,1)
    paryroll_entry.start_date = first_day
    paryroll_entry.end_date = first_day.replace(day = monthrange(first_day.year, first_day.month)[1])

    paryroll_entry.flags.ignore_permissions  = True
    paryroll_entry.update({
        'payroll_frequency': paryroll_entry.payroll_frequency,
        'validate_attendance': paryroll_entry.validate_attendance,
        'start_date': paryroll_entry.start_date,
        'end_date': paryroll_entry.end_date
    }).insert()

    employee_list = frappe.db.sql("""select employee,employee_name,department,designation
        from tabEmployee where status = 'Active'""",as_dict = 1)

    number_of_employees = 0
    for item in employee_list:
        number_of_employees = number_of_employees + 1
        paryroll_entry.append('employees', {
            'employee': item.employee,
            'employee_name': item.employee_name,
            'department': item.department,
            'designation': item.designation,
        })

    paryroll_entry.number_of_employees = number_of_employees
    paryroll_entry.save()
    paryroll_entry.submit()


    return paryroll_entry