from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any, List
import yfinance as yf
import pandas as pd

from app.models.screener_models import (
    EquityScreenerParams,
    FundScreenerParams,
    ScreenerResponse
)

router = APIRouter()

def dataframe_to_dict(df):
    """Convert pandas DataFrame to dict with date index as string."""
    if isinstance(df, pd.DataFrame):
        df_dict = df.reset_index().to_dict(orient="records")
        return df_dict
    return df

@router.post("/equity", response_model=ScreenerResponse)
async def screen_equity(params: EquityScreenerParams):
    """
    Screen for equities based on specified parameters.
    """
    try:
        # Note: yfinance does not provide a direct screener API
        # This is a placeholder for demonstration purposes
        # In a real implementation, you would need to build a custom screener using data from yfinance
        # or integrate with another service
        
        # For demonstration only
        return ScreenerResponse(
            data={"message": "Equity screener requires implementation with custom logic or additional API"},
            count=0
        )
    except Exception as e:
        return ScreenerResponse(success=False, error=str(e))

@router.post("/fund", response_model=ScreenerResponse)
async def screen_fund(params: FundScreenerParams):
    """
    Screen for funds based on specified parameters.
    """
    try:
        # Note: yfinance does not provide a direct fund screener API
        # This is a placeholder for demonstration purposes
        # In a real implementation, you would need to build a custom screener using data from yfinance
        # or integrate with another service
        
        # For demonstration only
        return ScreenerResponse(
            data={"message": "Fund screener requires implementation with custom logic or additional API"},
            count=0
        )
    except Exception as e:
        return ScreenerResponse(success=False, error=str(e))

@router.get("/sectors", response_model=ScreenerResponse)
async def get_sectors():
    """
    Get list of available sectors.
    """
    try:
        # This is a placeholder - yfinance doesn't have a direct API for sectors
        # You would need to implement a custom solution or integrate with another API
        sectors = [
            "Basic Materials", 
            "Communication Services",
            "Consumer Cyclical",
            "Consumer Defensive",
            "Energy",
            "Financial Services",
            "Healthcare",
            "Industrials",
            "Real Estate",
            "Technology",
            "Utilities"
        ]
        
        return ScreenerResponse(
            data=sectors,
            count=len(sectors)
        )
    except Exception as e:
        return ScreenerResponse(success=False, error=str(e))

@router.get("/industries", response_model=ScreenerResponse)
async def get_industries():
    """
    Get list of available industries.
    """
    try:
        # This is a placeholder - yfinance doesn't have a direct API for industries
        # You would need to implement a custom solution or integrate with another API
        industries = [
            "Aerospace & Defense",
            "Auto Manufacturers",
            "Banks—Diversified",
            "Banks—Regional",
            "Biotechnology",
            "Building Materials",
            "Computer Hardware",
            "Drug Manufacturers—General",
            "Entertainment",
            "Insurance—Diversified",
            "Internet Content & Information",
            "Oil & Gas E&P",
            "Semiconductors",
            "Software—Application",
            "Software—Infrastructure",
            "Telecom Services",
            # This is just a sample, not the complete list
        ]
        
        return ScreenerResponse(
            data=industries,
            count=len(industries)
        )
    except Exception as e:
        return ScreenerResponse(success=False, error=str(e)) 