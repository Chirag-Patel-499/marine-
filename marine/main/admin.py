from django.contrib import admin
from .models import (
    HeroContent, HeroSlide, Service, FleetItem, Project,
    ContactInfo, ContactMessage, TeamMember, Testimonial,
    HomeTwoHero, HomeThreeHero
)


# ==========================
# Homepage 1 Hero
# ==========================
@admin.register(HeroContent)
class HeroContentAdmin(admin.ModelAdmin):
    list_display = ('title',)


# ==========================
# Homepage 1 Slider
# ==========================
@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('order', 'video')
    ordering = ('order',)


# ==========================
# Homepage 2 Hero (NEW)
# ==========================
@admin.register(HomeTwoHero)
class HomeTwoHeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_status')

    def video_status(self, obj):
        return obj.video.url if obj.video else "No Video"
    video_status.short_description = "Hero Video"



@admin.register(HomeThreeHero)
class HomeThreeHeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_status')

    def video_status(self, obj):
        return obj.video.url if obj.video else "No Video"
    video_status.short_description = "Hero Video"


# ==========================
# Services
# ==========================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(FleetItem)
class FleetItemAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)


# ==========================
# Contact Info
# ==========================
@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'email')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')


# ==========================
# Team Members
# ==========================
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')


# ==========================
# Testimonials
# ==========================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name',)
