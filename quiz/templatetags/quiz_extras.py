
"""Custom template tags for user Groups"""
# Code taken from https://stackoverflow.com/questions/56499036/tag-is-not-a-registered-tag-library-must-be-one-of-in-a-django-app
from django import template


register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()