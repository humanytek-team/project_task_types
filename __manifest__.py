{
    "name": "Project Task Types",
    "version": "17.0.1.0.1",
    "author": "Humanytek",
    "website": "http://humanytek.com",
    "depends": [
        "account",
        "hr_timesheet",
        "project",
        "sale_timesheet_enterprise",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/account_analytic_line_type.xml",
        "views/project_task.xml",
        "views/project_task_create_timesheet.xml",
    ],
    "installable": True,
    "application": False,
}
