from django.shortcuts import render

# Create your views here.
def chat_view(request):
    # return render(request, 'rt_chat/chat.html')
    return render(request, 'chat.html')