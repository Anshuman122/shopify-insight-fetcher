from pydantic import BaseModel
from typing import List, Optional

class FAQ(BaseModel):
    question: str
    answer: str

class BrandInsights(BaseModel):
    brand_name: Optional[str]
    products: List[str]
    hero_products: List[str]
    privacy_policy: Optional[str]
    return_policy: Optional[str]
    refund_policy: Optional[str]
    faqs: List[FAQ]
    social_links: List[str]
    contact_emails: List[str]
    contact_numbers: List[str]
    about_brand: Optional[str]
    important_links: List[str]
