from .models import Tests, CompanyDetail

def basetest1(request):

    hello = Tests.objects.all()

    return {
        'testname': hello,

    }


def basetest2(request):

    labs = CompanyDetail.objects.all()
    return {
        'labsname': labs
    }