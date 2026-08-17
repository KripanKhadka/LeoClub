# Generated manually for Leo Club membership applications.
from django.db import migrations, models
import django.db.models.deletion
import django.db.models
import datetime


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MembershipApplication",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=150)),
                ("date_of_birth", models.DateField()),
                ("gender", models.CharField(max_length=30)),
                ("profile_photo", models.ImageField(blank=True, null=True, upload_to="membership/profile/")),
                ("phone", models.CharField(max_length=30, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("address", models.TextField()),
                ("emergency_contact_name", models.CharField(blank=True, max_length=150)),
                ("emergency_contact_number", models.CharField(blank=True, max_length=30)),
                ("institution", models.CharField(max_length=200)),
                ("program", models.CharField(blank=True, max_length=200)),
                ("semester_year", models.CharField(blank=True, max_length=100)),
                ("occupation", models.CharField(blank=True, max_length=150)),
                ("reason_to_join", models.TextField()),
                ("previous_experience", models.TextField(blank=True)),
                ("skills", models.TextField(blank=True)),
                ("interests", models.TextField(blank=True)),
                ("service_areas", models.TextField(blank=True)),
                ("heard_about_us", models.CharField(blank=True, max_length=200)),
                ("transaction_id", models.CharField(max_length=150)),
                ("payment_receipt", models.FileField(upload_to="membership/payments/")),
                ("status", models.CharField(choices=[("pending", "Pending Review"), ("payment_submitted", "Payment Submitted"), ("under_review", "Under Review"), ("approved", "Approved"), ("rejected", "Rejected")], default="pending", max_length=30)),
                ("information_correct", models.BooleanField(default=False)),
                ("agrees_to_rules", models.BooleanField(default=False)),
                ("contact_consent", models.BooleanField(default=False)),
                ("application_number", models.CharField(editable=False, max_length=30, unique=True)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-submitted_at"]},
        ),
    ]
