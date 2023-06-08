from django.db import models


class Consumable(models.Model):
    """
    Model for a `Consumable` item. It is used to keep track of the consumables
    that are used in the market. It will be used to store the current cost
    of the consumable used in the `Market` application.

    Attributes:
        name (CharField): The name of the consumable.
        unit (CharField): The unit of the consumable. (e.g. kg, g, mg, l, ml, etc.)
        cost_per_unit (DecimalField): The cost per unit of the consumable.
    """

    name = models.CharField(
        help_text="The name of the consumable.",
        max_length=30,
    )
    unit = models.CharField(
        help_text="The unit of the consumable. (e.g. kg, g, mg, l, ml, etc.)",
        max_length=10,
    )
    cost_per_unit = models.DecimalField(
        help_text="The cost per unit of the consumable.",
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        """
        String representation of `Consumable`.
        """
        # Remember that f-string interpolation is our friend.
        return f"{self.name} (${self.cost_per_unit}/{self.unit})"

    class Meta:
        verbose_name_plural = "Consumables"


class ConsumableInstance(models.Model):
    """
    This model represents an instance of use of a `Consumable`. It is used
    to store the cost of the consumable at the time of creation as well
    as the quantity of the `Consumable` used in the instance.

    Attributes:
        consumable (ForeignKey): The consumable that was used.
        quantity (DecimalField): The quantity of the consumable that was
        used.
        cost (DecimalField): The cost of the consumable at the time of
        creation.
    """

    consumable = models.ForeignKey(
        Consumable,
        on_delete=models.SET_NULL,
        null=True, # May keep or remove this in the future.
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

    def get_current_cost_of_consumable(self):
        """
        Returns the current cost of the consumable.
        """
        return self.consumable.cost_per_unit * self.quantity

    def save(self, *args, **kwargs):
        self.cost = self.get_current_cost_of_consumable()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of `ConsumableInstance`. It includes the name,
        unit, cost, and quantity of the consumable.
        """
        # Remember that f-string interpolation is our friend.
        return (
            f"{self.consumable.name} (${self.cost} | "
            f"{self.quantity} {self.consumable.unit})"
        )
