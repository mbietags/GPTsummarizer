import openai
import os
from time import time, sleep
import textwrap
import re

# Function to open a file and return its content
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Function to save content to a file
def save_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

# Set up the OpenAI API key
openai.api_key = open_file("openaiapikey.txt")

# Function for GPT-3 completion
def gpt3_completion(prompt, engine='text-davinci-003', temp=0.6, tokens=2000, top_p=1.0, freq_pen=0.25, pres_pen=0.0, stop=['<<END>>']):
    max_retry = 5
    retry = 0
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response.choices[0].text.strip()
            text = re.sub('\s+', ' ', text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % oops
            print('Error communicating with OpenAI:', oops)
            sleep(1)

def recursive_summarize(text):
    if len(text) <= 2000:
        return text

    chunks = textwrap.wrap(text, 2000)
    summarized_chunks = []

    for chunk in chunks:
        prompt = f"Please summarize the following text:\n\n{chunk}\n"
        summary = gpt3_completion(prompt)
        summarized_chunks.append(summary)

    summarized_text = ' '.join(summarized_chunks)
    return recursive_summarize(summarized_text)

# Example usage
input_file_path = 'input.txt'
file_content = open_file(input_file_path)

# Summarize the input file recursively
final_summary = recursive_summarize(file_content)

# Save the final summary to a new .txt file
output_file_path = f'output_at_time_{time()}.txt'
save_file(final_summary, output_file_path)


def generate_spr(summary):
    prompt = f"Generate a Sparse Priming Representation (SPR) for the following summarized text:\n\n{summary}\n"
    spr = gpt3_completion(prompt)
    return spr

# Example usage
input_file_path = 'input.txt'
file_content = open_file(input_file_path)

# Summarize the input file recursively
final_summary = recursive_summarize(file_content)

# Generate a Sparse Priming Representation (SPR) from the final summary
spr = generate_spr(final_summary)

# Save the SPR to a new .txt file
spr_file_path = f'spr_at_time{time()}.txt'
save_file(spr, spr_file_path)