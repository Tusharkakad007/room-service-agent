import os

class MockLLM:
    async def ask(self, messages):
        last = messages[-1]["content"].lower()

        # simple clarifications based on keywords
        if "or" in last:
            return "Can you clarify your choice?"
        if "gluten" in last:
            return "We have gluten-free pasta and salad. Which one would you like?"
        if "vegetarian" in last and "burger" in last:
            return "The chicken burger conflicts with your vegetarian preference. Would you like a veg alternative?"

        # default fallback
        return "Could you please clarify your order?"

def get_llm():
    return MockLLM()
