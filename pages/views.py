from django.shortcuts import render
from pages.models import ReceiptInfo
# Create your views here.
def index(request):
   return render(request, 'pages/index.html', {})

def details(request):

   receiptInfo = ReceiptInfo()

   # print(receiptInfo.getModel())

   return render(request, 'pages/detail.html', receiptInfo.get())
