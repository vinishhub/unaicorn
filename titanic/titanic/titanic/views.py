from django.shortcuts import render

from. import fake_model
def Home(request):
    return render(request,'index.html')



def result(request):
    user_inp_age=int(request.GET["age"])
    prediction=fake_model.fake_predict(user_inp_age)
    return render(request,'result.html',{'prediction':prediction})

