from odoo import models, fields, api


class EmployeesInformation(models.Model):
    _inherit = 'hr.employee'
    _description = "Employee Info"

    skype_id = fields.Char(string="Skype ID")
    employee_type = fields.Char(string="Employee Type")