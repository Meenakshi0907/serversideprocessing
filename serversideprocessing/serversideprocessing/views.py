from django.shortcuts import render

def areacalculation(request):
    context ={}
    context["area"]='0'
    context["b"]='0'
    context["h"]='0'
    if request.method == 'POST':
        
        l=request.POST.get('base','0')
        b=request.POST.get('height','0')
        area=int(l)*int(b)
        context['area'] = area
        context['b']=b
        context['h']=h 
    return render(request,"mathapp/area.html",context)