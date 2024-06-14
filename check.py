import os, sys, subprocess

# Clearing the Screen
os.system('cls')

print(f"Python version: {sys.version}")

try:
  import flask
except:
  subprocess.run(["pip", "install", "Flask"])
  import flask
print(f"Flask version: {flask.__version__}")

try: 
  import requests
except:
  subprocess.run(["pip", "install", "requests"])
  import requests
print(f"requests version: {requests.__version__}")

try:
  from dotenv import load_dotenv
  load_dotenv()
except:
  subprocess.run(["pip", "install", "python-dotenv"])
  from dotenv import load_dotenv
  load_dotenv()
for name, value in os.environ.items():
  if "API" in name:
    print(f"{name} = {value}")