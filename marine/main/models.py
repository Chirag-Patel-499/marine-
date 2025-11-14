from django.db import models


class HeroContent(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.TextField()
    card_title = models.CharField(max_length=200)
    card_text = models.CharField(max_length=300)

    def __str__(self):
        return "Hero Content"


class HeroSlide(models.Model):
    video = models.FileField(upload_to='hero_videos/')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Slide {self.order}"




class Service(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()

    def __str__(self):
        return self.title


class FleetItem(models.Model):   # ← missing hato
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    title = models.CharField(max_length=200, default="Get in touch")
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    office_hours = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    feedback = models.TextField()
    client_name = models.CharField(max_length=200)

    def __str__(self):
        return self.client_name
