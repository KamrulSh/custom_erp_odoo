from odoo import models, fields, api


class CreateDailyReport(models.Model):
    _name = 'employee.dailyreport'
    _description = 'employee dailyreport'

    def _default_employee_name(self):
        return self.env.user.employee_id

    def _default_department_name(self):
        return self.env.user.department_id.id

    name = fields.Many2one('hr.employee', string="Employee", default=_default_employee_name, required=True,
                           ondelete='cascade', index=True, readonly=True)
    department = fields.Many2one('hr.department', string="Department", default=_default_department_name, required=True,
                                 ondelete='cascade', index=True, readonly=False)
    report_date = fields.Date(string="Offer Start Date", default=lambda self: fields.Date.today(), required=True)
    office_in_time = fields.Float(string="Office In Time", digits=(12, 2), copy=False)
    office_out_time = fields.Float(string="Office Out Time", digits=(12, 2), copy=False)
    work_duration = fields.Float(compute="_work_duration", store=True)
    mail_sent = fields.Boolean(default=False, string="Mail Sent")
    activity = fields.One2many('dailyreport.activity', 'report', string="Activities")
    activity_details_id = fields.One2many('dailyreport.activity', 'report_activity_ids', string="Activities details")
    achievement = fields.Text(string='Achievement')
    problems = fields.Text(string='Problems')
    solutions = fields.Text(string='Solutions')

    @api.depends('office_in_time', 'office_out_time')
    def _work_duration(self):
        for record in self:
            record.work_duration = float(record.office_out_time - record.office_in_time)
