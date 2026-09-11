from django.contrib import messages
from django.shortcuts import redirect, render
from membership.forms import MembershipApplicationForm


def home(request):
    return render(request, "site/leo-club-home.html")


def about(request):
    return render(request, "site/leo-club-about.html")


def events(request):
    return render(request, "site/leo-club-events.html")


def join(request):
    return render(request, "site/leo-club-join.html")

def notices(request):
    return render(request, "site/leo-club-notices.html")

def members(request):
    return render(request, 'site/leo-club-members.html')


def membership_application(request):
    if request.method == "POST":
        form = MembershipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            messages.success(
                request, "Your membership application has been submitted successfully!"
            )
            return render(
                request,
                "site/application-success.html",
                {"application": application},
            )
        else:
            messages.error(
                request,
                "There was an error in your submission. Please check the fields below.",
            )
    else:
        form = MembershipApplicationForm()

    return render(request, "site/membership-application.html", {"form": form})