from odoo import models,fields
from dateutil.relativedelta import relativedelta


class PlantModel(models.Model):
    _name = "plant.model"
    _description = "describe plant properties"
    _log_access = False

    plant_ID = fields.Text(string="Plant ID",required=True)
    name = fields.Char(string="Name")
    type = fields.Char(string="Type")
    species = fields.Text(string="Species",default="Unknown")
    price = fields.Float(string="Price")
    expected_harvest_date = fields.Datetime(string="Expected harvest date")
    date_of_planting = fields.Datetime(string="Date of planting",default = lambda self:fields.Datetime.today()+relativedelta(days=-7))