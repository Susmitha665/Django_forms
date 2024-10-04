from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import RegisterForm,ContactForm



from django.contrib.auth.decorators import login_required
@login_required
def contact_view(request):
  
  if request.method == 'POST':
      
      form = ContactForm(request.POSt)
      if form.is_valid():
         #process the data
         name = form.cleaned_data['name']
         email = form.cleaned_data['email']
         message = form.cleaned_dat['message']
         return render(request,'thanks.html',{'name':name})
  else:
     form = ContactForm()
  return render(request,'contact.html',{'form':form})
def register_view(request):

   if request.method =='POST':
     
     form =RegisterForm(request.POST)
     if form.is_valid():
        user=form.save
        login(request,user)
        return redirect('contact')
   else:

      form=RegisterForm()
   return render(request,'register.html',{'form': form})
      





