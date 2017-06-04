from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Greeting
from .models import ShortUrl, Hit
from .forms import UrlForm


def index(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            url = make_short_url(url)
            return render(request, 'index.html', {'url': url})
    else:
        form = UrlForm(label_suffix='')
    return render(request, 'index.html', {'form': form, 'url': ''})


def redirect(request, key):
    target = get_object_or_404(ShortUrl, key=key)

    try:
        hit = Hit()
        hit.target = target
        hit.referer = request.META.get("HTTP_REFERER", "")
        hit.ip = request.META.get("REMOTE_ADDR", "")
        hit.user_agent = request.META.get("HTTP_USER_AGENT", "")
        hit.save()
    except IntegrityError:
        pass
    return HttpResponseRedirect(target.target)


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, 'db.html', {'greetings': greetings})


def make_short_url(url):
    short_url = ShortUrl.objects.get_or_create(target=url)[0]
    short_url.save()
    return 'https://django-minify-url.herokuapp.com/%s' % short_url.key
