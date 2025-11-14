from django.contrib import admin
from .models import HeroContent, HeroSlide, Service, FleetItem, Project, ContactInfo, ContactMessage, TeamMember, Testimonial


# Register your models here.


@admin.register(HeroContent)
class HeroContentAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('order', 'video')
    ordering = ('order',)



@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(FleetItem)
class FleetItemAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)



@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'email')



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')



@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name',)
