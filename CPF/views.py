from django.shortcuts import render
from .forms import CpfPlanning
# Create your views here.

def CPFPlanning(request):
    form = CpfPlanning()
    context = {'form':form}

    return render(request,'CPF/PlanningPage.html',context)
