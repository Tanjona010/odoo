from odoo import models, fields, api


class TextileProject(models.Model):
    _name = "textile.project"
    _description = "Project"

    name = fields.Char(required=True)
    client_id = fields.Many2one("textile.client", string="Client")
    material_cost = fields.Float(string="Material Cost")
    labor_cost = fields.Float(string="Labor Cost")
    total_cost = fields.Float(
        string="Total Cost",
        compute="_compute_total_cost",
        store=True,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
        ],
        default="draft",
        string="Status",
    )

    @api.depends("material_cost", "labor_cost")
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.material_cost + record.labor_cost

    def action_start(self):
        self.write({"state": "in_progress"})

    def action_done(self):
        self.write({"state": "done"})
