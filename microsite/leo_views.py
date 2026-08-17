from django.shortcuts import render, redirect
from django.contrib import messages

from membership.forms import MembershipApplicationForm


def home(request):
    return render(request, "site/leo-club-home.html")


def about(request):
    return render(request, "site/leo-club-about.html")


def events(request):
    return render(request, "site/leo-club-events.html")


def join(request):
    return render(request, "site/leo-club-join.html")


def membership_application(request):
    if request.method == "POST":
        form = MembershipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            return render(
                request,
                "site/application-success.html",
                {"application": application},
            )
    else:
        form = MembershipApplicationForm()

    return render(request, "site/membership-application.html", {"form": form})
