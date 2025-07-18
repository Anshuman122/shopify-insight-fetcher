
🧠 Brand Insights Scraper API  
This is a simple FastAPI project that takes a Shopify website URL and gives back product details, brand policies, contact info, and FAQs.

📝 What You Need  
- Python 3.8 or above  
- Internet connection  
- Any code editor (like VS Code)  
- Postman or browser for testing  

⚙️ How to Run (Step-by-Step)

1️⃣ Clone this Project  
git clone https://github.com/yourusername/brand-insights-scraper.git  
cd brand-insights-scraper  

2️⃣ Create a Virtual Environment  
# For Windows  
python -m venv venv  
venv\Scripts\activate  

# For macOS/Linux  
python3 -m venv venv  
source venv/bin/activate  

3️⃣ Install All Required Libraries  
pip install -r requirements.txt  

This will install packages like
fastapi
uvicorn
requests
beautifulsoup4
pydantic
and many more from requirement.txt

4️⃣ Add Your .env File  
  
OPENAI_API_KEY=sk-dummy-key  


5️⃣ Start the Server  
uvicorn app.main:app --reload  

🔍 Test the API

Use This Endpoint:  
GET /fetch-insights?website_url="https://examplestore.myshopify.com"  

Test on postman with GET request:  
http://127.0.0.1:8000/fetch-insights?website_url="https://examplestore.myshopify.com"  

(Replace the link"https://examplestore.myshopify.com" with any real Shopify store.)

OUTPUT will be a JSON file with the details of the store


FOLDER STRUCTURE

shopify_insight_fetcher
├── app
│ ├── main.py
│ ├── models
│ │ └── schema.py
│ ├── routers
│ │ └── fetch.py
│ ├── services
│ │ └── scraper.py
│ └── utils
│ └── parser.py
├── .env # Your environment variables (OpenAI Secret Key like OPENAI_API_KEY=sk-xxx-example)
├── requirements.txt # All dependencies
├── README.md # This file