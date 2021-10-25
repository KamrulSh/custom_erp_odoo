from odoo import models, fields, api


class EmployeesInformation(models.Model):
    _inherit = 'res.users'
    _description = "Inherit Contact Info"
