from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Club(models.Model):
    name= models.CharField(max_length=255, null=False, blank=True)
    fan = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    details=models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("club_detail", kwargs={"pk": self.pk})
