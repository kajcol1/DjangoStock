from django.shortcuts import render, redirect
# importujemy Stock z models.py, czyli pliku z definicją bazy danych
from .models import Stock
from .forms import StockForm
from django.contrib import messages


def home(request):
	# to dopisujemy do obsługi API
	# pk_cf903dce188d4f09bfee7d1bbcded34c
	#klucz pobrany z https://iexcloud.io/console/home
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_cf903dce188d4f09bfee7d1bbcded34c")

	
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})

	else:
		return render(request, 'home.html', {'ticker': "Enter a ticker symbol Above"})

	
def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def add_stock(request):
	import requests
	import json
	
	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added"))
			return redirect('add_stock')	
	else:
	# dodajemy wszystkie elementy z obiektu Stock
		ticker = Stock.objects.all()
		output = []

		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_cf903dce188d4f09bfee7d1bbcded34c")

	
			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."
		
		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Deleted"))
	return redirect(delete_stock)

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request, 'delete_stock.html', {'ticker':ticker})
		




