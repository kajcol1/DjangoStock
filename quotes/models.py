from django.db import models

# definicja bazy danych i pola o długosci 10 znakow
class Stock(models.Model):
	ticker = models.CharField(max_length=10)

	def __str__(self):
		return self.ticker