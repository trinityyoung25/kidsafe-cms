from django.shortcuts import render, redirect
from .models import Content, ChildProfile, ActivityLog

def dashboard(request):
    content = Content.objects.all()
    return render(request, "dashboard.html", {"content": content})


def upload_content(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        url = request.POST.get("url")

        Content.objects.create(
            title=title,
            description=description,
            url=url,
            approved=False
        )

        return redirect("dashboard")

    return render(request, "upload_content.html")


def child_library(request):
    approved_content = Content.objects.filter(approved=True)
    return render(request, "child_library.html", {"content": approved_content})
