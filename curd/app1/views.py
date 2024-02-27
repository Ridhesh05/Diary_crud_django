from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from django.contrib import messages

# Create your views here.
def home(request):
    # when we want data to send to backend 
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        city = request.POST['city']
        contact = request.POST['contact']
        obj = Student(name=name, email=email, city=city, contact=contact)
        obj.save()
        return redirect('records')
    else:
        pass
    return render(request,'app1/home.html')

def records(request):
    # Get all the records in the database
    records = Student.objects.all()
    
    # Create a context dictionary
    context = {"records": records}
    
    # Pass the context dictionary as the third argument to the render() function
    return render(request, 'app1/records.html', context)
def delete(request, id):
    if request.method == "POST":
        # Retrieve the student object or return a 404 response if not found
        obj = get_object_or_404(Student, id=id)
        
        try:
            # Delete the object
            obj.delete()
            messages.success(request, 'Student deleted successfully.')
        except Exception as e:
            messages.error(request, 'An error occurred while deleting the student.')

        # Redirect to a different URL after deletion
        return redirect('records')  # Assuming 'records' is the name of the view for displaying records

    return render(request, 'app1/records.html')

def edit(request, id):
    # Retrieve the student object or return a 404 response if not found
    data = get_object_or_404(Student, id=id)
    context ={
        'data':data
    }
    return render(request, 'app1/edit.html',context)
def update(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        city = request.POST['city']
        updated_record=Student(id=id,name=name,email=email,contact=contact,city=city)
        updated_record.save()
        return redirect('records')
    else:
        pass
    return render(request,'edit.html')