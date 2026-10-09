import json
import os
from analyzer import analyze_feedback
from offer_generator import generate_special_offer

def load_feedback(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}")
        return []

def main():
    print("🚀 Starting RetentionAI Agent...")

    # Path to mock data
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'feedback.json')
    feedbacks = load_feedback(data_path)

    if not feedbacks:
        print("No feedback data found.")
        return

    print(f"Found {len(feedbacks)} customer feedback records.\n")
    print("-" * 50)

    for item in feedbacks:
        customer_id = item.get("customer_id")
        text = item.get("feedback_text")

        print(f"Processing Customer {customer_id}...")
        print(f"Feedback: '{text}'")

        # 1. Analyze Feedback (Company-Facing Action)
        print("Agent Status: Analyzing sentiment and extracting product insights...")
        analysis = analyze_feedback(text)

        if not analysis:
            print("Failed to analyze. Skipping...\n")
            continue

        print(f"👉 Core Issue Identified: {analysis.get('core_issue')}")
        print(f"👉 Priority: {analysis.get('priority').upper()}")
        print(f"👉 Action for Product Team: {analysis.get('product_insight')}")

        # 2. Generate Special Offer (Customer-Facing Action)
        print(f"Agent Status: Checking customer value (LTV: ${item.get('lifetime_value_usd')}) and Margin Limit ({item.get('margin_limit_percentage')}%)...")
        print("Agent Status: Generating personalized, margin-protected retention offer...")
        offer_message = generate_special_offer(text, analysis, item)

        print(f"✉️  Message to Customer:\n{offer_message}")
        print("-" * 50)

    print("✅ All feedback processed. Product team has been updated and customers have been retained.")

if __name__ == "__main__":
    main()
