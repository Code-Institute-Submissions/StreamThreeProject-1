"""ScrapQuotation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from site_pages import views as pages
from .settings import MEDIA_ROOT, STATIC_ROOT

urlpatterns = [
	url(r'^admin/', admin.site.urls),  # django admin page
	url(r'^$', pages.get_home_page, name='home'),  # site home page
    url(r'^accounts/', include('user_accounts.urls')),  # user account urls.
    url(r'^quote/', include('scrap_quote.urls')),  # quotation urls

    # url to serve media
    url(r'^user_uploads/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]

# if in Debug mode, include the debug toolbar.
if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        url(r'^debug/', include(debug_toolbar.urls))
    )
