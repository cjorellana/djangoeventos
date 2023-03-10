from django.contrib import admin
from .models import Evento,Persona,Pais,Contacto

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display= ["nombre","precio","inicio","fin","ultimo","diploma","foto","activo"
        ,"created_by","created_at"]
    #list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["activo","diploma","inicio"]
    exclude = ["created_by", "created_at"]


admin.site.register(Evento,EventoAdmin)
admin.site.register(Persona)
admin.site.register(Pais)
admin.site.register(Contacto)
