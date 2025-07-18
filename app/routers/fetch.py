from fastapi import APIRouter, HTTPException
from pydantic import HttpUrl
from app.models.schema import BrandInsights
from app.services.scraper import scrape_website

router = APIRouter()
from urllib.parse import urlparse

import time

@router.get("/fetch-insights", response_model=BrandInsights)
def get_brand_insights(website_url: HttpUrl):
    try:
        start = time.time()
        url_str = str(website_url)

        print(f"→ [START] Incoming request for {url_str}", flush=True)

        insights = scrape_website(url_str)

        print(f"→ [END] Done scraping. Took {time.time() - start:.2f}s", flush=True)

        if not insights["products"]:
            raise HTTPException(status_code=404, detail="No products found.")

        return BrandInsights(**insights)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


