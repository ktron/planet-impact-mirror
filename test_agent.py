import asyncio
import pytest
import time
from agent import async_combined_agent, bing_web_search

@pytest.mark.asyncio
async def test_bing_web_search():
    # This test assumes BING_SEARCH_API_KEY is set and valid
    result = bing_web_search("carbon emissions")
    assert isinstance(result, str)
    assert "carbon" in result.lower() or "error" in result.lower() or "no relevant" in result.lower()

@pytest.mark.asyncio
async def test_async_combined_agent_response():
    user_input = "Tell me about Elon Musk's carbon footprint and wealth."
    response = await async_combined_agent(user_input)
    assert isinstance(response, str)
    assert len(response) > 0
    assert "Offset your existence" in response or "carbon" in response.lower() or "wealth" in response.lower()

@pytest.mark.asyncio
async def test_async_combined_agent_performance():
    user_input = "Tell me about Elon Musk's carbon footprint and wealth."
    start_time = time.perf_counter()
    response = await async_combined_agent(user_input)
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"async_combined_agent execution time: {duration:.2f} seconds")
    assert duration < 10, "async_combined_agent took too long to respond"
    assert isinstance(response, str)
    assert len(response) > 0