from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class GiftList(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='giftLists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shared_to = models.ManyToManyField(User, related_name='shared_gift_lists')

    def __str__(self):
        return self.name


class Gift(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    gift_list = models.ForeignKey(GiftList, on_delete=models.CASCADE, related_name='gifts')
    reservate_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    reversed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GiftShopLink(models.Model):
    url = models.URLField()
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, related_name='shop_urls')

    def __str__(self):
        return self.url

