from django.db import models



class Project(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    starting_price = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    down_payment_percent = models.DecimalField(max_digits=15, decimal_places=2,blank=True, null=True)
    installment_years = models.IntegerField(blank=True, null=True)
    whatsapp=models.URLField(max_length=200,blank=True, null=True)
    def __str__(self):
        return self.name


class Unit(models.Model):
    UNIT_TYPES = [
        ('apartment', 'Apartment'),
        ('duplex', 'Duplex'),
        ('townhouse', 'Town House'),
        ('standalone', 'Stand Alone Villa'),
        ('penthouse', 'Penthouse'),
        ('twinhouse', 'Twin House'),
        ('loft', 'Loft'),
        ('studio', 'Studio'),
        ('chalet', 'Chalet'),
        ('serviced', 'Serviced Apartment'),
        ('commercial', 'Commercial Unit'),
        ('land', 'Land'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='units')
    type = models.CharField(max_length=20, choices=UNIT_TYPES)
    bref=models.CharField(max_length=500,blank=True, null=True)
    bedrooms_count = models.IntegerField(blank=True, null=True)
    area_min = models.FloatField(help_text="Minimum area in m²",blank=True, null=True)
    area_max = models.FloatField(help_text="Maximum area in m²",blank=True, null=True)
    is_fully_finished = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    whatsapp=models.URLField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.project.name}"


class ProjectMedia(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='media_project')
    image = models.FileField(upload_to='image/project')

    def __str__(self):
        return f"{self.Project}"


class UnitMedia(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='media_unit')
    image = models.FileField(upload_to='image/unit')

    def __str__(self):
        return f" {self.unit}"


