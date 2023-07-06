from . import __version__ as app_version

app_name = "club_customization"
app_title = "Club Customization"
app_publisher = "Ahmed"
app_description = "the club customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ahmed751995@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/club_customization/css/club_customization.css"
# app_include_js = "/assets/club_customization/js/club_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/club_customization/css/club_customization.css"
# web_include_js = "/assets/club_customization/js/club_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "club_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "club_customization.install.before_install"
# after_install = "club_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "club_customization.uninstall.before_uninstall"
# after_uninstall = "club_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "club_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	# "ToDo": "custom_app.overrides.CustomToDo"
	"Attendance": "club_customization.overrides.custom_attendance.CustomAttendance"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
#	"all": [
#		"club_customization.tasks.all"
#	],
#	"daily": [
#		"club_customization.tasks.daily"
#	],
#	"hourly": [
#		"club_customization.tasks.hourly"
#	],
#	"weekly": [
#		"club_customization.tasks.weekly"
#	]
#	"monthly": [
#		"club_customization.tasks.monthly"         
#	]
    "cron": {
        "1 0 1 7 *": [
            "club_customization.overrides.custom_sales_invoice.renew_members_subscriptions"
        ]
    }
}

# Testing
# -------

# before_tests = "club_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "club_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "club_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["club_customization.utils.before_request"]
# after_request = ["club_customization.utils.after_request"]

# Job Events
# ----------
# before_job = ["club_customization.utils.before_job"]
# after_job = ["club_customization.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"club_customization.auth.validate"
# ]

