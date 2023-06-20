from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Club
from django.contrib.auth import get_user_model



# Create your tests here.
class ClubsTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse("club_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("club_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "clubs/club-list.html")
        self.assertTemplateUsed(response, "_base.html")

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", email="teas@email.com", password="1234"
        )
        self.club = Club.objects.create(
            name="test", details="test info", fan=self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.club), "test")


    def test_detail_view(self):
        url = reverse("club_detail", args=[self.club.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "clubs/club-detail.html")

    def test_create_view(self):
        obj = {
            "name": "test2",
            "details": "info...",
            "fan": self.user.id,
        }
        url = reverse("club_create")
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertRedirects(response, reverse("club_detail", args=[2]))