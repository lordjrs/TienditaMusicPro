
from unittest import result
from django.conf.urls import url
from django.http import response
from rest_framework.test import APITestCase

# Models
from products.models import Product

# Create your tests here.

class TestTiendita(APITestCase):
    url = "/api/producto/"

    def setUp(self):
        Product.objects.create(name="Guitarra",slug="instrumento",category="Instrumento de cuerda",image="foto.jpge",excerpt="cualquierwea",detail="detalle",price=1500000,available=True)


    def test_get_products(self):

        response=self.client.get(self.url)
        result=response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],"Guitarra")

    def test_post_products(self):
        #_definicion
        data = {
            "name":"Bajo",
            "slug": "instrumento",
            "category":"Intrumento de cuerda",
            "image": "image2.jpg",
            "excerpt": "nose",
            "detail": "detalles",
            "price":"500000",
            "available":"true"
        }
        #process
        response = self.client.post(self.url,data=data)
        result= response.json()

        #assert
        self.assertEqual(response.status_code,201)
        self.assertEqual(result["name"],"Bajo")

    def test_update_products(self):
        pk="1"
        data = {
            "name":"Flauta"
        }
        response = self.client.path(self.url + f"/{pk}",data=data)
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["name"],"Flauta")

    def test_delete_products(self):
        
        pk="1"

        response_del = self.client.delete(self.url + f"/{pk}")
        response_get = self.client.get(self.url + f"/{pk}")

        result = response_get.json()

        self.assertEqual(response_del.status_code, 204)
        self.assertEqual(response_get.status_code, 404)