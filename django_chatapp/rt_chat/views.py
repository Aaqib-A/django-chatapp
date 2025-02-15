from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from rt_chat.models import ChatGroup
from rt_chat.forms import ChatMessageCreateForm
from users.models import User


# Create your views here.

@login_required
def chat_view(request, chatroom_name='public-chat'):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_message.all()[:30]
    form = ChatMessageCreateForm()

    other_user = None
    if chat_group.is_private:
        if request.user not in chat_group.members.all():
            raise Http404()
        for member in chat_group.members.all():
            if member != request.user:
                other_user = member
                break

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
        
    context = {
        'chat_messages': chat_messages, 
        'form': form,
        'other_user': other_user,
        'chatroom_name': chatroom_name,
    }
    return render(request, 'rt_chat/chat.html', context)

@login_required
def get_or_create_chatroom(request, username):
    if request.user.username == username:
        return redirect('home')
    
    other_user = User.objects.get(username = username)
    my_private_chatrooms = request.user.chat_groups.filter(is_private=True)
    
    if my_private_chatrooms.exists():
        for chatroom in my_private_chatrooms:
            if other_user in chatroom.members.all():
                return redirect('chatroom', chatroom.group_name)
   
    chatroom = ChatGroup.objects.create( is_private = True )
    chatroom.members.add(other_user, request.user)   
    return redirect('chatroom', chatroom.group_name)
