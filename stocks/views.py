import requests
from django.shortcuts import render, redirect
from .models import Watchlist


def dashboard(request):
    watchlist = Watchlist.objects.filter(user=request.user)
    stock_data = []
    for item in watchlist:
        symbol = 'ibm'
        response = requests.get(
            f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey=ZAUT54ES3OC2UN27"
        )
        if response.status_code == 200:
            data = response.json()
            latest_data = list(data["Time Series (5min)"].values())[0]
            latest_price = latest_data["4. close"]
            stock_data.append({"symbol": symbol, "latest_price": latest_price})
    context = {"stock_data": stock_data}
    return render(request, "dashboard.html", context)


def add_to_watchlist(request):
    if request.method == "POST":
        symbol = request.POST.get("symbol")
        Watchlist.objects.create(user=request.user, symbol=symbol)
        return redirect("dashboard")


def remove_from_watchlist(request, watchlist_id):
    watchlist = Watchlist.objects.get(id=watchlist_id)
    watchlist.delete()
    return redirect("dashboard")
