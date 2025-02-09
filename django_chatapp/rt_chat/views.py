from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rt_chat.models import ChatGroup

# Create your views here.

@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="public-chat")
    chat_messages = chat_group.chat_message.all()[:30]
    return render(request, 'rt_chat/chat.html', {'chat_messages': chat_messages})
