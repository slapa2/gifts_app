from django.contrib import admin

from .models import GiftList, Gift, GiftShopLink

admin.site.register(GiftList)

admin.site.register(Gift)

admin.site.register(GiftShopLink)