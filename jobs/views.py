from django.shortcuts import render, get_object_or_404
# the get_object_or_404 library returns a single object if exists or a 404 if not found
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects   # This is the django framework accessing the database
    context = {
        'jobs': jobs
    }

    return render(request, 'jobs/home.html', context)

    # add a dictionary parameter
    # return render(request, 'jobs/home.html', {'jobs': jobs})  

def detail(request, job_id): # when detail is invoked, the job_id is passed in
    # print(job_id)
    # the job_detail is working with a Job class and contains a Job object that has an image and summary
    # every model in the database has a primary key, a unique id
    # want to pass this job_detail to browser.  Need to add another template named detail.html
    job_detail = get_object_or_404(Job, pk=job_id)
    context = {
        'job': job_detail
    }

    return render(request, 'jobs/detail.html', context)