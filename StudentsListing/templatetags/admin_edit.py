from django import template
from django.core import urlresolvers

register = template.Library()

@register.simple_tag
def get_admin_url(self):
    return urlresolvers.reverse("admin:%s_%s_change" %
        (self._meta.app_label, self._meta.module_name), args=(self.id,))