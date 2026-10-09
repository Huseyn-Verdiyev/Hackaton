import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "mock-key-for-testing"))

def generate_special_offer(feedback_text, analysis, customer_data):
    """
    Generates a personalized response and special offer strictly respecting business margins.
    """
    ltv = customer_data.get("lifetime_value_usd", 0)
    margin_limit = customer_data.get("margin_limit_percentage", 5)

    if client.api_key == "mock-key-for-testing":
        # Mock response dynamically adapting to LTV and Margins
        if ltv > 1000:
            return f"As a VIP customer, we deeply apologize. We've applied a {margin_limit}% credit to your massive account and assigned a dedicated account manager to resolve this today."
        elif analysis.get('priority') == 'high':
            return f"We are sorry for the frustration. Here is a {margin_limit}% discount code for your next month."
        else:
            return "Thank you for your feedback! Here is a small token of appreciation."

    try:
        prompt = f"""
        You are an elite Customer Retention AI that must protect company revenue while retaining customers.

        Customer Profile:
        - Lifetime Value (LTV): ${ltv}
        - Maximum Allowed Discount/Margin: {margin_limit}%

        Customer Feedback: "{feedback_text}"
        Analysis of Problem: {analysis}

        Rules for the Offer:
        1. YOU MUST NEVER EXCEED the maximum allowed discount/margin of {margin_limit}%.
        2. If the LTV is very high (VIP), prioritize concierge-level service (e.g., dedicated support) rather than just giving away money, but you can give up to {margin_limit}% discount.
        3. If the LTV is low, give a very small, strict, automated discount (up to {margin_limit}%).
        4. Write a short, highly personalized, empathetic message.
        5. DO NOT use placeholder brackets like [Name]. Return the final ready-to-send text.
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
