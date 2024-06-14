from g4f.client import Client
import yaml
from yaml import Loader, Dumper

client = Client()
test_doc = '''
name: Python
description: Python basic course for dummies
course:
  1:
    chapter-name: Hello World
    info: In this chapter you need to describe how to install on windows/linux (use linux mint as example on linux), first 'hello world' code and what it means
  2:
    chapter-name: Greetable input and output
    info: In this chapter you need to describe how to use input string and print content and create basic Hello Name program
'''
info = yaml.load(test_doc, Loader=Loader)
print(info)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "system", "content": "You're an AI Programming teacher ezcode. You need to write text for course with chapters. User gives you chapter name and instructions for this chapter"}, {"role": "user", "content": f"Chapter name: {info['course'][1]['chapter-name']}\nInstructions: {info['course'][1]['info']}. Write it on Russian language"}]
)

print(response.choices[0].message.content)