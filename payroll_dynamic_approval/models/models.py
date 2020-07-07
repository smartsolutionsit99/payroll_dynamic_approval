# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class hrPayrollStage(models.Model):
    _name = 'hr.payslip.stage'
    _order = 'sequence'
    _description = 'Payslip Approval Stages'

    _sql_constraints = [
        ('sequence_unique', 'UNIQUE (sequence)', _("Sequence Should Be Unque!"))
    ]

    name = fields.Char(string='Stage Name', required=True, translate=True)
    description = fields.Text(translate=True)
    sequence = fields.Integer(default=1)
    user_id = fields.Many2many(
        string="Users",
        comodel_name="res.users", required=True,
    )

    compute_sheet = fields.Boolean(
        string='Compute Sheet Button',
        required=False)
    confirm = fields.Boolean(
        string='Confirm Button',
        required=False)
    cancel = fields.Boolean(
        string='Cancel Button',
        required=False)
    refund = fields.Boolean(
        string='Refund Button',
        required=False)

class hrPayslip(models.Model):
    _inherit = 'hr.payslip'

    stage_id = fields.Many2one(
        comodel_name='hr.payslip.stage',
        string='Stages',
        default=lambda self:self.env['hr.payslip.stage'].search([], order='sequence')[0] or False,
        required=False)

    st_compute_sheet = fields.Boolean(
        string='Compute Sheet Button',
        related="stage_id.compute_sheet",
        required=False)
    st_confirm = fields.Boolean(
        string='Confirm Button',
        related="stage_id.confirm",
        required=False)
    st_cancel = fields.Boolean(
        string='Cancel Button',
        related="stage_id.cancel",
        required=False)
    st_refund = fields.Boolean(
        string='Refund Button',
        related="stage_id.refund",
        required=False)

class hrBatchStage(models.Model):
    _name = 'hr.payslip.run.stage'
    _order = 'sequence'
    _description = 'Payslip Batch Approval Stages'

    _sql_constraints = [
        ('sequence_unique', 'UNIQUE (sequence)', _("Sequence Should Be Unque!"))
    ]

    name = fields.Char(string='Stage Name', required=True, translate=True)
    description = fields.Text(translate=True)
    sequence = fields.Integer(default=1)
    user_id = fields.Many2many(
        string="Users",
        comodel_name="res.users", required=True,
    )

    generate_payslip = fields.Boolean(
        string='Generate Payslips Button',
        required=False)
    close = fields.Boolean(
        string='Close Button',
        required=False)


