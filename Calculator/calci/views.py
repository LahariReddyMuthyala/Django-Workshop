from django.shortcuts import render

def calc(requests):
    field1=requests.GET['field1']
    field2=requests.GET['field2']
    opt=requests.GET['optradio']
    result=0
    if opt =='+':
        result = int(field1) + int(field2)
    if opt =='-':
        result = int(field1) - int(field2)
    if opt == '*':
        result = int(field1) * int(field2)
    if opt =='/':
        result = int(field1) / int(field2)
    return render(requests, 'calci/calc.html',{'result':result, 'field1':field1, 'field2':field2, 'opt':opt})
def home(requests):
    return render(requests, 'calci/home.html')
