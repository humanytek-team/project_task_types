from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    line_type = fields.Selection([
        ('DS', 'Design'),
        ('TL', 'Team Lead'),
        ('PP', 'PrePress'),
        ('AE', 'Account Executive'),
        ('CR', 'Creative director'),
        ('ART', 'Art direction'),
        ('ILL', 'Ilustration'),
        ('BE', 'Bench'),
        ('REN', 'Render'),
        ('ANI', 'Video Animation'),
        ('CGI', 'CGI'),
        ('ED', 'Video Edition'),
        ('COPY', 'Copy'),
        ('INC', 'Incidence'),
        ('PPT', 'Power Point'),
        ('COO', 'Coordination'),
        ('WEB', 'Web Programmer'),
        ('TR', 'Trainning'),
    ], required=True)
