from google import genai
from google.genai import types

# Assign your API key to api_key
client = genai.Client(api_key="<YOUR API KEY>")

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool],
    temperature=0.4,
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide top 10 news today. For each news, provide headline and summary consisting of 4 to 5 sentences. Also, provide the publisher for each news. Format it as a numbered list.",
    config=config,
)

raw_text = response.text
cleaned_text = raw_text.replace('**', '')
cleaned_text = cleaned_text.replace('*', '')

output_filename = "top 10 news_gemini.txt"

with open(output_filename, "w", encoding='utf-8') as f:
    f.write(cleaned_text)

print("News successfully saved")