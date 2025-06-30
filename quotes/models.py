from django.db import models


class Quote(models.Model):
    text = models.TextField()
    source = models.CharField(max_length=200)
    weight = models.PositiveIntegerField(default=1)
    views = models.PositiveIntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            if Quote.objects.filter(source=self.source).count() >= 3:
                raise ValueError(
                    "Нельзя добавить более 3 цитат из одного источника. Сначало удалите одну из старых цитат")
            if Quote.objects.filter(source=self.source, text=self.text).count() > 0:
                raise ValueError(
                    "Такая цитата уже существует")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.source}: {self.text[:50]}"
