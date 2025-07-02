from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Quote(models.Model):
    """
        Represents a quote submitted by users.

        Fields:
            text (TextField): The content of the quote.
            source (CharField): The source of the quote (e.g., author, book). Max length 200 characters.
            weight (PositiveIntegerField): Weight from 1 to 100 used to influence how often the quote is shown randomly.
            views (PositiveIntegerField): Number of times the quote has been viewed.
            likes (IntegerField): Number of likes.
            dislikes (IntegerField): Number of dislikes.
        """

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
