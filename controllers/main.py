import logging

from odoo.http import request, JsonRequest, Response
from odoo.tools import date_utils
from odoo import _, http

LOGGER = logging.getLogger(__name__)


class Controller(http.Controller):
    @http.route('/api/v1/task_create', type='json', methods=['POST'], csrf=False, auth='public', website=True)
    def create(self, **post):
        res = request.jsonrequest
        su_task = request.env['task'].sudo()

        response = {}
        if res:
            su_task.create({'name': res.get('name'),'description': res.get('description'), 'user_id': res.get('user_id'),'duration': res.get('duration'), 'status': 'draft'})
            response.update({'message': 'Task created'})
        return response

    @http.route('/api/v1/task_start', type='json', methods=['POST'], csrf=False, auth="public", website=True)
    def start(self, **rec):
        res = request.jsonrequest
        su_task = request.env['task'].sudo()

        response = {}
        if res:
            task = su_task.search([('user_id', '=', res.get('user_id')), ('name', '=', res.get('name')), ('status', '=', 'draft')],limit=1)
            if task:
                task.action_progress()
                response.update({'message': 'Task %s in progress' % task.name})
        return response

    @http.route('/api/v1/task_done', type='json', methods=['POST'], csrf=False, auth="public", website=True)
    def done(self, **rec):
        res = request.jsonrequest
        su_task = request.env['task'].sudo()

        response = {}
        if res:
            task = su_task.search([('user_id', '=', res.get('user_id')), ('name', '=', res.get('name')), ('status', '=', 'in_progess')], limit=1)
            if task:
                task.action_complete()
                response.update({'message': 'Task %s status set to complete' % task.name})
        return response
