# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import datetime
import logging
from datetime import timedelta

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class Task(models.Model):
    _name = 'task'
    _description = 'Task Scheduling'
    _inherit = [
                'mail.thread.phone',
                'mail.activity.mixin',
               ]

    user_id = fields.Many2one('res.users', string='Assigned To', required=True, store=True)
    phone = fields.Char(related='user_id.phone')
    mobile = fields.Char(related='user_id.mobile')
    name = fields.Char(string='Task', required=True)
    description = fields.Text(string='Description', required=True)
    start = fields.Date()
    duration = fields.Integer(string='Days Allocation')
    stop = fields.Date(required=True, compute='_compute_stop')
    status = fields.Selection([('draft', 'New'), ('in_progess', 'In Progress'), ('complete', 'Completed'), ('expired', 'Expired')], string='Status', default='draft')

    @api.depends('duration')
    def _compute_stop(self):
        self.ensure_one()
        self.stop = datetime.datetime.now() + timedelta(days=self.duration) 

    def action_progress(self):
        if self.status not in 'draft':
            return
        self.write({'status': 'in_progess', 'start': fields.Date.today()})

    def action_complete(self):
        self.write({'status': 'complete'})

    def _autopost_expired_entries(self):
        
        ''' This method is called from a cron job.
        It is used to change status of expired entries.
        '''
        records = self.search([
            ('status', '=', 'in_progress'),
            ('stop', '<=', fields.Date.context_today(self)),
        ])

        for record in records:
            record.write({'status': 'expired'})
    
    def _phone_get_number_fields(self):
        """ Use mobile or phone fields to compute sanitized phone number """
        return ['mobile', 'phone']
