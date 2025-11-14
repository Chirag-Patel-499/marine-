
from django.shortcuts import render
from .models import HeroContent, HeroSlide, Service, FleetItem, Project, ContactInfo, ContactMessage, TeamMember, Testimonial




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
            'success': True,     # For showing popup/toast
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


