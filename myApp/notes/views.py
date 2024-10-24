from django.shortcuts import render
from .models import Notes
# Create your views here.

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html',{'notes': all_notes})

def details(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notes/notes_details.html', {'note': note})
    
