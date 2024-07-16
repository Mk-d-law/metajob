# Generated by Django 5.0.2 on 2024-07-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('job_id', models.CharField(max_length=100, unique=True)),
                ('photo_url', models.URLField()),
                ('description', models.TextField()),
                ('job_type', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=255)),
                ('company_id', models.CharField(max_length=100)),
                ('company_full_address', models.TextField()),
                ('company_facebook_url', models.URLField()),
                ('company_data_policy_url', models.URLField()),
                ('company_url', models.URLField()),
                ('company_page_matching_approach', models.CharField(max_length=50)),
                ('full_address', models.TextField()),
                ('country', models.CharField(max_length=50)),
                ('salary_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_max', models.DecimalField(decimal_places=2, max_digits=10)),
                ('salary_currency', models.CharField(max_length=14)),
                ('salary_type', models.CharField(max_length=50)),
                ('facebook_apply_data_callback_url', models.URLField()),
                ('facebook_apply_data_custom_questions_url', models.URLField()),
                ('facebook_apply_data_email_field_optional', models.BooleanField()),
                ('facebook_apply_data_phone_number_field_optional', models.BooleanField()),
                ('facebook_apply_data_work_experience_field_optional', models.BooleanField()),
            ],
        ),
    ]
