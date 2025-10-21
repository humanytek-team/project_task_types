from odoo import api, fields, models


class TimeSheetAnalysisReport(models.Model):
    _inherit = "timesheets.analysis.report"

    line_type_id = fields.Many2one(
        "account.analytic.line.type",
        string="Type",
        # related="line_id.line_type_id",
        readonly=True,
    )

    @property
    def _table_query(self):
        return """
            SELECT A.*       
            FROM (
                %s %s %s
            ) A
        """ % (self._select(), self._from(), self._where())

    @api.model
    def _select(self):
        return (
            super()._select()
            + """,
                A.line_type_id AS line_type_id
        """
        )

    @api.model
    def _from(self):
        return (
            super()._from()
            + """
            LEFT JOIN account_analytic_line_type AAL ON A.line_type_id = AAL.id
        """
        )
