from django.db import models
from django.utils.text import slugify

# 1. بلاگ کے لیے ماڈل
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# 2. مارکیٹ پلیس (گیسٹ پوسٹنگ سائٹس) کے لیے ماڈل
class MarketplaceSite(models.Model):
    domain_name = models.CharField(max_length=255)
    da = models.IntegerField(verbose_name="Domain Authority")
    dr = models.IntegerField(verbose_name="Domain Rating")
    traffic = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    link_type = models.CharField(max_length=50, default="Do-Follow")

    def __str__(self):
        return self.domain_name

# 3. کانٹیکٹ فارم (لیڈز) کے لیے ماڈل
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"