# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class hrPayrollStage(models.Model):
    _name = 'hr.payslip.stage'
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

class hrBatchStage(models.Model):
    _name = 'hr.payslip.run.stage'
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

    compute_sheet = fields.Boolean(
        string='Compute Sheet Button',
        required=False)
    confirm = fields.Boolean(
        string='Confirm Button',
        required=False)
    close = fields.Boolean(
        string='Close Button',
        required=False)


