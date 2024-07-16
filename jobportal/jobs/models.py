from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    job_id = models.CharField(max_length=100, unique=True)
    photo_url = models.URLField()
    description = models.TextField()
    job_type = models.CharField(max_length=50)

    # Company info
    company_name = models.CharField(max_length=255)
    company_id = models.CharField(max_length=100)
    company_full_address = models.TextField()
    company_facebook_url = models.URLField()
    company_data_policy_url = models.URLField()
    company_url = models.URLField()
    company_page_matching_approach = models.CharField(max_length=50)

    # Location
    full_address = models.TextField()
    country = models.CharField(max_length=50)

    # Salary
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    salary_currency = models.CharField(max_length=3)
    salary_type = models.CharField(max_length=50)

    # Integration configuration
    facebook_apply_data_callback_url = models.URLField()
    facebook_apply_data_custom_questions_url = models.URLField()
    facebook_apply_data_email_field_optional = models.BooleanField()
    facebook_apply_data_phone_number_field_optional = models.BooleanField()
    facebook_apply_data_work_experience_field_optional = models.BooleanField()

def __str__(self):
    return self.title
