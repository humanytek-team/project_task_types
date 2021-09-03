# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProjectTaskCreateTimesheet(models.TransientModel):
    _inherit = "project.task.create.timesheet"

    line_type_id = fields.Many2one(
        comodel_name="account.analytic.line.type",
        required=True,
        string="Type",
    )

    def save_timesheet(self):
        account_analytic_line = super(ProjectTaskCreateTimesheet, self).save_timesheet()
        account_analytic_line.line_type_id = self.line_type_id
        return account_analytic_line
