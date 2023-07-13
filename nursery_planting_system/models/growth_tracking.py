from odoo import models,fields
from dateutil.relativedelta import relativedelta

class GrowthTrackingModel(models.Model):
    _name="growth.tracking"
    _description="track the growth of the plants"
    _order = "plant_ID desc"

    plant_ID=fields.Char(string="Plant ID")
    curr_height = fields.Float(string="Current height")
    curr_width = fields.Float(string="Current width")
    health_status = fields.Selection([('H','healthy'),('UH','unhealthy'),('NW','Need Water')],string="Health Status")
    last_watering_date = fields.Date(string="Last Watering date")
    last_fertilization_date = fields.Date(string="Last fertilization date")