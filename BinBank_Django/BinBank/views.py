from BinBank.models import Parent,Child,Place,Expense,Income
from django.http import JsonResponse


def signin(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        eror=False
        child=None
        parent=None
        try:
            child=Child.get(email=email,password=password)
            parent=Parent.get(id=child.parerent_ID)
        except Exception:
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0, "data": {
                                                        "parent":{
                                                                    "parent_id":parent.id,
                                                                    "first_name":parent.first_name,
                                                                    "last_name":parent.last_name,
                                                                    "phone":parent.phone,
                                                                    "email":parent.email,
                                                                    "balance":parent.balance,
                                                                    "password":parent.password,
                                                                },
                                                    "child":{
                                                        "child_id":child.id,
                                                        "first_name":child.first_name,
                                                        "last_name":child.last_name,
                                                        "phone":child.phone,
                                                        "email":child.email,
                                                        "balance":child.balance,
                                                        "parerent_id":child.parerent_ID,
                                                        "password":child.password,
                                                        "online_cashing_bit":child.online_cashing_bit,
                                                        "max_per_day":child.max_per_day,
                                                        "max_payment":child.max_payment,
                                                        "low_balance":child.low_balance,
                                                        "max_cashing":child.max_cashing,
                                                    }

                                                }})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def request_balance(request):
    try:
        child_ID = request.POST['child_id']
        balance = request.POST['balance']

        try:
            child = Child.get(id=child_ID)
            parent = Parent.get(id=child.parerent_ID)
            child.balance+=int(balance)
            parent.balance-=int(balance)
            child.save()
            parent.save()
            Income.objects.create(type=1,sum=balance,child_ID=child_ID,parent_ID=parent.id)
        except Exception:
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0, "data": child.balance})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def get_expense(request):
    try:
        child_ID = request.POST['child_id']
        try:
            expenses=Expense.objects.filter(child_ID=child_ID)
            print(expenses)
            data = list(expenses)
        except Exception:
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0, "data": data})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def get_income(request):
    try:
        child_ID = request.POST['child_id']
        try:
            incomes=Income.objects.filter(child_ID=child_ID)
            print(incomes)
            data = list(incomes)
        except Exception:
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0, "data": data})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})



def sos(request):
    try:
        child_ID = request.POST['child_id']
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        try:
            child = Child.get(id=child_ID)
            parent = Parent.get(id=child.parerent_ID)
            print('sending sos')

        except Exception:
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def operation(child,sum,cashing):
    ask_parent=False
    if(child.balance-sum<child.low_balance):ask_parent=True
    if(sum>child.max_payment):ask_parent=True
    if(cashing and sum>child.max_cashing): ask_parent=True
    Expense.objects.create(type=1,sum=sum,child_ID=child.id)

def online_payment(request):
    try:
        child_ID = request.POST['child_id']
        balance = request.POST['balance']
        try:
            child = Child.get(id=child_ID)
            parent = Parent.get(id=child.parerent_ID)
            if(child.online_cashing_bit==1):
                operation(child,balance,False)
            else:
                return JsonResponse({"code": 1})




        except Exception:
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


def payment(request):
    try:
        child_ID = request.POST['child_id']
        balance = request.POST['balance']
        try:
            child = Child.get(id=child_ID)
            operation(child, balance, False)
        except Exception:
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})

def cashing(request):
    try:
        child_ID = request.POST['child_id']
        balance = request.POST['balance']
        try:
            child = Child.get(id=child_ID)
            operation(child, balance, True)
        except Exception:
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0})
    except Exception as e:
        print(e)
        return JsonResponse({"code": 1})


