from odoo import models, fields

class Course(models.Model):
    _name = "school.course"
    _description = "Course"

    name = fields.Char(required=True)
    description = fields.Text()