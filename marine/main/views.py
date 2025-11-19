from django.shortcuts import render
from .models import (
    HeroContent, HeroSlide, Service, FleetItem, Project,
    ContactInfo, ContactMessage, TeamMember, Testimonial,
    HomeTwoHero, HomeThreeHero
)


# ==========================
# HOMEPAGE 1 (SLIDER VERSION)
# ==========================
def home(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),
        )

        return render(request, "index.html", {
            'services': Service.objects.all(),
            'fleet': FleetItem.objects.all(),
            'projects': Project.objects.all(),
            'contact': ContactInfo.objects.first(),
            'success': True,
        })

    ctx = {
        'hero': HeroContent.objects.first(),
        'slides': HeroSlide.objects.all().order_by('order'),

        'services': Service.objects.all(),
        'fleet': FleetItem.objects.all(),
        'projects': Project.objects.all(),
        'contact': ContactInfo.objects.first(),
        'team': TeamMember.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }
    return render(request, "index.html", ctx)



# ==========================
# HOMEPAGE 2 (SINGLE VIDEO)
# ==========================
def home2(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),
        )

        return render(request, "home2.html", {
            'services': Service.objects.all(),
            'fleet': FleetItem.objects.all(),
            'projects': Project.objects.all(),
            'contact': ContactInfo.objects.first(),
            'success': True,
        })

    hero2 = HomeTwoHero.objects.first()

    # Safe video
    video_url = hero2.video.url if (hero2 and hero2.video) else None

    ctx = {
        'hero2': hero2,
        'video2': video_url,

        'services': Service.objects.all(),
        'fleet': FleetItem.objects.all(),
        'projects': Project.objects.all(),
        'contact': ContactInfo.objects.first(),
        'team': TeamMember.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }

    return render(request, "home2.html", ctx)



# ==========================
# HOMEPAGE 3 (PREMIUM HERO)
# ==========================
def home3(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),
        )

        return render(request, "home3.html", {
            'services': Service.objects.all(),
            'fleet': FleetItem.objects.all(),
            'projects': Project.objects.all(),
            'contact': ContactInfo.objects.first(),
            'team': TeamMember.objects.all(),
            'testimonials': Testimonial.objects.all(),
            'success': True,
        })

    hero3 = HomeThreeHero.objects.first()

    # Safe video
    video_url = hero3.video.url if (hero3 and hero3.video) else None

    ctx = {
        'hero3': hero3,
        'video3': video_url,

        'services': Service.objects.all(),
        'fleet': FleetItem.objects.all(),
        'projects': Project.objects.all(),
        'contact': ContactInfo.objects.first(),
        'testimonials': Testimonial.objects.all(),
    }

    return render(request, "home3.html", ctx)
