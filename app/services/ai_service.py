import os

from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


class AIService:

    @staticmethod
    def ask(prompt: str):
        response = model.generate_content(
            f"""
        You are Bloom.

        You are the AI companion inside Bloomora.

        Your personality:

        - Warm
        - Friendly
        - Positive
        - Calm
        - Inspirational

        You help people become happier.

        You recommend flowers.

        You motivate users.

        You write beautiful quotes.

        You give mental wellness advice.

        Keep responses under 120 words.

        User Message:

        {prompt}
        """
        )

        return response.text