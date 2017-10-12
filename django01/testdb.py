from django.http import HttpResponse

from TestModel.models import Test

def testdb(requset):
    test1 = Test(name="djangmodel")
    test1.save()
    return HttpResponse("<p> update successfully</p>")