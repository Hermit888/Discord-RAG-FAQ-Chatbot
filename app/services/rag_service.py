import os
import logging
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

"""
RAG Service using Google Gemini Pro model
to answer questions based on provided context.
"""

# load api key from .env file
logger = logging.getLogger(__name__)

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# models = genai.list_models()
# for m in models:
#     print(m.name, m.supported_generation_methods)
# initialize the Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-flash")

PYTHON_CONTEXT = """
You are a Python expert assistant.
Answer clearly, concisely, and with code examples if helpful.
Only answer Python-related questions, and the length is less than 2000 characters.
"""

def query_rag(query: str) -> str:
    logger.info('Calling Gemini', extra={'query': query})

    prompt = f"""
    {PYTHON_CONTEXT}

    User question:
    {query}
    """

    response = model.generate_content(prompt)

    return response.text