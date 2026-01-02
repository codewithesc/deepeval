import os
from typing import List
from openai import OpenAI
from deepeval.prompt.prompt import Prompt
from deepeval.optimizer.prompt_optimizer import PromptOptimizer
from deepeval.dataset.golden import Golden
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.models import GPTModel
import deepeval_poc


def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    eval_model = GPTModel(model="gpt-4o")

    initial_prompt = Prompt(
        alias="support-agent",
        text_template="Answer the question: {question}"
    )

    goldens = [
        Golden(
            input="How do I reset my password?",
            expected_output="To reset your password, go to the login page and click 'Forgot Password'. Enter your email address and we'll send you a reset link. Click the link in your email to create a new password."
        ),
        Golden(
            input="What are your support hours?",
            expected_output="Our support team is available 24/7 via live chat and email. Phone support is available Monday-Friday, 9 AM - 6 PM EST."
        ),
        Golden(
            input="How can I upgrade my plan?",
            expected_output="To upgrade: Log in to your account, go to Settings > Billing, click 'Upgrade Plan', select your desired tier, and confirm payment. The upgrade takes effect immediately."
        ),
        Golden(
            input="Can I get a refund?",
            expected_output="Yes, we offer full refunds within 30 days of purchase. Go to Settings > Billing > Request Refund, or email billing@example.com. Refunds are processed within 5-7 business days."
        ),
    ]

    def model_callback(prompt: Prompt, golden: Golden) -> str:
        interpolated = prompt.interpolate(question=golden.input)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": interpolated}],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()

    optimizer = PromptOptimizer(
        model_callback=model_callback,
        metrics=[AnswerRelevancyMetric(threshold=0.7, model=eval_model)],
        optimizer_model=eval_model,
    )

    print("\nOptimizing with GEPA algorithm...")
    optimized = optimizer.optimize(prompt=initial_prompt, goldens=goldens)

    print("\n" + "="*70)
    print("RESULTS")
    print("="*70)
    print("\nORIGINAL:")
    print(f'"{initial_prompt.text_template}"')
    print("\nOPTIMIZED:")
    print(f'"{optimized.text_template}"')
    print("\n" + "="*70)

    if initial_prompt.text_template == optimized.text_template:
        print("\nPrompt unchanged - original already meets quality threshold.")
    else:
        print("\nPrompt successfully optimized!")
    print("="*70)


if __name__ == "__main__":
    main()
