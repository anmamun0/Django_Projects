from django.shortcuts import render

# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        return render(request,'contact.html',{'name':name,'email':email})
    else:
        return render(request,'contact.html')

def submit_form(request):
    # if request.method == "POST":
    #     name = request.POST.get("username")
    #     email = request.POST.get("email")
    #     return render(request,'form.html',{'name':name,'email':email})
    # else:
    # print(request.POST)
    return render(request,'form.html')