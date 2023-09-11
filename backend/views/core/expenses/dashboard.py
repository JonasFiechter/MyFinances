from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, HttpResponseForbidden, \
    HttpResponseServerError
from django.shortcuts import render, redirect


@login_required
def expenses_dashboard(request: HttpRequest):
    return render(request, 'core/pages/invoices/dashboard/dashboard.html', {})