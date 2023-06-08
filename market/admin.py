from django.contrib import admin

from market.models import Consumable, ConsumableInstance


@admin.register(Consumable)
class ConsumableAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "unit",
        "cost_per_unit",
    )
    list_filter = (
        "name",
        "unit",
        "cost_per_unit",
    )
    search_fields = (
        "name",
        "unit",
        "cost_per_unit",
    )


@admin.register(ConsumableInstance)
class ConsumableInstanceAdmin(admin.ModelAdmin):
    list_display = (
        # Currently showing the `__str__` method of the `Consumable` model. This may change to just return `consumable.name` in the future.
        "consumable",
        "cost",
        "quantity",
    )
    list_filter = (
        "consumable",
        "cost",
        "quantity",
    )
    search_fields = (
        # "consumable", # This is a ForeignKey, so it is not searchable.
        "quantity",
    )
    readonly_fields = (
        "cost",
    )
