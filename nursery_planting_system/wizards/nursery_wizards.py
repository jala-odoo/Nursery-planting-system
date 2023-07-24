from odoo import models,fields

class NurseryWizards(models.TransientModel):
    _name = "nursery.wizards"
    _description = "showing wizard to add specific watering date to every plant"
    _inherit = "watering.schedule"


    def add_date(self):
        list_of_plants = self.env.context.get('active_ids',[])
        dates = self.env['watering.schedule']

        for plant_ID in list_of_plants:
            watering_date_ids = {
                'plant_ID' : plant_ID,
                'watering_date' : self.watering_date,
                'quantity' : self.quantity,
            }
            dates.create(watering_date_ids)


