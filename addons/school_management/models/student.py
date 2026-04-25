from odoo import models, fields

class Student(models.Model):
    _name = "school.student"
    _description = "Student"

    name = fields.Char(required=True)
    age = fields.Integer()
    
    course_id = fields.Many2one("school.course", string="Course")