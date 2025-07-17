from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse






@login_required
def download_csv(request):
    csv = request.session.get("cleaned_csv", "")
    filename = request.session.get("filename", "cleaned_data")
    cleaned_filename = f"{filename}.csv"
    response = HttpResponse(csv, content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{cleaned_filename}"'
    return response


