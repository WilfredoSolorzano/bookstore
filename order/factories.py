import factory
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from order.models import Order, OrderItem
from product.factories import ProductFactory

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', 'password123')


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # Crear OrderItems para cada producto
            for product in extracted:
                OrderItem.objects.create(
                    order=self,
                    product=product,
                    quantity=1,
                    price=product.price
                )
        else:
            # Crear un producto por defecto
            product = ProductFactory()
            OrderItem.objects.create(
                order=self,
                product=product,
                quantity=1,
                price=product.price
            )