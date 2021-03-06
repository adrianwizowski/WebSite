from django.utils import timezone
from .models import Post
from .forms import DonationForm
from django.shortcuts import render, redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt




# rendering english version
def base(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'base/base.html', {'posts': posts})

# rendering polish version
def base_pl(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'base/base_pl.html', {'posts': posts})


@csrf_exempt
def money_done(request):
    return render(request, 'base/done.html')

@csrf_exempt
def money_process(request):
    return render(request, 'base/process.html')

@csrf_exempt
def money_canceled(request):
    return render(request, 'base/canceled.html')

def paypal(request):
    host = request.get_host()

    paypal_dict = {
        "business": settings.PAYPAL_RECIEVER_EMAIL,
        "item_name": "Donation",
        "notify_url": 'http://{}{}'.format(host, reverse('paypal-ipn')),
        "return_url": 'http://{}{}'.format(host, reverse('done')),
        "cancel_return": 'http://{}{}'.format(host, reverse('canceled')),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, 'base/process.html', context)


def donation(request):
    form = DonationForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        return redirect('/process')
    return render(request, 'base/donation.html', {'form': form})


def feedback(request):
    return render(request, 'base/feedback.html')

from django.db import connection

def air(request):
    with connection.cursor() as cursor:
        sql_query_korzeniowskiego = "SELECT * FROM stacja s JOIN pomiar p ON p.stacja=s.id WHERE s.id = 8128"
        cursor.execute(sql_query_korzeniowskiego)
        response = cursor.fetchall()
        result_korzeniowskiego = {'name': response[0][1], 'update': response[0][2]}
        for row in range(len(response)):
            result_korzeniowskiego[response[row][3]] = response[row][-1]

    with connection.cursor() as cursor:
        sql_query_powstancow = "SELECT * FROM stacja s JOIN pomiar p ON p.stacja=s.id WHERE s.id = 8129"
        cursor.execute(sql_query_powstancow)
        response = cursor.fetchall()
        result_powstancow = {'name': response[0][1], 'update': response[0][2]}
        for row in range(len(response)):
            result_powstancow[response[row][3]] = response[row][-1]

        return render(request, 'base/air.html',context={'result_korzeniowskiego':result_korzeniowskiego, 'result_powstancow': result_powstancow})

