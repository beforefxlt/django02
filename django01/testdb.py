from django.http import HttpResponse

from TestModel.models import Test


def testdb(requset):
    test1 = Test(name="djangmodel")
    test1.save()
    return HttpResponse("<p> update successfully</p>")

def dbQuery(request):
    list = Test.objects.all()
    response = Test.objects.filter(id=1)
    response2 = Test.objects.get(id=1)
    for var in list:
        response = var.name + " "
    return HttpResponse("<p>"+ response + "</p>")

def dbadd(request):
    newName = ""
    checkNameF= ""
    newName = str(2)
    test = Test(name=newName,id=1)
    test.save()
    checkName = Test.objects.filter(id=2)
    for i in checkName:
        checkNameF += i.name
    return HttpResponse("add successfully" + checkNameF + "  " +"\n")

def deldb(request):
    delModel= Test.objects.get(id=1)
    delModel.delete()
    return HttpResponse("<p>delete successfully.</p>")