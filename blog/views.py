from django.shortcuts import render, get_object_or_404
from .models import Blog
from random import *

lineList = [
    'Hasta la vista, baby',
    'I\'ma get medieval on your ass.',
    'There\'s nothing wrong with letting the girls know that you\'re money and that you want to party.',
    'That rug really tied the room together.',
    'I had no idea you could milk a cat.',
    'Just when I thought I was out, they pull me back in.',
    'As far back as I can remember, I always wanted to be a gangster.',
    'Hello. My name is Inigo Montoya. You killed my father. Prepare to die!',
    'Why am I Mr. Pink?',
    'Houston, we have a problem',
]

def allblogs(request):
    blog = Blog.objects
    
    rng = randint(0, 14)
    rng2 = randint(0, 9)

    quoteList = [
        ['I don’t dream at night, I dream at day, I dream all day; I’m dreaming for a living.', 'Steven Spielberg'],
        ['If it’s a good movie, the sound could go off and the audience would still have a pretty clear idea of what was going on.', 'Alfred Hitchcock'],
        ['Self-plagiarism is style', 'Alfred Hitchcock'],
        ['I don’t want to tell you how to do your job, but somebody has to.', 'David Fincher'],
        ['Cinema is a matter of what’s in the frame and what’s out.', 'Martin Scorsese'],
        ['I don’t believe that the public knows what it wants; this is the conclusion that I have drawn from my career.', 'Charlie Chaplin'],
        ['Cinema should make you forget you are sitting in a theater.', 'Roman Polanski'],
        ['The saddest journey in the world is the one that follows a precise itinerary. Then you’re not a traveler, you’re a fucking tourist.', 'Guillermo del Toro'],
        ['I didn\'t show up at the ceremony to collect any of my first three Oscars. Once I went fishing, another time there was a war on, and on another occasion, I remember, I was suddenly taken drunk.', 'John Ford'],
        ['I\'m a skilled professional actor. Whether or not I\'ve any talent is beside the point.', 'Michael Caine'],
        ['I try to push ideas away, and the ones that will not leave me alone are the ones that ultimately end up happening.', 'J.J. Abrams'],
        ['All You need for is movie is: a gun and a girl.”', 'Jean-Luc Godard'],
        ['Life is a combination of magic and pasta', 'Federico Fellini'],
        ['Human beings share the same common problems. A film can only be understood if it depicts these properly.', 'Akira Kurosawa'],
        ['If you have to have a job in this world, a high-priced movie star is a pretty good gig.', 'Tom Hanks']
    ]


    return render(request, 'blog/homepage.html', {'blog': blog, 'quote_content': quoteList[rng][0], 'quote_author': quoteList[rng][1], 'bottomline': lineList[rng2]})

def detail(request, slug):
    detailBlog = get_object_or_404(Blog, slug=slug)
    rng = randint(0, 9)
    return render(request, 'blog/article.html', {
        'article': detailBlog,
        'bottomline': lineList[rng]
    })