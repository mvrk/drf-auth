from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Drf


class DrfTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_drfs = Drf.objects.create(
            name="banana",
            purchaser=testuser1,
            description="",
        )
        test_drfs.save()

    def test_drfs_model(self):
        drf = Drf.objects.get(id=1)
        actual_purchaser = str(drf.purchaser)
        actual_name = str(drf.name)
        actual_description = str(drf.description)
        self.assertEqual(actual_purchaser, "testuser1")
        self.assertEqual(actual_name, "banana")
        self.assertEqual(
            actual_description, ""
        )

    def test_get_drf_list(self):
        url = reverse("drf_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drfs = response.data
        self.assertEqual(len(drfs), 1)
        self.assertEqual(drfs[0]["name"], "banana")

    def test_get_drf_by_id(self):
        url = reverse("drf_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Drf = response.data
        self.assertEqual(Drf["name"], "banana")

    def test_create_drf(self):
        url = reverse("drf_list")
        data = {"purchaser": 1, "name": "apple", 'color': 'red', "description": "fruit",
                "created_at": "2022-05-26T22:51:34.624349Z", "updated_at": "2022-05-26T22:51:34.624349Z"}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        drfs = Drf.objects.all()
        self.assertEqual(len(drfs), 2)
        self.assertEqual(Drf.objects.get(id=1).name, "banana")

    def test_update_drf(self):
        url = reverse("drf_detail", args=(1,))
        data = {
            "purchaser": 1,
            "name": "banana",
            "color": "yellow",
            "description": "fruit",
            # "created_at": "2022-08-29T17:51:34.622367Z", "updated_at": "2022-08-29T17:51:34.622367Z"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        drf = Drf.objects.get(id=1)
        self.assertEqual(drf.name, data["name"])
        self.assertEqual(drf.purchaser.id, data["purchaser"])
        self.assertEqual(drf.description, data["description"])

    def test_delete_drf(self):
        url = reverse("drf_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        drfs = Drf.objects.all()
        self.assertEqual(len(drfs), 0)
