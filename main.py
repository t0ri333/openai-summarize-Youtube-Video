import openai
import os

# ID of the video
VIDEO_ID = 'QA6ebemXDwE'

# Openai api key. Check https://beta.openai.com/account/api-keys
OPENAI_API_KEY = ' '

# Openai language model. Check https://beta.openai.com/docs/models/gpt-3
LANG_MODEL = 'text-davinci-002'

# Import the YouTubeTranscriptApi module
from youtube_transcript_api import YouTubeTranscriptApi

# Get the transcript for the video
script = YouTubeTranscriptApi.get_transcript(VIDEO_ID)

# Extract the text values from the script
text_values = [obj['text'] for obj in script]

# Join the text values into a single transcript
transcript = ' '.join(text_values)

# Set the API key
openai.api_key = OPENAI_API_KEY

# Set the prompt for the GPT-3 chatbot
prompt = f"Please summarize the following transcript: {transcript}"

# Use the GPT-3 chatbot to generate a summary
response = openai.Completion.create(engine=LANG_MODEL, prompt=prompt, max_tokens=4097)

# Get the summary from the chatbot's response
summary = response['choices'][0]['text']

# Print the summary
print(summary)
