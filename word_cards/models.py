from django.db import models
from django.utils.translation import gettext_lazy as _


class WordCard(models.Model):
    front: str = models.CharField(max_length=255, unique=True)
    back: str = models.CharField(max_length=255, blank=True)
    description: str = models.TextField(blank=True)


class UsageExample(models.Model):
    word_card: WordCard = models.ForeignKey(WordCard, on_delete=models.CASCADE)
    front: str = models.CharField(max_length=1024)
    back: str = models.CharField(max_length=1024, default=_("Empty"), blank=True)
