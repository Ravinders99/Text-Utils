from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"home.html")
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    captalize= request.POST.get('captalize','off')
    newLine= request.POST.get('newLine','off')
    spaceremover= request.POST.get('spaceremover','off')
    charcount= request.POST.get('charcount','off')
    purpose =""
    
    # Check the checkbox
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~1234567890'''
        count =0
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        purpose ='|Remove Punctuation| '
        param ={"purpose ":purpose,"analyzed_text":analyzed,"Count":count}
        djtext = analyzed
        

    if(captalize=="on"):
        analyzed = ""
        count=0
        for char in djtext:
            analyzed = analyzed + char.upper()

        purpose +='|Capatilize| '
        param ={"purpose ":purpose,"analyzed_text":analyzed,"Count":count}
        djtext = analyzed
       

    if(spaceremover=="on"):
        analyzed = ""
        count=0
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        purpose +='|Remove Spaces| '
        param ={"purpose ":purpose,"analyzed_text":analyzed,"Count":count}
        djtext = analyzed
       

    if (newLine == "on"):
        count=0
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        purpose +='|New Line Remover| '
        param ={"purpose ":purpose,"analyzed_text":analyzed,"Count":count}
    if charcount=='on':
        
        count =0
        for char in djtext:
                count = count+1
        purpose +="|Count|"
        param ={"purpose":purpose,"analyzed_text":analyzed,"Count":count}
    

    if(removepunc != "on" and spaceremover!="on" and newLine!="on" and captalize!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', param)    