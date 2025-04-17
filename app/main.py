from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
import uvicorn

from app.routers import ticker, market, screener, search

app = FastAPI(
    title="YFinance API",
    description="API for Yahoo Finance data using yfinance library",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ticker.router, prefix="/api/ticker", tags=["Ticker"])
app.include_router(market.router, prefix="/api/market", tags=["Market"])
app.include_router(screener.router, prefix="/api/screener", tags=["Screener"])
app.include_router(search.router, prefix="/api/search", tags=["Search"])

@app.get("/", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=3000, reload=True) 