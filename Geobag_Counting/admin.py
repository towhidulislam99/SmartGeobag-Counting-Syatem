from django.contrib import admin

from .models import GeobagRiverBank,FilledRiverBank,PrototypeProposed,PreparingDataset,TestingProcedures

admin.site.register(GeobagRiverBank)
admin.site.register(FilledRiverBank)
admin.site.register(PrototypeProposed)
admin.site.register(PreparingDataset)
admin.site.register(TestingProcedures)