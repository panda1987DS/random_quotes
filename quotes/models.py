from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Quote(models.Model):
    text = models.TextField()
    source = models.CharField(max_length=200)
    weight = models.PositiveIntegerField(default=100, validators=[MinValueValidator(1),
                                       MaxValueValidator(100)])
    views = models.PositiveIntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.source}: {self.text[:50]}"
