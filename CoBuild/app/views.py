from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Project, Task, Chat
from . forms import CreateSpace
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.

def CredLogin(request):
    creds = 'credlogin'
    if request.user.is_authenticated:
        return redirect('module')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User does not exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('module')
        else:
            messages.error(request,'User Credentials does not exist')
            
    content = {'creds' : creds}       
    return render(request, 'docs/logs.html', content)
    
def CredLogout(request):
    logout(request)
    return redirect('module')
    
def CredNewUser(request):
    userform = UserCreationForm()
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            user = userform.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("module")
        else:
            messages.error(request, 'Cannot create User, Error Occured during Registration')
            return redirect('module')
    content = {'userform' : userform}
    return render(request , 'docs/logs.html', content)

def module(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    projects = Project.objects.filter(
                                    Q(task__name__icontains = q)|
                                    Q(name__icontains = q)|
                                    Q(description__icontains = q))
    
    tasks = Task.objects.all()
    
    project_count = projects.count()
    
    activities = Chat.objects.all().filter(project__task__name__icontains = q).order_by('-created')
    
    content = {'projects' : projects , 'tasks':tasks, "project_count" : project_count, 'activities': activities}
    return render(request, 'docs/module.html', content)

def project(request, pk):
    project = Project.objects.get(id = pk)
    chats = project.chat_set.all()
    followers = project.followers.all()
    
    student_count = chats.count()
    
    if request.method == 'POST':
        chat = Chat.objects.create(
            user = request.user,
            project=project,
            body=request.POST.get('body')
        )
        project.followers.add(request.user)
        return redirect('project', pk = project.id)
    
    content = {'project' : project, 'chats' : chats, 'followers' : followers, 'student_count' : student_count}
    return render(request, 'docs/project.html', content)

def UserAccount(request, pk):
    profile = User.objects.get(id = pk)
    projects = profile.project_set.all()
    activities = profile.chat_set.all()
    tasks = Task.objects.all()
    content = {"profile" : profile, 'activities' : activities, 'projects' : projects, 'tasks' : tasks}
    return render(request, 'docs/user_account.html', content)

@login_required(login_url = 'credlogin')
def Create(request):
    space = CreateSpace()
    
    if request.method == 'POST':
        space = CreateSpace(request.POST)
        if space.is_valid():
            project = space.save(commit = False)
            project.admin = request.user
            project.save()
            return redirect('module')
    
    content = {'space' : space}
    return render(request, 'docs/crude.html', content)

@login_required(login_url = 'credlogin')
def Update(request, pk):
    project = Project.objects.get(id = pk)
    space = CreateSpace(instance=project)
    
    if request.user != project.admin:
        return HttpResponse('You can\'t Update a Space!!')
    
    if request.method == 'POST':
        space  = CreateSpace(request.POST, instance=project)
        if space.is_valid():
            space.save()
            return redirect('module')
    
    content = {'space' : space}
    return render(request,'docs/crude.html', content)

@login_required(login_url = 'credlogin')
def Delete(request, pk):
    project = Project.objects.get(id = pk)
    
    if request.user != project.admin:
        return HttpResponse('You can\'t Delete a Space!!')
    
    if request.method == 'POST':
        project.delete()
        return redirect('module')
    
    return render(request, 'docs/clear.html' , {'area':project})

@login_required(login_url = 'credlogin')
def ClearChat(request, pk):
    chat = Chat.objects.get(id = pk)
    
    if request.user != chat.user:
        return HttpResponse('You can\'t Delete a Chat!!')
    
    if request.method == 'POST':
        chat.delete()
        return redirect('module')
    return render(request, 'docs/clear.html' , {'area':chat})