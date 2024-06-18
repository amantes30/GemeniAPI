import pathlib
import textwrap
import os
import asyncio
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import json
from hp_func import extract_json;
#from functions import extract_json, to_markdown, send_data

async def main():
    # SETUP
    GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    if (genai.get_model == None):
        print("API key is not valid")
    else:
        print("API key is valid")
        # CHOOSE MODEL AND SEND PROMPT
        model = genai.GenerativeModel('gemini-pro')
        message = str(input("App name: "))
        prompt= f"""
        I need you to generate test cases in order to perform GUI testing on {message} Android app.
        the response need to be in json format, and should include the following fields: 
        test case Id, 
        test case description, 
        test case steps, 
        expected results.
        output the json file only don't put any markdown""";
        response = await model.generate_content_async("Hello Gemini! " + prompt)
        response_txt = extract_json(response.text)
        
        # CREATE OUTPUT FILE TO SAVE THE RESPONSE
        with open('output.json', 'w') as file:
            json.dump(response_txt, file)
        print("Response saved in output.json")
        

if __name__ == "__main__":
    asyncio.run(main())