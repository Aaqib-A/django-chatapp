from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rt_chat.models import ChatGroup
from rt_chat.forms import ChatMessageCreateForm

# Create your views here.

@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="public-chat")
    chat_messages = chat_group.chat_message.all()[:30]
    form = ChatMessageCreateForm()
    print(form)

    # if request.request == "POST":
    if request.htmx:
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            # return redirect('home')

            context = {
                'message': message,
                'user': message.author,
            }
            return render (request, 'rt_chat/partials/chat_message_p.html', context)
    return render(request, 'rt_chat/chat.html', {'chat_messages': chat_messages, 'form': form})
