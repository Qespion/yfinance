from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any
import yfinance as yf
import pandas as pd

from app.models.market_models import (
    MarketSummaryParams,
    MarketMoversParams,
    MarketResponse
)

router = APIRouter()

def dataframe_to_dict(df):
    """Convert pandas DataFrame to dict with date index as string."""
    if isinstance(df, pd.DataFrame):
        df_dict = df.reset_index().to_dict(orient="records")
        return df_dict
    return df

@router.get("/summary", response_model=MarketResponse)
async def get_market_summary(params: MarketSummaryParams = Depends()):
    """
    Get market summary data.
    """
    try:
        # Note: yfinance doesn't have a direct market summary API,
        # so we'll get summary for major indices
        indices = ["^GSPC", "^DJI", "^IXIC", "^RUT", "^VIX"]
        market_data = {}
        
        for index in indices:
            ticker = yf.Ticker(index)
            if ticker:
                info = ticker.info
                if info:
                    market_data[index] = {
                        "shortName": info.get("shortName", ""),
                        "regularMarketPrice": info.get("regularMarketPrice", None),
                        "regularMarketChange": info.get("regularMarketChange", None),
                        "regularMarketChangePercent": info.get("regularMarketChangePercent", None),
                        "regularMarketTime": info.get("regularMarketTime", None),
                        "marketCap": info.get("marketCap", None),
                        "regularMarketVolume": info.get("regularMarketVolume", None),
                        "regularMarketDayHigh": info.get("regularMarketDayHigh", None),
                        "regularMarketDayLow": info.get("regularMarketDayLow", None),
                        "regularMarketOpen": info.get("regularMarketOpen", None),
                        "regularMarketPreviousClose": info.get("regularMarketPreviousClose", None),
                    }
        
        return MarketResponse(data=market_data)
    except Exception as e:
        return MarketResponse(success=False, error=str(e))

@router.get("/movers/gainers", response_model=MarketResponse)
async def get_market_gainers(params: MarketMoversParams = Depends()):
    """
    Get top gainers in the market.
    """
    try:
        # Note: yfinance doesn't have a direct market movers API,
        # This is a placeholder - in a real-world scenario you might need to 
        # implement a custom solution or use another API
        
        # Placeholder for demonstration
        return MarketResponse(data={"message": "This endpoint requires implementation with a custom solution or additional API"})
    except Exception as e:
        return MarketResponse(success=False, error=str(e))

@router.get("/movers/losers", response_model=MarketResponse)
async def get_market_losers(params: MarketMoversParams = Depends()):
    """
    Get top losers in the market.
    """
    try:
        # Note: similar to gainers, this would need a custom implementation
        return MarketResponse(data={"message": "This endpoint requires implementation with a custom solution or additional API"})
    except Exception as e:
        return MarketResponse(success=False, error=str(e))

@router.get("/movers/active", response_model=MarketResponse)
async def get_most_active(params: MarketMoversParams = Depends()):
    """
    Get most active stocks in the market.
    """
    try:
        # Note: similar to gainers, this would need a custom implementation
        return MarketResponse(data={"message": "This endpoint requires implementation with a custom solution or additional API"})
    except Exception as e:
        return MarketResponse(success=False, error=str(e)) 