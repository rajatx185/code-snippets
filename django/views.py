##How to fetch data from a view??
def login_view(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        user_type = login_data.get("user_type")
        print(user_type, username, password)
        return HttpResponse("This is a post request")
    else:
        return render(request, "base.html")