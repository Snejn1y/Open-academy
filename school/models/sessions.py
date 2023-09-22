# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError



class Session(models.Model):
    _name = 'school.session'
    _description = 'Session'

    name = fields.Char(required=True)
    description = fields.Char()
    start_date = fields.Date(default=datetime.today())
    duration = fields.Integer()
    number_of_seats = fields.Integer()
    percent_seats = fields.Integer(compute='_compute_percent')

    instructor = fields.Many2one('res.partner', domain=['|', ('instructor', '=', True),
                                                        ('category_id.name', 'ilike', 'Teacher / Level')])
    course = fields.Many2one('school.course')

    attendees = fields.Many2many('res.partner')

    active = fields.Boolean(default=True)


    @api.depends('number_of_seats', 'attendees')
    def _compute_percent(self):
        for seat in self:
            seat.percent_seats = len(seat.attendees) / seat.number_of_seats * 100 if seat.number_of_seats > 0 else 0

    @api.onchange('number_of_seats')
    def nos(self):
        for seats in self:
            if seats.number_of_seats < 0:
                return {
                    'warning': {
                        'title': "Something bad happened",
                        'message': "Number of seats cant be a negative",
                    }
                }
            elif seats.number_of_seats < len(seats.attendees):
                return {
                    'warning': {
                        'title': "Something bad happened",
                        'message': "Number of seats cant be < than attendees amount",
                    }
                }

    @api.onchange('attendees')
    def noa(self):
        for seats in self:
            if len(seats.attendees) > seats.number_of_seats:
                return {
                    'warning': {
                        'title': "Something bad happened",
                        'message': "Attendees amount cant be > than number of seats",
                    }
                }

    @api.constrains('attendees')
    def attendees_check(self):
        for record in self:
            if record.instructor in record.attendees:
                raise ValidationError(f"Instructor {record.instructor.name} can be in attendees list")
