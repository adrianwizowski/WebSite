from django.utils import timezone
from .models import Post
from .forms import DonationForm
from django.shortcuts import render
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
        "amount": "1.00",
        "item_name": "Donation",
        "currency_code": "EUR",
        "notify_url": 'http://{}{}'.format(host, reverse('paypal-ipn')),
        "return_url": 'http://{}{}'.format(host, reverse('base:done')),
        "cancel_return": 'http://{}{}'.format(host, reverse('base:canceled')),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, 'base/process.html', context)

def donation(request):
    form = DonationForm()
    return render(request, 'base/donation.html', {'form': form})