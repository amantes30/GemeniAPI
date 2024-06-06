import pathlib
import textwrap
import os
import asyncio
import google.generativeai as genai
import json;
from IPython.display import display
from IPython.display import Markdown
import requests
import webbrowser
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')


genai.configure(api_key=GOOGLE_API_KEY)

if (genai.get_model == None):
    print("API key is not valid")
else:
    print("API key is valid")
def send_data(json_data):
    url = "http://amantes30.com/thesis/testcases"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=json_data, headers=headers)
      # Check if the request was successful
    if response.status_code == 200:
        print("Successfully sent the JSON data to the backend.")
        webbrowser.open(url)
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
async def main():
    model = genai.GenerativeModel('gemini-pro')
    message = str(input("App name: "))
    prompt= f"""
    I need you to generate test cases in order to perform GUI testing on {message} Android app.
    the response need to be in json format, and should include the following fields: 
    test case Id, 
    test case description, 
    test case steps, 
    expected results""";
    response = await model.generate_content_async("Hello Gemini! + " + prompt);
    try:
        json_data = json.loads(response.text)
        print(json_data)
        send_data(json_data)
    except json.JSONDecodeError:
         print("Failed to convert response to JSON.")
    print ('**********response**********')
    print(response.text)

if __name__ == "__main__":
    asyncio.run( main())