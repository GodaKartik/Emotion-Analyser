from django.shortcuts import render, redirect
from miniProject.models import Thought
from random import randint
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pickle
import os

def removeStopwords(text):
    tokens = word_tokenize(text)
    cleaned = [token for token in tokens if token not in stopwords.words('english')]
    return " ".join(cleaned)

# Create your views here

def home(request):
    return render(request, 'layout.html')

def project(request):
    context =  {
        'img' : randint(1,4),
    }
    if request.method == 'POST':
        thoughts = request.POST.get('thts')
        tht = Thought(thoughts = thoughts)
        tht.save()
        return redirect('/analysis')
    return render(request, 'start.html', context)

def analysis(request):
    text = Thought.objects.order_by('id')[len(Thought.objects.order_by('id'))-1].thoughts
    cleaned_text = removeStopwords(text)

    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'lr.pkl')
    lrmodel = pickle.load(open(filename, 'rb'))
    filename = os.path.join(here, 'vectorizer.pkl')
    vectorizer = pickle.load(open(filename,'rb'))
    vector = vectorizer.transform([cleaned_text])

    dct = dct = dict(zip(lrmodel.classes_,lrmodel.predict_proba(vector)[0]*100))
    for i in dct:
        dct[i] = str(round(dct[i],2))+'%'

    context = {
        'bruh' : cleaned_text,
        'prime_emotion' : change_emotion_form(lrmodel.predict(vector)[0]),
        'emotions' : dct,
    }
    return render(request, 'analysis.html', context)


# UTILITY MEHTODS

def change_emotion_form(emotion):
    dct = {
        'fear' : 'scared',
        'anger' : 'angry',
        'joy' : 'happy',
        'surprise' : 'surprised',
        'sadness' : 'sad',
        'love' : 'in love'
    }
    return dct[emotion]
