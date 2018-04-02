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

from site_pages import views as pages
from user_accounts import views as accounts

urlpatterns = [
	url(r'^admin/', admin.site.urls),  # django admin page
	url(r'^$', pages.get_home_page, name='home'),  # site home page

    # user accounts
	url(r'^account/register/$', accounts.register, name='register'), # user registration
    url(r'^account/login/$', accounts.login, name='login'), # user log in
    url(r'^account/logout/$', accounts.logout, name='logout'), # user log out
    url(r'^account/$', accounts.my_account, name='my_account'), # my account home page

    # ajax calls
    url(r'^ajax/check_email/$', accounts.lookup_email, name='lookup_email') # check email address doesn't exist
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        url(r'^debug/', include(debug_toolbar.urls))
    )
