from django.shortcuts import render
from .models import question
from .forms import questionForm
# Create your views here.

def askquestion(request):
    if request.method == 'POST':
        form=questionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=questionForm()

    context={
        'form':form
    }
    return render(request, 'ques/main.html', context)