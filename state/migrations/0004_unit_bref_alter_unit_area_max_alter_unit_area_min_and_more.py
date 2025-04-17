# Generated by Django 5.2 on 2025-04-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0003_alter_project_down_payment_percent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='bref',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='area_max',
            field=models.FloatField(blank=True, help_text='Maximum area in m²', null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='area_min',
            field=models.FloatField(blank=True, help_text='Minimum area in m²', null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='type',
            field=models.CharField(choices=[('apartment', 'Apartment'), ('duplex', 'Duplex'), ('townhouse', 'Town House'), ('standalone', 'Stand Alone Villa'), ('penthouse', 'Penthouse'), ('twinhouse', 'Twin House'), ('loft', 'Loft'), ('studio', 'Studio'), ('chalet', 'Chalet'), ('serviced', 'Serviced Apartment'), ('commercial', 'Commercial Unit'), ('land', 'Land')], max_length=20),
        ),
    ]
