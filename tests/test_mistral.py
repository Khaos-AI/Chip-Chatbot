import pytest
from src.llm.mistral_handler import MistralHandler

@pytest.mark.asyncio
async def test_mistral_generation():
    handler = MistralHandler()
    prompt = "Who is Kaito in Project Khaos?"
    response = handler.generate_response(prompt)
    assert len(response) > 0
    assert "Kaito" in response
