from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm, modelform_factory, inlineformset_factory
from .models import SaleItem, Order, OrderItem
from decimal import Decimal

# ---------------- Home ----------------
def home(request):
    return render(request, 'home.html')


# ---------------- SaleItem ----------------
class SaleItemForm(ModelForm):
    class Meta:
        model = SaleItem
        fields = ['name', 'rate', 'tax', 'multiple_allowed']


def add_saleitem(request):
    if request.method == 'POST':
        form = SaleItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_saleitems')
    else:
        form = SaleItemForm()
    return render(request, 'add_saleitem.html', {'form': form})


def list_saleitems(request):
    items = SaleItem.objects.all()
    return render(request, 'list_saleitems.html', {'items': items})


# ---------------- Order Forms ----------------
# Order form
OrderForm = modelform_factory(Order, fields=["order_discount"])


# Order item formset
OrderItemFormSet = inlineformset_factory(
    Order,
    OrderItem,
    fields=["sale_item", "quantity", "item_discount"],
    extra=1,
    can_delete=True
)


# CREATE ORDER
def create_order(request):

    if request.method == "POST":

        order_discount_raw = request.POST.get("order_discount", "0")

        try:
            order_discount = Decimal(order_discount_raw)
        except:
            order_discount = Decimal("0")


        order_form = OrderForm({"order_discount": order_discount})
        formset = OrderItemFormSet(request.POST)


        if order_form.is_valid() and formset.is_valid():

            order = order_form.save()

            formset.instance = order
            items = formset.save(commit=False)

            total = Decimal("0")

            for item in items:

                sale_item = item.sale_item

                price = sale_item.rate * item.quantity
                price = Decimal(price)

                item.price_without_discount = price

                item_discount = item.item_discount or Decimal("0")

                # If order discount exists ignore item discounts
                if order_discount > 0:
                    item_discount = Decimal("0")
                    item.item_discount = Decimal("0")

                tax = sale_item.tax

                total += price - item_discount + tax

                item.save()


            # Apply order discount to whole order
            if order_discount > 0:
                total = total - order_discount


            order.order_total = total
            order.save()

            return redirect("order_detail", order_id=order.id)


        else:

            print("Order Form Errors:", order_form.errors)
            print("Formset Errors:", formset.errors)


    else:

        order_form = OrderForm()
        formset = OrderItemFormSet()


    return render(request, "create_order.html", {
        "order_form": order_form,
        "formset": formset
    })

# ---------------- Order Detail View ----------------
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})



def list_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'list_orders.html', {'orders': orders})