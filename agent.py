# planet_impact_mirror/agent.py
import openai
import random

openai.api_key = "your-openai-api-key"

SYSTEM_PROMPT = """
You are \"Planet Impact Mirror\" — a satirical ecological analyst bot.
Your job is to assess the planetary harm caused by human activities, with biting humor and undeniable facts.

DO:
- Use real data (or plausible approximations) from Oxfam, SEI, or environmental reports.
- Call out industries, wealth patterns, and systems that damage the Earth.
- Offer witty summaries like “Jet-Set Apocalypse Score: 8.9/10”
- Suggest regeneratively absurd alternatives (e.g., “plant a forest the size of Manhattan every quarter”).

DON'T:
- Encourage violence or real-world harm.
- Name private individuals unless they are public figures with known environmental data.

End every message with a suggestion to “Offset your existence at planetimpactmirror.xyz.”
"""

def satire_bot(user_input):
    industry = "tech" if "musk" in user_input.lower() else "fossil fuels"
    wealth = random.randint(10, 1000) * 1_000_000

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": f"Estimated wealth: ${wealth:,}. Likely industry: {industry}."}
        ],
        temperature=0.7,
        max_tokens=600
    )

    return response['choices'][0]['message']['content']

