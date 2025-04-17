from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any, List
import yfinance as yf

from app.models.search_models import (
    SearchParams,
    SearchResponse
)

router = APIRouter()

@router.get("/", response_model=SearchResponse)
async def search_tickers(
    query: str,
    limit: int = 10,
    proxy: str = None
):
    """
    Search for securities by name or ticker symbol.
    """
    try:
        # yfinance provides the search() function to search for securities
        search_results = yf.search(query, limit=limit, proxy=proxy)
        
        result_list = []
        if search_results is not None:
            # Format the search results
            for item in search_results:
                result_list.append({
                    "symbol": item.get("symbol", ""),
                    "name": item.get("shortname", ""),
                    "exchange": item.get("exchange", ""),
                    "type": item.get("quoteType", ""),
                    "score": item.get("score", 0)
                })
                
        return SearchResponse(
            data=result_list,
            count=len(result_list)
        )
    except Exception as e:
        return SearchResponse(success=False, error=str(e)) 