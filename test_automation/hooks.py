# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "test_automation"
app_title = "test-automation"
app_publisher = "frappe"
app_description = "payroll process automation using sceduler"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "test@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/test_automation/css/test_automation.css"
# app_include_js = "/assets/test_automation/js/test_automation.js"

# include js, css files in header of web template
# web_include_css = "/assets/test_automation/css/test_automation.css"
# web_include_js = "/assets/test_automation/js/test_automation.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
	"Salary Slip" : "public/js/salary_slip.js"
	}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "test_automation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "test_automation.install.before_install"
# after_install = "test_automation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "test_automation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
#	"all": [
#        "test_automation.task.payroll_entry"
 	#	"test_automation.tasks.all"
# 	]
# 	"daily": [
# 		"test_automation.tasks.daily"
# 	],
# 	"hourly": [
# 		"test_automation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"test_automation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"test_automation.tasks.monthly"
# 	]
}

# Testing
# -------

# before_tests = "test_automation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "test_automation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "test_automation.task.get_dashboard_data"
# }

