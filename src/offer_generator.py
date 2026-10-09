import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "mock-key-for-testing"))

def generate_special_offer(feedback_text, analysis):
    """
    Generates a personalized response and special offer based on the analysis.
    """
    if client.api_key == "mock-key-for-testing":
        # Mock response
        if analysis.get('priority') == 'high' or analysis.get('sentiment') == 'negative':
            return "We are incredibly sorry for the frustration. As an apology, here is a 30% discount code (SORRY30) for your next month while our team works on a fix."
        else:
            return "Thank you for your valuable feedback! Here is a 10% off coupon (THANKS10) for your next purchase."

    try:
        prompt = f"""
        Customer Feedback: "{feedback_text}"
        Analysis: {analysis}

        Write a short, empathetic, and professional message to this customer.
        Acknowledge their specific problem.
        Provide them with a special offer or compensation (e.g., a discount code, free month, or store credit) to retain them as a customer.
        Do not use placeholder brackets like [Name]. Keep it ready to send.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an empathetic Customer Retention Manager."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating offer: {e}")
        return "We apologize for the inconvenience. Please contact support for assistance."
