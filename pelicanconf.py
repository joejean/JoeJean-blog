#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#General info about the Site
AUTHOR = u'Joe Jean'
SITENAME = u"Joe Jean"
SITEURL = 'http://www.joejean.net'
TIMEZONE = 'Asia/Dubai'
DEFAULT_LANG = u'en'


#Content settings
PATHS = "content"
PAGES_DIR = "pages"
ARTICLES_DIR = "articles"

STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
    'files/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},}


#DEFAULT_DATE_FORMAT = ('%d-%m-%Y')


#Feed Generation Settings
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

#Blogroll Settings
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#         ('Another social link', '#'),)



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/joejean.info-pelican-theme'

# URL settings
ARTICLE_URL = ('articles/{slug}/')
ARTICLE_SAVE_AS = ('articles/{slug}/index.html')
PAGE_URL = ('pages/{slug}/')
PAGE_SAVE_AS = ('pages/{slug}/index.html')
PAGE_LANG_SAVE_AS = False
TAG_URL = ('tag/{slug}/')
TAG_SAVE_AS = ('tag/{slug}/index.html')
TAGS_URL = ('tags/')
TAGS_SAVE_AS = None
CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')
AUTHOR_SAVE_AS = False

#Do not process html input files
READERS = {'html': None}

DEFAULT_DATE = ('fs')

#TagCloud
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_STEPS = 4

DISQUS_SITENAME ="joejeanblog"
GOOGLE_ANALYTICS ="UA-46696882-1"

#PAGINATION
DEFAULT_PAGINATION = 6 #Maximum number of articles on a given page
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

DISPLAY_CATEGORIES_ON_MENU = False

#PLUGINS USED
PLUGIN_PATHS = ["pelican_plugins"]
PLUGINS = ['summary']
