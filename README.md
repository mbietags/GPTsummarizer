Recursive Text Summarizer with Sparse Priming Representations
This project provides a Python script that takes an arbitrarily large text file as input, recursively summarizes it using OpenAI's GPT-3 until the final summary is shorter than 2000 tokens, and then generates a Sparse Priming Representation (SPR) for the summarized content.

**Features**

Reads text files of any size
Splits large text files into smaller chunks and summarizes each chunk using GPT-3
Recursively summarizes the content until the final summary is shorter than 2000 tokens
Generates a Sparse Priming Representation (SPR) for efficient knowledge storage and retrieval
Utilizes OpenAI's GPT-3 for generating summaries and SPRs

**Requirements**
Python 3.6 or higher
OpenAI Python package: pip install openai
An OpenAI API key


**Note**
The quality of the SPR may not be as accurate or effective as intended since GPT-3 is not specifically trained for generating Sparse Priming Representations. You may need to fine-tune the model or experiment with different prompts to get better results.

Remember to replace yourusername in the clone URL with your actual GitHub username.
