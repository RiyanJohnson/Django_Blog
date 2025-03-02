from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm

#message.debug
#message.info
#message.success
#message.warning
#message.error
#these are diff types of flashing messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created, you can now login") 
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_reg/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'user_reg/logout.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)  #user update form
 
        if u_form.is_valid(): 
            u_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)    


    context = {
        'u_form' : u_form,
    }
    return render(request, 'user_reg/profile.html',context )
