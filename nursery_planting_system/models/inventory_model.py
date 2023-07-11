from odoo import models,fields

class InventoryModel(models.Model):
    _name="inventory.model"
    _description="Manage the inventory of plants"

    plant_ID = fields.Text(string="Plant ID",required=True)
    quantity = fields.Integer(string="Quantity(in stock)")