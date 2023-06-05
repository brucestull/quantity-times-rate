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
        "consumables",
        # This is a method defined in this class. We can see the return
        # value of this method in the admin panel list view.
        "current_cost_of_consumables",
        "quantity",
    )
    list_filter = (
        "consumables",
        "quantity",
    )
    search_fields = (
        # "consumables", # This is a ForeignKey, so it is not searchable.
        "quantity",
    )
    readonly_fields = (
        "cost",
    )

    def current_cost_of_consumables(self, obj):
        return obj.get_current_cost_of_consumables()
