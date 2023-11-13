from django.urls import path, reverse_lazy
from django.shortcuts import render, redirect

from .forms import FormTask
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

class lsView1(ListView):
    model = Task
    template_name = 'todo.html'
    context_object_name = 'todo_list'


class dtView1(DetailView):
    model = Task
    template_name = 'tododet2.html'
    context_object_name = 'todo_itm'


class updat1(UpdateView):
    model = Task
    template_name = 'todoupdat.html'
    context_object_name = 'todo_itm'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:dtView1', kwargs={'pk': self.object.id})


class clsDel1(DeleteView):
    model = Task
    template_name = 'tododel.html'
    success_url = reverse_lazy('todoapp:lsView1')


def fun_todo(request):
    return render(request, 'todo.html')


def fun_add1(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        prior1 = request.POST.get('priority', '')
        date1 = request.POST.get('date', '')
        objMain = Task(name=name, priority=prior1, date=date1)
        objMain.save()

    mov1 = Task.objects.all()
    return render(request, 'todo.html', {'todo_list': mov1})


def fun_det3(request):
    tsk1 = Task.objects.all()
    return render(request, 'tododet.html', {'todo_list': tsk1})


def fun_del(request, taskID):
    tsk = Task.objects.get(id=taskID)
    if request.method == 'POST':
        tsk.delete()
        return redirect('todoapp:show1')

    return render(request, 'tododel.html')


def fun_edit(request, taskID):
    tsk = Task.objects.get(id=taskID)
    form = FormTask(request.POST or None, instance=tsk)
    if form.is_valid():
        form.save()
        return redirect('todoapp:show1')
    return render(request, 'todoedit.html', {'form1': form, 'task': tsk})
