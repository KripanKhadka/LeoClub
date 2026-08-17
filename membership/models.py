from django.db import models


class MembershipApplication(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending Review"),
        ("payment_submitted", "Payment Submitted"),
        ("under_review", "Under Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=30)
    profile_photo = models.ImageField(upload_to="membership/profile/", blank=True, null=True)
    phone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=150, blank=True)
    emergency_contact_number = models.CharField(max_length=30, blank=True)

    institution = models.CharField(max_length=200)
    program = models.CharField(max_length=200, blank=True)
    semester_year = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=150, blank=True)

    reason_to_join = models.TextField()
    previous_experience = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    service_areas = models.TextField(blank=True)
    heard_about_us = models.CharField(max_length=200, blank=True)

    transaction_id = models.CharField(max_length=150)
    payment_receipt = models.FileField(upload_to="membership/payments/")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="pending")

    information_correct = models.BooleanField(default=False)
    agrees_to_rules = models.BooleanField(default=False)
    contact_consent = models.BooleanField(default=False)

    application_number = models.CharField(max_length=30, unique=True, editable=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.application_number} — {self.full_name}"

    def save(self, *args, **kwargs):
        if not self.application_number:
            last = MembershipApplication.objects.order_by("-id").first()
            next_number = (last.id + 1) if last else 1
            self.application_number = f"LCOS-{next_number:04d}"
        super().save(*args, **kwargs)
