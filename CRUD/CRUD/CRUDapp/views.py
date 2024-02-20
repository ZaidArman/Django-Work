# importing
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student_Entry
from .forms import StudentEntryForm
from django.db.models import Q
from django.views import View # functional based views
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView # generic class based view
from django.urls import reverse, reverse_lazy 


# home() functional based view
"""
def home(request):
    return render(request, 'index.html')
"""
# home() class based normal view
"""
class home(View):
    def get(self, request):
        return render(request, 'index.html')
"""
# home() class based generic views
class home(CreateView):
    template_name = 'index.html' # TemplateResponseMixin
    # context_object_name = 'data' # Context Mixin 
    form_class = StudentEntryForm

    def get_success_url(self):
        return reverse("show")

# show() funtional based views
"""
def show(request):    
    query = request.GET.get('search')
    if query:
        data = Student_Entry.objects.filter(
            Q(roll_no__icontains=query) | Q(fname__icontains=query) | Q(lname__icontains=query) |
            Q(s_class__icontains=query) | Q(subject__icontains=query) | Q(marks__icontains=query)
        ).order_by('roll_no')
    else:
        data = Student_Entry.objects.all()
    return render(request, 'show.html', {'data': data, 'query': query})
"""
# show() class based view
"""
class show(View):
    def get(self, request):
        query = request.GET.get('search')
        if query:
            data = Student_Entry.objects.filter(
                Q(roll_no__icontains=query) | Q(fname__icontains=query) | Q(lname__icontains=query) |
                Q(s_class__icontains=query) | Q(subject__icontains=query) | Q(marks__icontains=query)
            ).order_by('roll_no')
        else:
            data = Student_Entry.objects.all()
        return render(request, 'show.html', {'data': data, 'query': query})
"""
# show() Generic Class Based View
class show(ListView):
    model = Student_Entry
    template_name = 'show.html'
    
    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Student_Entry.objects.filter(
                Q(roll_no__icontains=query) | Q(fname__icontains=query) | Q(lname__icontains=query) |
                Q(s_class__icontains=query) | Q(subject__icontains=query) | Q(marks__icontains=query)
            ).order_by('roll_no')
        else:
            return Student_Entry.objects.all()

# send() functional based view
"""
def send(request):
    if request.method == 'POST':
        form = StudentEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = StudentEntryForm()
    return render(request, 'index.html', {'form': form})
"""
# send() class based view
"""
class send(View):
    def post(self, request):
        form = StudentEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
        else:
            form = StudentEntryForm()
        return render(request, 'index.html', {'form': form})
"""
# send() Generic Class Based View
class send(CreateView):
    model = Student_Entry
    template_name = 'index.html'
    success_url = '/show/'  # Redirect to this URL upon successful form submission 
    form_class = StudentEntryForm
    
# edit() functional based view
"""
# def edit(request, id):
#     student_entry = get_object_or_404(Student_Entry, id=id)
#     if request.method == 'POST':
#         form = StudentEntryForm(request.POST, instance=student_entry)
#         if form.is_valid():
#             form.save()
#             return redirect('show')
#     else:
#         form = StudentEntryForm(instance=student_entry)
#     return render(request, 'edit.html', {'form': form, 'student_entry': Student_Entry}) 
"""

# edit() class based view
"""
class edit(View):
    
    def get_object(self):
        return get_object_or_404(Student_Entry, id=self.kwargs.get("pk"))
    
    def get(self, request, *args, **kwargs):
        form = StudentEntryForm(instance=self.get_object())
        return render(request, 'edit.html', {'form': form, 'student_entry': Student_Entry})
        
    def post(self, request, *args,**kwargs):
        form = StudentEntryForm(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect('show')
        else:
            form = StudentEntryForm(instance=self.get_object())
        return render(request, 'edit.html', {'form': form, 'student_entry': Student_Entry})
"""
# edit() Generic Class Based View
class edit(UpdateView):
    model = Student_Entry
    form_class = StudentEntryForm
    template_name = 'edit.html'
    success_url = '/show/'  # Redirect to this URL upon successful form submission

# delete() functional based view
"""
def delete(request, pk):
    student_entry = get_object_or_404(Student_Entry, id=pk)
    student_entry.delete()
    return redirect('show')
"""
# delete() class based view
"""
class delete(View):
    def get(self, request, *args, **kwargs):
        student_entry = get_object_or_404(Student_Entry, id=self.kwargs.get("pk"))
        student_entry.delete()
        return redirect('show')
"""

# delete() Generic class Based View
class delete(DeleteView):
    model = Student_Entry
    template_name = 'delete.html'  # Replace with the actual template name
    success_url = reverse_lazy('show')  # Replace with the desired success URL