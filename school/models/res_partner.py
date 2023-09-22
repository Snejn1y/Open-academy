from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string="Instructor")

    session = fields.Many2many('school.session')