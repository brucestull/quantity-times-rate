from django.db import models


class Consumable(models.Model):
    """
    Model for a `Consumable` item.
    """

    name = models.CharField(
        help_text="The name of the consumable.",
        max_length=30,
    )
    unit = models.CharField(
        help_text="The unit of the consumable. (e.g. kg, g, l, ml, etc.)",
        max_length=10,
    )
    cost_per_unit = models.DecimalField(
        help_text="The cost per unit of the consumable.",
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        """
        String representation of `Category`.
        """
        return (
            self.name
            + " ("
            + self.unit
            + ")"
            + " - $"
            + str(self.cost_per_unit)
            + "/"
            + self.unit
        )

    class Meta:
        verbose_name_plural = "Consumables"


class ConsumableInstance(models.Model):
    consumables = models.ForeignKey(
        Consumable,
        on_delete=models.SET_NULL,
        null=True,
    )
    quantity = models.DecimalField(
        help_text="The quantity of the consumable.",
        max_digits=10,
        decimal_places=2,
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    def get_current_cost_of_consumables(self):
        """
        Returns the current cost of the consumable.
        """
        return self.consumables.cost_per_unit * self.quantity

    def save(self, *args, **kwargs):
        self.cost = self.get_current_cost_of_consumables()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of `ConsumableInstance`.
        """
        return (
            str(self.consumables)
            + " - "
            + str(self.quantity)
            + " "
            + self.consumables.unit
            + " - $"
            + str(self.cost)
        )
