# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ActivityReports(models.Model):
    _name = 'dailyreport.activity'
    _description = 'daily report activity'

    report = fields.Many2one('employee.dailyreport', string='report')

    start_time = fields.Float(string="Office In Time", digits=(12, 2), copy=False)
    end_time = fields.Float(string="Office Out Time", digits=(12, 2), copy=False)
    activity = fields.Text(string='Activity')

    report_activity_ids = fields.Many2one('employee.dailyreport', string='Activity report')

    starting_time = fields.Float(string="Office In Time", digits=(12, 2), copy=False)
    ending_time = fields.Float(string="Office Out Time", digits=(12, 2), copy=False)
    activity_details = fields.Text(string='Activity')
