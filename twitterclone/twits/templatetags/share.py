import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.template.defaultfilters import urlencode
from django.template.loader import render_to_string

register = template.Library()

TWITTER_URL = 'http://twitter.com/intent/tweet?text='
FACEBOOK_URL = 'http://www.facebook.com/sharer/sharer.php?u='


@register.simple_tag
def hostpost(host, link):
    linkk = str(link)
    hostt = str(host)
    url = hostt + linkk
    links_twitter = TWITTER_URL + url
    links_facebook = FACEBOOK_URL + url
    cta = {'links_twitter': links_twitter, 'links_facebook':links_facebook}
    return render_to_string("share.html", cta)

@register.filter(name='ttags')
def ttags(text):

    pattern = re.compile(r"(?P<start>.?)@(?P<user>[A-Za-z0-9_]+)(?P<end>.?)")
    link = r'\g<start><a href="/\g<user>"  title="#\g<user> on Twitter">@\g<user></a>\g<end>'
    text = pattern.sub(link, text)


    return mark_safe(text)