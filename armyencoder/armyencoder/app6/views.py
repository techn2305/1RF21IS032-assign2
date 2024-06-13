
from django.shortcuts import render
from .forms import MessageForm
from .utils import encode_message

def home(request):
    encoded_message = None
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            encoded_message = encode_message(message)
    else:
        form = MessageForm()
    
    return render(request, 'app6/index.html', {'form': form, 'encoded_message': encoded_message})

# Create your views here.
