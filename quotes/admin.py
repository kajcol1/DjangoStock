from django.contrib import admin


# importujemy i rejestrujemy klase bazy danych na podstronie admin, ktora stworzylismy w pliku models.py
# models to baza danych w Django
from .models import Stock

admin.site.register(Stock)
