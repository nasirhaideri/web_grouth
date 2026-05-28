from django.contrib import admin
from .models import Post, MarketplaceSite

admin.site.register(Post)
admin.site.register(MarketplaceSite)
from .models import Post, MarketplaceSite, ContactMessage # اسے اپڈیٹ کریں
admin.site.register(ContactMessage)