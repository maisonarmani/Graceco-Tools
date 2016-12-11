# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "graceco_tools"
app_title = "Graceco Tools"
app_publisher = "bobzz.zone@gmail.com"
app_description = "by bobby"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/graceco_tools/css/graceco_tools.css"
# app_include_js = "/assets/graceco_tools/js/graceco_tools.js"

# include js, css files in header of web template
# web_include_css = "/assets/graceco_tools/css/graceco_tools.css"
# web_include_js = "/assets/graceco_tools/js/graceco_tools.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"
fixtures = ['Custom Field','Print Format','Workflow','Workflow State','Workflow Action','Role']
# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "graceco_tools.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "graceco_tools.install.before_install"
# after_install = "graceco_tools.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "graceco_tools.notifications.get_notification_config"

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

# scheduler_events = {
# 	"all": [
# 		"graceco_tools.tasks.all"
# 	],
# 	"daily": [
# 		"graceco_tools.tasks.daily"
# 	],
# 	"hourly": [
# 		"graceco_tools.tasks.hourly"
# 	],
# 	"weekly": [
# 		"graceco_tools.tasks.weekly"
# 	]
# 	"monthly": [
# 		"graceco_tools.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "graceco_tools.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "graceco_tools.event.get_events"
# }

