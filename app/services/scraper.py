import requests
from bs4 import BeautifulSoup
from app.utils.parser import extract_faq_using_llm
from typing import List

import time

def fetch_products(website_url):
    try:
        start = time.time()
        url = f"{website_url}/products.json"
        print(f"[SCRAPER] Trying to fetch: {url}", flush=True)

        res = requests.get(url, timeout=5)

        duration = time.time() - start
        print(f"[SCRAPER] Response time: {duration:.2f} seconds", flush=True)

        if res.status_code != 200:
            print(f"[SCRAPER] Non-200 response: {res.status_code}", flush=True)
            return []

        data = res.json()
        products = [product['title'] for product in data.get('products', [])]
        print(f"[SCRAPER] Found {len(products)} products", flush=True)

        return products

    except Exception as e:
        print(f"[SCRAPER] Error: {e}", flush=True)
        return []


def scrape_website(website_url: str):
    products = fetch_products(website_url)

    # Fallback FAQ
    raw_faq_text = "Q. Do you offer COD?\nA. Yes we do.\nQ. How long does shipping take?\nA. 5–7 days."
    faqs = extract_faq_using_llm(raw_faq_text)

    return {
        "brand_name": "Test Brand",
        "products": products,
        "hero_products": products[:3],  # Example
        "privacy_policy": "We value your privacy.",
        "return_policy": "Returns accepted within 30 days.",
        "refund_policy": "Refunds processed within 5–7 business days.",
        "faqs": faqs,
        "social_links": ["https://instagram.com/testbrand"],
        "contact_emails": ["support@testbrand.com"],
        "contact_numbers": ["+91-1234567890"],
        "about_brand": "We are a Shopify-based D2C brand.",
        "important_links": ["https://testbrand.com/about", "https://testbrand.com/contact"]
    }
