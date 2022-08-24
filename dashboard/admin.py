from django.contrib import admin

from dashboard.models import elec_res, my_team, voterlist

# Register your models here.
admin.site.register(voterlist)
admin.site.register(elec_res)
admin.site.register(my_team)