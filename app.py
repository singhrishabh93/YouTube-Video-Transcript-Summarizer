from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline #method of transformers model(helps us to implement models of transformers)

app = Flask(__name__) # setting up appname

@app.get('/summary') #used to call url or API requests which is basically an url
def summary_api():
    url = request.args.get('url', '') #fetching the url
    video_id = url.split('=')[1]
    summary = get_summary(get_transcript(video_id)) #passing the video id to transcript function and passing the whole transcript to the summary function
    return summary, 200

def get_transcript(video_id): #this transcript return the list of all the transcript provided by YouTube
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list]) #joining all the string to get a whole paragraph
    return transcript

def get_summary(transcript): #for summarizing I'not implementing the whole model instead of it, using the existing model implementation by Hugging Face
    summariser = pipeline('summarization') #type of model i.e. here we used 'summarization' model
    summary = ''
    for i in range(0, (len(transcript)//1000)+1): #But it has a limitation that it can provide a summary of text that is smaller than 1000 characters, so to remove this limitation we can split the content into multiple parts
        summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary = summary + summary_text + ' '
    return summary


if __name__ == '__main__':
    app.run()


