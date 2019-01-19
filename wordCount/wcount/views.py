from django.shortcuts import render
from django.http import HttpResponse
import operator


# Create your views here.

def homepage(request):
    return render(request, 'wcount/home.html')

def about(request):
    return render(request, 'wcount/about.html')

def count(request):
    fulltext=request.GET['text']
    word_count=len(fulltext.split())
    word_list=fulltext.split()
    word_dict={}
    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    tup=[(i, word_dict[i]) for i in word_dict]
    return render(request, 'wcount/count.html', {'fulltext':fulltext, 'wordcount': word_count,'word_list_count':tup})
