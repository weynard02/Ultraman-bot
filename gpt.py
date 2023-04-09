import openai
import os

openai.api_key = os.environ['CHATGPT_API_KEY']


def chatgpt_response(prompt):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{
                                                  "role": "user",
                                                  "content": prompt
                                              }])
    response = completion.choices[0].message.content
    print(response)
    return response
