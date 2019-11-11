from django.contrib import admin
from webay.models import UserProfile, Bid, Auction, Item

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Bid)
admin.site.register(Auction)
admin.site.register(Item)

