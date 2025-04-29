from django.db import models


class Section_5(models.Model):
    PROJECT_TYPES = [
        ('Indoor Signage', 'Indoor Signage'),
        ('Outdoor Signage', 'Outdoor Signage'),
        ('Vinyl Sticker', 'Vinyl Sticker'),
        ('LED Display', 'LED Display'),
        ('Digital Signage', 'Digital Signage'),

    ]

    name = models.CharField(max_length=200)  # Project Name
    image = models.ImageField(upload_to='staticfiles/section_5/', blank=True, null=True)
    type = models.CharField(max_length=100, choices=PROJECT_TYPES)
    location = models.CharField(max_length=255, default='Unknown')
    details = models.TextField(blank=True)  # Project Details
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Section8(models.Model):
    client_name = models.CharField(max_length=100)
    client_role = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to='staticfiles/Section8/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5)
    message = models.TextField()
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.client_name} - {self.client_role}"