{
    'name' : 'nursery planting system',
    'author' : "jala",
    'version' : '1.0',

    'depends' : ['base','mail','web'],
    'application' : True,

    'data' : [
       'security/ir.model.access.csv',
       'wizards/nursery_wizards.xml',
       'view/plant_model_view.xml',
       'view/watering_schedule_view.xml',
       'view/inventory_model_view.xml',
       'view/growth_tracking_view.xml',
       'view/nursery_menus.xml',
       'report/nursery_reports.xml',
       'report/nursery_templates.xml',
    ],

    'demo':[
        'demo/plant_demo.xml',
        'demo/watering_schedule_demo.xml',
    ],
}