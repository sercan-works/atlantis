from django.contrib import admin

from .models import Firma,PC,Kasa,PSU,MotherBoard,CPU,Ram,GPU,Monitor,Kulaklık,Klavye,Mouse,MousePad,Koltuk

admin.site.register(Firma)
admin.site.register(Kasa)
admin.site.register(PSU)
admin.site.register(MotherBoard)
admin.site.register(CPU)
admin.site.register(Ram)
admin.site.register(GPU)
admin.site.register(Monitor)
admin.site.register(Kulaklık)
admin.site.register(Klavye)
admin.site.register(Mouse)
admin.site.register(MousePad)
admin.site.register(Koltuk)

@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
