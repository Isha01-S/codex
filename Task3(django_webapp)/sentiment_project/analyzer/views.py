from django.shortcuts import render
from textblob import TextBlob 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        text = request.POST['text']
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return render(request, 'result.html', {
            'text': text,
            'sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': subjectivity
        })
    return render(request, 'home.html')
