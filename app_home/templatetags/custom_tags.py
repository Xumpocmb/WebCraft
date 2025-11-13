from django import template
from app_home.models import ContactInfo

register = template.Library()

@register.simple_tag
def get_contact_info():
    return ContactInfo.objects.first()
