from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm  
from first_app.models import Program, Student
# 'request' name is convention. It can be some other name too.
clicked = 1
def index(request) :
  global clicked
  program_values = Program.objects.all()
  student_values = Student.objects.all()
  clicked += 1
  my_dict = {
     'count' : clicked,
     'program_rows' : program_values,
    'student_rows' : student_values
 }
  return render(request, 'index.html', my_dict)

def help(request) :
    help_dict = { 'help_message' : "This is an injected help content"}
    return render(request, 'help.html', help_dict)
 
def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)     
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_degree = form.cleaned_data['degree']        
        s_branch = form.cleaned_data['branch']
        s_year = form.cleaned_data['year']
        s_dob = form.cleaned_data['dob']
        s_program = Program.objects.get(title=s_degree, branch=s_branch)
        if s_program is None:
            s_program.save()
        else:
            student = Student(name=s_name, roll_number=s_roll, year=s_year, dob=s_dob, program=s_program)
            student.save()
        return HttpResponseRedirect('/student/')
  else: 
      form =StudentForm()
      return render(request, 'forms.html', {'form': form})