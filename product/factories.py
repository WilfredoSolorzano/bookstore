import factory
from factory.django import DjangoModelFactory
from django.apps import apps


def get_category_model():
    return apps.get_model('product', 'Category')


def get_product_model():
    return apps.get_model('product', 'Product')


class CategoryFactory(DjangoModelFactory):
    # Cambia 'name' por 'title' si ese es el campo real
    title = factory.Faker("word")  # ¡IMPORTANTE! Cambié name por title
    slug = factory.Faker("slug")
    description = factory.Faker("sentence")
    active = factory.Iterator([True, False])

    class Meta:
        model = get_category_model()


class ProductFactory(DjangoModelFactory):
    price = factory.Faker("pydecimal", left_digits=4, right_digits=2, positive=True)
    title = factory.Faker("sentence", nb_words=3)
    description = factory.Faker("paragraph")

    # REMUEVE 'in_stock' y 'image_url' si no existen en tu modelo

    class Meta:
        model = get_product_model()

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)
        else:
            self.category.add(CategoryFactory())