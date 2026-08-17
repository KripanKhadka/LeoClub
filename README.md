# Leo Club of Kathmandu Samakhusi Website

A Django-powered website for **Leo Club of Kathmandu Samakhusi, District 325 I, Nepal**.

## Features

- Modern Leo Club homepage
- Cinematic hero slider with loading animation
- About, Events, and Get Involved pages
- Leo Club branding and Nepal-focused content
- Responsive design for desktop and mobile
- Local SVG artwork for the hero section
- Static-site friendly structure with no third-party business branding

## Run locally

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Project structure

- `templates/site/` — Leo Club pages
- `static/site/css/` — Leo Club styling
- `static/site/js/` — hero slider
- `static/site/images/` — Leo Club logo and hero artwork
- `microsite/` — minimal Django configuration and Leo views

## Club identity

**Leo Club of Kathmandu Samakhusi**  
**District 325 I, Nepal**


## Membership Registration

The Get Involved page's **Apply Now** button opens the Leo Club membership application.

First-time setup:
```text
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Applications are available at `/admin/` after creating the admin account.

Replace `static/site/images/payment-qr.svg` with the club's official payment QR image. If you use a PNG, name it `payment-qr.png` and update the image path in `templates/site/membership-application.html`.

Applications are limited to one per email address and one per phone number.
