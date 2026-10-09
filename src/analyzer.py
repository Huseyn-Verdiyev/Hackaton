import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize client. Assumes OPENAI_API_KEY is in environment or .env
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "mock-key-for-testing"))

def analyze_feedback(feedback_text):
    """
    Analyzes the customer feedback to extract sentiment, core issue, and priority.
    """
    if client.api_key == "mock-key-for-testing":
        # Mock response for hackathon demo if no key is provided
        if "crash" in feedback_text.lower():
            return {
                "sentiment": "negative",
                "core_issue": "App crashes during usage",
                "priority": "high",
                "product_insight": "Need to investigate crash logs and improve app stability."
            }
        elif "price" in feedback_text.lower() or "expensive" in feedback_text.lower():
            return {
                "sentiment": "negative",
                "core_issue": "Pricing is considered too high",
                "priority": "medium",
                "product_insight": "Consider introducing a mid-tier subscription plan."
            }
        else:
            return {
                "sentiment": "neutral",
                "core_issue": "General feedback",
                "priority": "low",
                "product_insight": "Monitor for further patterns."
            }

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a product manager AI. Analyze the following customer feedback. Return a JSON object with keys: 'sentiment' (positive/neutral/negative), 'core_issue' (brief description of the problem), 'priority' (high/medium/low), and 'product_insight' (what the dev/product team should do to fix it). Output ONLY raw JSON without markdown formatting."},
                {"role": "user", "content": feedback_text}
            ],
            temperature=0
        )
        # Parse the JSON response
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        print(f"Error during analysis: {e}")
        return None
