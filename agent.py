# planet_impact_mirror/agent.py
import openai
import random
import os
import requests
from openai.agents import Tool, create_openai_functions_agent
from openai.responses import ChatResponse

<<<<<<< HEAD
openai.api_key = os.getenv("OPENAI_API_KEY", "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")
=======
openai.api_key = os.getenv("OPENAI_API_KEY", "")
>>>>>>> dde48bc (`Refactor bot.py and agent.py to use OpenAI Responses API`)

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

End every message with a suggestion to “Offset your existence at planetimpactmirror.xyz.”
"""

# Placeholder for API keys - to be set as environment variables or replaced here
CLIMATIQ_API_KEY = os.getenv("CLIMATIQ_API_KEY", "")
FORBES_API_KEY = os.getenv("FORBES_API_KEY", "")
BLOOMBERG_API_KEY = os.getenv("BLOOMBERG_API_KEY", "")
ADS_B_API_KEY = os.getenv("ADS_B_API_KEY", "")
MARINETRAFFIC_API_KEY = os.getenv("MARINETRAFFIC_API_KEY", "")
BING_SEARCH_API_KEY = os.getenv("BING_SEARCH_API_KEY", "")
BING_SEARCH_ENDPOINT = os.getenv("BING_SEARCH_ENDPOINT", "https://api.bing.microsoft.com/v7.0/search")

def bing_web_search(query):
    if not BING_SEARCH_API_KEY:
        return "Web search data not available (Bing API key missing)."
    headers = {
        "Ocp-Apim-Subscription-Key": BING_SEARCH_API_KEY
    }
    params = {
        "q": query,
        "textDecorations": True,
        "textFormat": "HTML",
        "count": 3
    }
    try:
        response = requests.get(BING_SEARCH_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        snippets = []
        for item in search_results.get("webPages", {}).get("value", []):
            snippet = item.get("snippet", "")
            snippets.append(snippet)
        if snippets:
            return "Web search results:\n" + "\n".join(snippets)
        else:
            return "No relevant web search results found."
    except Exception as e:
        return f"Error performing web search: {str(e)}"

def get_carbon_emissions(activity):
    if not CLIMATIQ_API_KEY:
        return "Carbon emissions data not available (API key missing)."
    url = "https://beta3.api.climatiq.io/estimate"
    headers = {
        "Authorization": f"Bearer {CLIMATIQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "emission_factor": {
            "activity_id": activity
        },
        "parameters": {}
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        emissions = result.get("co2e", None)
        if emissions is not None:
            return f"Estimated carbon emissions for {activity}: {emissions} kg CO2e."
        else:
            return "Carbon emissions data not found for the specified activity."
    except Exception as e:
        return f"Error fetching carbon emissions data: {str(e)}"

def get_wealth_info(name):
    # Placeholder implementation - real API integration needed
    if not FORBES_API_KEY and not BLOOMBERG_API_KEY:
        return "Wealth data not available (API keys missing)."
    # For now, return a dummy response
    return f"Estimated net worth of {name} is $X billion (data integration pending)."

def get_flight_tracking_info(flight_id):
    if not ADS_B_API_KEY:
        return "Flight tracking data not available (API key missing)."
    url = f"https://adsbexchange.com/api/{flight_id}"
    headers = {
        "Authorization": f"Bearer {ADS_B_API_KEY}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        # Simplified example of extracting flight info
        return f"Flight {flight_id} is currently at {data.get('altitude', 'unknown altitude')} meters."
    except Exception as e:
        return f"Error fetching flight tracking data: {str(e)}"

def get_yacht_tracking_info(yacht_id):
    if not MARINETRAFFIC_API_KEY:
        return "Yacht tracking data not available (API key missing)."
    url = f"https://services.marinetraffic.com/api/{MARINETRAFFIC_API_KEY}/vessel/{yacht_id}/position"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # Simplified example of extracting yacht position
        position = data.get("position", {})
        lat = position.get("latitude", "unknown")
        lon = position.get("longitude", "unknown")
        return f"Yacht {yacht_id} is currently at latitude {lat}, longitude {lon}."
    except Exception as e:
        return f"Error fetching yacht tracking data: {str(e)}"

<<<<<<< HEAD
def satire_bot(user_input):
    # Basic heuristic to detect keywords for enriched data fetching
    user_input_lower = user_input.lower()
    extra_info = []

    if "carbon" in user_input_lower or "emission" in user_input_lower:
        # Example activity id for flights - this would be dynamic or parsed from input
        carbon_data = get_carbon_emissions("passenger_flight")
        extra_info.append(carbon_data)

    if "billionaire" in user_input_lower or "wealth" in user_input_lower or "net worth" in user_input_lower:
        # Extract name from input - simplified as the whole input for now
        wealth_data = get_wealth_info(user_input)
        extra_info.append(wealth_data)

    if "flight" in user_input_lower:
        # Extract flight id from input - simplified placeholder
        flight_data = get_flight_tracking_info("sample_flight_id")
        extra_info.append(flight_data)

    if "yacht" in user_input_lower:
        # Extract yacht id from input - simplified placeholder
        yacht_data = get_yacht_tracking_info("sample_yacht_id")
        extra_info.append(yacht_data)

    industry = "tech" if "musk" in user_input_lower else "fossil fuels"
    wealth = random.randint(10, 1000) * 1_000_000

    enriched_content = f"Estimated wealth: ${wealth:,}. Likely industry: {industry}."
    if extra_info:
        enriched_content += " Additional data:\n" + "\n".join(extra_info)

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": enriched_content}
=======
async def async_combined_agent(user_input: str) -> str:
    # Define the WebSearchTool
    web_search_tool = Tool(
        name="WebSearch",
        func=lambda q: bing_web_search(q),
        description="Useful for answering questions about current events, industries, wealth, and emissions by searching the web."
    )

    # Facts agent using WebSearchTool and GPT-4o
    facts_agent = create_openai_functions_agent(
        tools=[web_search_tool],
        llm=openai.ChatCompletion,
        system_message="You are a factual assistant providing accurate and up-to-date information.",
        temperature=0.7,
        max_tokens=600
    )

    # Get factual information asynchronously
    facts_response: ChatResponse = await facts_agent.invoke_async(user_input)

    # Satire agent using GPT-4o
    satire_prompt = SYSTEM_PROMPT + "\n\nFactual information:\n" + facts_response.text + "\n\nNow provide a satirical commentary based on the facts and the user input."

    satire_response = await openai.ChatCompletion.acreate(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": satire_prompt},
            {"role": "user", "content": user_input}
>>>>>>> dde48bc (`Refactor bot.py and agent.py to use OpenAI Responses API`)
        ],
        temperature=0.7,
        max_tokens=600
    )

<<<<<<< HEAD
    return response['choices'][0]['message']['content']

=======
    return satire_response.choices[0].message.content
>>>>>>> dde48bc (`Refactor bot.py and agent.py to use OpenAI Responses API`)
