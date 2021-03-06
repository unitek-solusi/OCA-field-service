# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class Agreement(models.Model):
    _inherit = 'agreement'

    service_order_count = fields.Integer(
        compute='_compute_service_order_count',
        string='# Service Orders'
    )
    equipment_count = fields.Integer('# Equipments',
                                     compute='_compute_equipment_count')
    fsm_location_id = fields.Many2one('fsm.location', string="FSM Location")

    @api.multi
    def _compute_service_order_count(self):
        for agreement in self:
            res = self.env['fsm.order'].search_count(
                [('agreement_id', '=', agreement.id)])
            agreement.service_order_count = res or 0

    @api.multi
    def action_view_service_order(self):
        for agreement in self:
            fsm_order_ids = self.env['fsm.order'].search(
                [('agreement_id', '=', agreement.id)])
            action = self.env.ref(
                'fieldservice.action_fsm_operation_order').read()[0]
            if len(fsm_order_ids) == 0 or len(fsm_order_ids) > 1:
                action['domain'] = [('id', 'in', fsm_order_ids.ids)]
            elif len(fsm_order_ids) == 1:
                action['views'] = [(
                    self.env.ref('fieldservice.fsm_order_form').id,
                    'form')]
                action['res_id'] = fsm_order_ids.ids[0]
            else:
                action = {'type': 'ir.actions.act_window_close'}
            return action

    @api.multi
    def _compute_equipment_count(self):
        data = self.env['fsm.equipment'].read_group(
            [('agreement_id', 'in', self.ids)],
            ['agreement_id'], ['agreement_id'])
        count_data = dict((item['agreement_id'][0],
                           item['agreement_id_count']) for item in data)
        for agreement in self:
            agreement.equipment_count = count_data.get(agreement.id, 0)

    @api.multi
    def action_view_fsm_equipment(self):
        for agreement in self:
            equipment_ids = self.env['fsm.equipment'].search(
                [('agreement_id', '=', agreement.id)])
            action = self.env.ref(
                'fieldservice.action_fsm_equipment').read()[0]
            if len(equipment_ids) == 0 or len(equipment_ids) > 1:
                action['domain'] = [('id', 'in', equipment_ids.ids)]
            elif len(equipment_ids) == 1:
                action['views'] = [(
                    self.env.ref('fieldservice.fsm_equipment_form').id,
                    'form')]
                action['res_id'] = equipment_ids.ids[0]
            else:
                action = {'type': 'ir.actions.act_window_close'}
            return action
