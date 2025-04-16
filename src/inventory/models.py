from django.db import models
from library.models import Book  # Importa tu modelo de libro

class BookCopy(models.Model):
    CONDITION_CHOICES = [
        ('new', 'Nuevo'),
        ('good', 'Bueno'),
        ('fair', 'Regular'),
        ('poor', 'Malo'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    inventory_number = models.CharField(max_length=50, unique=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    location = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    acquisition_date = models.DateField()

    def _str_(self):
        return f"{self.inventory_number} ({self.book.title})"
    
class Acquisition(models.Model):
    book_copy = models.OneToOneField(BookCopy, on_delete=models.CASCADE)
    supplier = models.CharField(max_length=255)
    acquisition_date = models.DateField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    def _str_(self):
        return f"Adquisición de {self.book_copy}"