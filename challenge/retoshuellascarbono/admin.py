from django.contrib import admin
from .models import Retos, Retosrespuesta, Poemas, Dibujos, Rankings
# Register your models here.
@admin.register(Retos)
class RetosAdmin(admin.ModelAdmin):
    pass

@admin.register(Retosrespuesta)
class RetosrespuestasAdmin(admin.ModelAdmin):
    pass

@admin.register(Poemas)
class PoemasAdmin(admin.ModelAdmin):
    pass

@admin.register(Dibujos)
class DibujosAdmin(admin.ModelAdmin):
    pass

@admin.register(Rankings)
class RankingAdmin(admin.ModelAdmin):
    pass