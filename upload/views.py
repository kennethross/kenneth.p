import csv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from upload.forms import FileForm
from upload.models import insertData
from upload.models import invitation, batchData

from django.core.management.base import BaseCommand

def abcdisplay(request):
    posts = invitation.objects.all()
    print posts
    return render(request, 'upload/index.html', {"posts": posts})
    #return render_to_response('submit/index.html', {"posts": posts})

def dataViewDisplay(request):
    posts = invitation.objects.all()
    return render(request, 'upload/viewdata.html' ,{"posts": posts})

def uploadBatchData(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        #print "trying to upload"
        # create a form instance and populate/insert it with data from the request:
        form = FileForm(request.POST,request.FILES)
        # check whether it's valid:
        
        if form.is_valid():
            #print "valid form"
            
            csv_path = request.FILES['docfile']

            print csv_path.read()

            csv_reader = csv.DictReader(csv_path)

            for row in csv_reader:
                obj = invitation.objects.create(
                           
                    date = row['date'],       
                    name = row['name']
                    )                   
                print obj
            
            #csv_path.save()
            return HttpResponseRedirect('thanks/')
                # if a GET (or any other method) we'll create a blank form
    else:
        print "invalid form"
        form = FileForm()

    #return render(request, 'upload/received.html')
    return render(request, 'upload/name.html', {'form': form})