from django.contrib import admin
from home.models import user
from home.models import appointment,event_benefits,history

# Register your models here.
admin.site.register(user)
admin.site.register(appointment)
admin.site.register(event_benefits)
admin.site.register(history)
# admin.site.register(appointment)



