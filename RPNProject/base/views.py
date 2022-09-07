from importlib.resources import contents
from webbrowser import Opera
from django.shortcuts import render, redirect
from .models import Operation, Stackmodel
from .forms import StackForm
from django.db.models import Q

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    #stacks = Stackmodel.objects.all()
    stacks = Stackmodel.objects.filter( 
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    operations = Operation.objects.filter(Q(stackmodel__name__icontains=q)).order_by('-created')
    stack_count = stacks.count()
    context = {'stacks': stacks, 'stack_count': stack_count, "stack_operations": operations}
    return render(request, 'home.html', context)

def createStack(request):
    form = StackForm()
    if request.method == "POST":
        form = StackForm(request.POST)
        if form.is_valid():
            stack = form.save(commit=False)
            stack.content = stack.body
            stack.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/stack_form.html', context)


def sum(stack):
    if len(stack) > 1:
        b = float(stack.pop())
        a = float(stack.pop())
        stack.append(a+b)
    return stack
def sub(stack):
    if len(stack) > 1:
        b = float(stack.pop())
        a = float(stack.pop())
        stack.append(a-b)
    return stack

def mul(stack):
    if len(stack) > 1:
        b = float(stack.pop())
        a = float(stack.pop())
        stack.append(a*b)
    return stack

def div(stack):
    if len(stack) > 1 and stack[-1] != '0':
        b = float(stack.pop())
        a = float(stack.pop())
        stack.append(a/b)
    return stack


def stack(request, pk):
    stack = Stackmodel.objects.get(id=pk)
    stack_operations = stack.operation_set.all().order_by('-created')
    
    if request.method == "POST":
        operation = Operation.objects.create(
            stackmodel = stack,
            body = request.POST.get('body'), # body is the name of the input in the room.html
            old = stack.content,
            new = stack.content,
        )
        res = ''
        
        if operation.body == "+":
            operation.action = "Addition Operation"
            liste = operation.new.split(',')
            res = ','.join(map(str, sum(liste)))
        elif operation.body == "-":
            operation.action = "Subscription Operation"
            liste = operation.new.split(',')
            res = ','.join(map(str, sub(liste)))
        elif operation.body == "*":
            operation.action = "Multiplication Operation"
            liste = operation.new.split(',')
            res = ','.join(map(str, mul(liste)))
        elif operation.body == "/":
            operation.action = "Division Operation"
            liste = operation.new.split(',')
            res = ','.join(map(str, div(liste)))
        elif operation.body.replace('-','').isdigit():
            operation.action = "Push a New Number " + operation.body 
            res = operation.new + ',' + operation.body
        else:
            operation.action = "Can you please add a digit or an operand ? Thx"
            res = operation.new

            
        operation.old = operation.new
        operation.new = res
        stack.content = res
        operation.save()
        stack.save()

        return redirect('stack', pk=stack.id)


    context = {'stack': stack, 'stack_operations': stack_operations}
    return render(request,'base/stack.html', context)


def deleteStack(request, pk):
    stack = Stackmodel.objects.get(id=pk)

    if request.method == "POST":
        stack.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': stack})


def deleteOperation(request, pk):
    operation = Operation.objects.get(id=pk)

    if request.method == "POST":
        operation.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': operation})