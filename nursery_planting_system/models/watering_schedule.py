from odoo import models,fields
from dateutil.relativedelta import relativedelta

class WateringSchedule(models.Model):
    _name="watering.schedule"
    _description="This model schedules the watering date of individual plant"
    _log_access=False

    plant_ID = fields.Text(string="Plant ID")
    watering_date = fields.Datetime(string="Watering_date")
    frequency = fields.Char(string="Frequency")
    date_of_planting = fields.Datetime(string="Date of planting",default = lambda self:fields.Datetime.today()+relativedelta(days=-7),copy=False)
