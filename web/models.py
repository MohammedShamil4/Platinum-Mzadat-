from django.db import models
from django.core.validators import MinValueValidator
from django.utils.functional import cached_property
import uuid

# ---------------- Sale Item ----------------
class SaleItem(models.Model):
    name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    multiple_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# ---------------- Order ----------------
class Order(models.Model):
    document_number = models.CharField(max_length=20, unique=True, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_discount = models.DecimalField(max_digits=30, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.document_number:
            self.document_number = "DOC-" + uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)

    @cached_property
    def items(self):
        return self.orderitem_set.all()

    @cached_property
    def order_item_discount_total(self):
        return sum([item.item_discount for item in self.items])

    @cached_property
    def order_tax_total(self):
        return sum([item.tax_amount for item in self.items])

    @cached_property
    def subtotal_before_order_discount(self):
        return sum([item.total_price for item in self.items])

    @cached_property
    def order_total(self):
        total = self.subtotal_before_order_discount - self.order_discount
        return max(total, 0)

    @cached_property
    def order_discount_total(self):
        return self.order_discount + self.order_item_discount_total

    def __str__(self):
        return f"{self.document_number}"


# ---------------- Order Item ----------------
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sale_item = models.ForeignKey(SaleItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    item_discount = models.DecimalField(max_digits=30, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.sale_item.multiple_allowed and self.quantity > 1:
            self.quantity = 1
        super().save(*args, **kwargs)

    @cached_property
    def price_without_discount(self):
        return self.sale_item.rate * self.quantity

    @cached_property
    def price_after_discount(self):
        return max(self.price_without_discount - self.item_discount, 0)

    @cached_property
    def tax_amount(self):
        return self.sale_item.tax * self.quantity

    @cached_property
    def total_price(self):
        return self.price_after_discount + self.tax_amount

    def __str__(self):
        return f"{self.sale_item.name} x {self.quantity}"