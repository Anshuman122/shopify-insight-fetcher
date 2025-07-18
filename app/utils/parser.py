

def extract_faq_using_llm(faq_text: str) -> list:
    print("[FAKE LLM] Returning hardcoded FAQ list.")
    return [
        {"question": "Do you offer COD?", "answer": "Yes, we do."},
        {"question": "How long does shipping take?", "answer": "5–7 days."}
    ]
