# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
    _name = 'school.course'
    _description = 'Open academy courses'

    name = fields.Char(required=True)
    description = fields.Char()

    responsible_user = fields.Many2one('res.users')

    session = fields.Many2many('school.session', 'course')

    _sql_constraints = [
        ('name_diff', 'CHECK (description <> title)', "Session name cant be same of it description"),
        ('name_uniq', 'UNIQUE (title)', "The session name must be unique")
    ]

    def copy(self, default={}):
        default['title'] = f"Copy of {self.title}"
        rn = super(Course, self).copy(default=default)
        return rn