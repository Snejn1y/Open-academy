from odoo import models, fields, api



class Wizard(models.Model):

    _name = 'school.wizard'

    session = fields.Many2one('school.session', default=lambda self: self.env['school.session'].browse(self._context.get('active_id')))
    attendees = fields.Many2many('res.partner')

    def add_attendees(self):
        for record in self.attendees:
            record.attendees = self.attendees