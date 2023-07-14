from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline #method of transformers model(helps us to implement models of transformers)

app = Flask(__name__) # setting up appname

@app.get('/summary') #used to call url or API requests which is basically an url
def summary_api():
    url = request.args.get('url', '') #fetching the url
    video_id = url.split('=')[1]
