from django.contrib import admin
from .models import Project, Unit, ProjectMedia, UnitMedia

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1

class UnitMediaInline(admin.TabularInline):
    model = UnitMedia
    extra = 1

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'starting_price')
    inlines = [ProjectMediaInline, UnitInline]

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('project', 'type', 'bedrooms_count', 'area_min', 'area_max', 'price')
    inlines = [UnitMediaInline]

admin.site.register(ProjectMedia)
admin.site.register(UnitMedia)


