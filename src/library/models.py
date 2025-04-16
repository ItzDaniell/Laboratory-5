from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    """Book category/genre"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Author(models.Model):
    """Book author"""
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_alive(self):
        """Check if author is alive"""
        return self.death_date is None

class AuthorProfile(models.Model):
    """Extended information about author (One-to-One relationship)"""
    author = models.OneToOneField(
        Author, 
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile'
    )
    biography = models.TextField(blank=True)
    website = models.URLField(blank=True)
    photo = models.ImageField(upload_to='authors/', blank=True)
    
    def __str__(self):
        return f"Profile for {self.author.name}"

class Publisher(models.Model):
    """Book publisher"""
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    website = models.TextField(blank=True)

    def __str__(self):
        return self.name