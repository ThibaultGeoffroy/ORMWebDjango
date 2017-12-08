from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from collections import defaultdict
from django.views import generic
from django.utils import timezone
from .models import Company, Employee
from django.db import  models, migrations
from django.db import connection
from django.apps import apps

from django.http import Http404


# Create your views here.
# def detail(request, question_id):
# try:
#    question = Question.objects.get(pk=question_id)
# except Question.DoesNotExist:
#    raise Http404("Question does not exist")

#    question = get_object_or_404(Question, pk=question_id);
#    return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)

#    response = "You're looking at the result of question %s"
#    return render(request, 'polls/results.html', {'question': question})

def generic_list(request, model):
    values = get_list_or_404(model)
    keyset = values.__getitem__(0).get_fields()
    dataset = []
    for value in values:
        data = []
        for key in keyset:
            data.append(value.get_field(key))
        dataset.append(data)
    return render(request, 'polls/generic_list.html', {'keyset': keyset, 'dataset':dataset, 'url_to_go': model.get_url_to_go()})


def generic_detail(request, model, pk):
    line = get_object_or_404(model, pk)
    keyset = line.get_fields()
    key_type_value = []

    for key in keyset:
        t = [key, line.get_type(key), line.get_field(key)]
        key_type_value.append(t)

    return render(request, 'polls/generic_detail.html', {"key_type_value": key_type_value})

def company_detail_view( request, pk):

    company = get_object_or_404(Company, pk=pk )
    return render(request, 'polls/companyDetail.html', {'company': company})


def employee_detail_view(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'polls/employee_detail.html', {'employee': employee})


def company_list_view(request):

    companies = get_list_or_404(Company)
    return render(request, 'polls/company_list.html', {'companies': companies})


def update_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    change = request.POST['name']
    company.name = change
    company.save()

    return HttpResponseRedirect(reverse('polls:companyList'))


def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    for key in request.POST:
        if hasattr(employee, key):
            setattr(employee, key, request.POST[key])
    employee.save()

    return HttpResponseRedirect(reverse('polls:companyDetail', args={employee.company.id}))


def delete(request, pk):
    print(request.get_full_path())
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return HttpResponseRedirect(reverse('polls:companyList'))
#
# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
#
# d
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/result.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#
#     return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


