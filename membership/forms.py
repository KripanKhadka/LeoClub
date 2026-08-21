from django import forms
from .models import MembershipApplication


class MembershipApplicationForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = [
            "full_name", "date_of_birth", "gender", "profile_photo", "phone", "email",
            "address", "emergency_contact_name", "emergency_contact_number",
            "institution", "program", "semester_year", "occupation",
            "reason_to_join", "previous_experience", "skills", "interests",
            "service_areas", "heard_about_us", "transaction_id", "payment_receipt",
            "information_correct", "agrees_to_rules", "contact_consent",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "address": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "reason_to_join": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "previous_experience": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "skills": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "interests": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "service_areas": forms.Textarea(attrs={"rows": 3, "class": "form-control"}),
            "heard_about_us": forms.TextInput(attrs={"placeholder": "Facebook, Instagram, friend, event, etc.", "class": "form-control"}),
        }
        labels = {
            "institution": "School / College / University",
            "semester_year": "Current Semester / Year",
            "reason_to_join": "Why do you want to join Leo Club?",
            "previous_experience": "Previous organizational / Leo / Lions experience",
            "service_areas": "Preferred areas of service",
            "transaction_id": "Payment Transaction / Reference ID",
            "payment_receipt": "Payment Receipt / Screenshot",
            "information_correct": "I confirm that the information provided is correct.",
            "agrees_to_rules": "I agree to follow the rules and code of conduct of Leo Club of Kathmandu Samakhusi.",
            "contact_consent": "I give permission for the club to contact me regarding my membership application.",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        required_fields = [
            "full_name", "date_of_birth", "gender", "phone", "email", "address",
            "institution", "reason_to_join", "transaction_id", "payment_receipt",
        ]
        for name in required_fields:
            if name in self.fields:
                self.fields[name].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip().lower()
        query = MembershipApplication.objects.filter(email__iexact=email)
        
        # Exclude current record if editing an existing application
        if self.instance and self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
            
        if query.exists():
            raise forms.ValidationError("An application has already been submitted with this email address.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()
        query = MembershipApplication.objects.filter(phone=phone)
        
        # Exclude current record if editing an existing application
        if self.instance and self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
            
        if query.exists():
            raise forms.ValidationError("An application has already been submitted with this phone number.")
        return phone

    def clean(self):
        cleaned = super().clean()
        for field in ("information_correct", "agrees_to_rules", "contact_consent"):
            if not cleaned.get(field):
                self.add_error(field, "This confirmation is required before submitting.")
        return cleaned