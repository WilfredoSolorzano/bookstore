#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        # Primero crear un usuario (si Order necesita user)
        self.user = UserFactory()

        # Crear productos con categorías
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()

        # OrderFactory probablemente espera productos como parámetro 'products'
        # o necesita ser creado de otra forma
        self.order = OrderFactory(
            user=self.user,  # Si Order tiene campo user
            products=[self.product_1, self.product_2]  # Depende de cómo esté definido OrderFactory
        )
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data

        # Verificar que el serializer funciona
        self.assertIn("products", serializer_data)

        # Si el serializer incluye datos de productos
        if "products" in serializer_data and len(serializer_data["products"]) > 0:
            # Ajustar según cómo esté estructurado tu serializer
            self.assertEqual(
                serializer_data["products"][0]["title"],
                self.product_1.title
            )
            self.assertEqual(
                serializer_data["products"][1]["title"],
                self.product_2.title
            )