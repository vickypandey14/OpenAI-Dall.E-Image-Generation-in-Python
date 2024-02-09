import os
import openai
import webbrowser
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found in .env file")

openai.api_key = api_key

user_prompt = input("Write A Prompt: ")

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']

# Create an HTML template with the image
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Display</title>
</head>
<body>
    <h1>Generated Image - ByteWebster</h1>
    <img src="{image_url}" alt="Generated Image" width="500">
</body>
</html>
"""

# Specify the folder where you want to save the HTML file
output_folder = "dalle-images"
os.makedirs(output_folder, exist_ok=True)

# Define the file path for the HTML file
file_path = os.path.join(output_folder, "image_display.html")

# Save the HTML template to the specified folder
with open(file_path, "w") as file:
    file.write(html_template)

print(f"Image URL: {image_url}")
print(f"HTML template saved to '{file_path}'")

# Open the HTML file in the default web browser
webbrowser.open(file_path)