import datetime
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib import messages
from accounts.models import Account
from django.contrib.auth.decorators import login_required
from accounts.views import organization
from organizations.helper_admin import *
from roles.models import UserRole
from assets.models import Borrowd_Asset

from workstudy.globalsettings import LOGIN_URL
from organizations.models import Issue, Organization


@login_required(login_url=LOGIN_URL)
def admin_dashboard(request, uuid):
    
    helper = UserAdminDetailsHelper(user=request.user, uuid=uuid)
    context = helper.get_nav_details()
    return render(request, "admin_user/dashboard.html", context=context)