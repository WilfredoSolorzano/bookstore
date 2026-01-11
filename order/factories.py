import factory
from order.models import Order, OrderItem
from product.factories import ProductFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                OrderItem.objects.create(
                    order=self,
                    product=product,
                    quantity=1
                )
