from django.db import models


class CommandStatus(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)


class Command(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, null=False, blank=False)
    pizza_ordered = models.ForeignKey('pizzas.PricePizza', on_delete=models.CASCADE, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(CommandStatus, on_delete=models.CASCADE, null=False, blank=False)


class IngredientByClient(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE, null=False, blank=False)
    ingredient_topping = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField(default=1)
    description = models.CharField(max_length=300, default="")