from django.shortcuts import render,HttpResponseRedirect
from .models import Student
from .forms import StudentRegister

# Create your views here.



##studentsInfo
def add_student(request):
    studinfo=Student.objects.all()
    #select * 
    if request.method=='POST':
        fm=StudentRegister(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=StudentRegister()
    return render(request,'enroll/addstudent.html',{'form':fm,'students':studinfo})

##Delete student info
def delete_info(request,id):
    if request.method=='POST':
        get_stu_data=Student.objects.get(pk=id)
        print(get_stu_data)
        get_stu_data.delete()
        return HttpResponseRedirect('/students/sadd')

#Update
def update_info(request,id):
    if request.method=='POST':
        get_det_of_id=Student.objects.get(pk=id)
        fm=StudentRegister(request.POST,instance=get_det_of_id)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/students/sadd')
    else:
        get_det_of_id=Student.objects.get(pk=id)
        fm=StudentRegister(instance=get_det_of_id)
        return render(request,'enroll/updateInfo.html',{'form':fm})