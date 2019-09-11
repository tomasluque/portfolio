from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'wordCount/home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        value = word.lower()
        if value in worddictionary:
            worddictionary[value] += 1
        else:
            worddictionary[value] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'wordCount/count.html', {
        'fulltext': fulltext, 
        'count': len(wordlist), 
        'sortedwords': sortedwords
        }) 