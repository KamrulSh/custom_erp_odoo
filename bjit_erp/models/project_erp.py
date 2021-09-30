from odoo import models, fields


class ErpProject(models.Model):
    _inherit = 'project.project'
    _description = 'Project'

    name = fields.Char(string='Name')

    # setting
    projectid = fields.Char(string="Project ID")
    p_department = fields.Char(string="Department")
    p_department_head = fields.Char(string="Department Head")
    project_status = fields.Selection([
                ('complete', 'Complete'),
                ('running', 'Running')],
                string='Project Status')
    project_type = fields.Selection([
                ('sm_easy', 'Small and Easy'),
                ('medium', 'Medium'),
                ('hard', 'Hard')],
                string='Project Type')

    project_tech = fields.Selection([
        ('odoo', 'Odoo'),
        ('python', 'Python')],
        string='Project Technology')

    last_modified_on = fields.Date(string='Last Modified on')
    created_on = fields.Date(string='Created on')
    start_date = fields.Date(string='Start Date')
    project_close_date = fields.Date(string='Project Close Date')
    project_lesson = fields.Text(string='Project Lesson Learn')
    project_matrices = fields.Text(string='Project matrices')
    project_modules = fields.Text(string='Project Modules')
