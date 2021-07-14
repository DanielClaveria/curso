# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'cooperative.task'
    _description_ = 'Tasks info'
    
    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    start = fields.Datetime(string='Start')
    end = fields.Datetime(string='End')
    repeat = fields.Boolean(string='Repeat?')
    frecuence = fields.Selection([('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'),],'Frecuence')
    
