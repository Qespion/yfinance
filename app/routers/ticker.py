from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional, Dict, Any
import yfinance as yf
import pandas as pd
from datetime import date
import json

from app.models.ticker_models import (
    HistoryParams, 
    DividendParams, 
    SplitParams, 
    FinancialStatementParams, 
    EarningsDateParams,
    TickerResponse
)

router = APIRouter()

def dataframe_to_dict(df):
    """Convert pandas DataFrame to dict with date index as string."""
    if isinstance(df, pd.DataFrame):
        df_dict = df.reset_index().to_dict(orient="records")
        return df_dict
    return df

@router.get("/{symbol}", response_model=TickerResponse)
async def get_ticker_info(symbol: str):
    """
    Get basic information about a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        return TickerResponse(data=info)
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/fast_info", response_model=TickerResponse)
async def get_ticker_fast_info(symbol: str):
    """
    Get basic information about a ticker using the faster API.
    """
    try:
        ticker = yf.Ticker(symbol)
        fast_info = ticker.fast_info
        # Convert to dict if it's not already
        if hasattr(fast_info, "__dict__"):
            fast_info = {k: v for k, v in fast_info.__dict__.items() if not k.startswith("_")}
        return TickerResponse(data=fast_info)
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/history", response_model=TickerResponse)
async def get_ticker_history(
    symbol: str, 
    params: HistoryParams = Depends()
):
    """
    Get historical market data for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        history = ticker.history(
            period=params.period,
            interval=params.interval,
            start=params.start,
            end=params.end,
            prepost=params.prepost,
            auto_adjust=params.auto_adjust,
            back_adjust=params.back_adjust,
            repair=params.repair,
            keepna=params.keepna,
            proxy=params.proxy,
            rounding=params.rounding,
            timeout=params.timeout,
            debug=params.debug
        )
        return TickerResponse(data=dataframe_to_dict(history))
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/dividends", response_model=TickerResponse)
async def get_ticker_dividends(
    symbol: str,
    params: DividendParams = Depends()
):
    """
    Get dividend data for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        dividends = ticker.dividends
        
        if params.start or params.end:
            if params.start:
                dividends = dividends[dividends.index >= params.start]
            if params.end:
                dividends = dividends[dividends.index <= params.end]
                
        return TickerResponse(data=dataframe_to_dict(dividends))
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/splits", response_model=TickerResponse)
async def get_ticker_splits(
    symbol: str,
    params: SplitParams = Depends()
):
    """
    Get stock splits data for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        splits = ticker.splits
        
        if params.start or params.end:
            if params.start:
                splits = splits[splits.index >= params.start]
            if params.end:
                splits = splits[splits.index <= params.end]
                
        return TickerResponse(data=dataframe_to_dict(splits))
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/actions", response_model=TickerResponse)
async def get_ticker_actions(
    symbol: str,
    start: Optional[date] = None,
    end: Optional[date] = None
):
    """
    Get dividend and stock splits data for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        actions = ticker.actions
        
        if start or end:
            if start:
                actions = actions[actions.index >= start]
            if end:
                actions = actions[actions.index <= end]
                
        return TickerResponse(data=dataframe_to_dict(actions))
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/income", response_model=TickerResponse)
async def get_ticker_income_statement(
    symbol: str,
    params: FinancialStatementParams = Depends()
):
    """
    Get income statement data for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        if params.frequency == "quarterly":
            income_stmt = ticker.quarterly_income_stmt
        else:
            income_stmt = ticker.income_stmt
            
        result = {}
        for col in income_stmt.columns:
            result[str(col.date())] = {row: income_stmt[col][row] for row in income_stmt.index}
            
        return TickerResponse(data=result)
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/balance", response_model=TickerResponse)
async def get_ticker_balance_sheet(
    symbol: str,
    params: FinancialStatementParams = Depends()
):
    """
    Get balance sheet data for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        if params.frequency == "quarterly":
            balance = ticker.quarterly_balance_sheet
        else:
            balance = ticker.balance_sheet
            
        result = {}
        for col in balance.columns:
            result[str(col.date())] = {row: balance[col][row] for row in balance.index}
            
        return TickerResponse(data=result)
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/cashflow", response_model=TickerResponse)
async def get_ticker_cashflow(
    symbol: str,
    params: FinancialStatementParams = Depends()
):
    """
    Get cash flow data for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        if params.frequency == "quarterly":
            cashflow = ticker.quarterly_cashflow
        else:
            cashflow = ticker.cashflow
            
        result = {}
        for col in cashflow.columns:
            result[str(col.date())] = {row: cashflow[col][row] for row in cashflow.index}
            
        return TickerResponse(data=result)
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/earnings", response_model=TickerResponse)
async def get_ticker_earnings(
    symbol: str,
    params: FinancialStatementParams = Depends()
):
    """
    Get earnings data for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        earnings = ticker.earnings
        
        return TickerResponse(data=earnings.to_dict())
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/earnings_dates", response_model=TickerResponse)
async def get_ticker_earnings_dates(
    symbol: str,
    params: EarningsDateParams = Depends()
):
    """
    Get earnings dates for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        earnings_dates = ticker.earnings_dates
        
        if earnings_dates is not None:
            return TickerResponse(data=dataframe_to_dict(earnings_dates))
        return TickerResponse(data=[])
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/sustainability", response_model=TickerResponse)
async def get_ticker_sustainability(symbol: str):
    """
    Get sustainability data for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        sustainability = ticker.sustainability
        
        if sustainability is not None:
            return TickerResponse(data=sustainability.to_dict())
        return TickerResponse(data={})
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/recommendations", response_model=TickerResponse)
async def get_ticker_recommendations(symbol: str):
    """
    Get analyst recommendations for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        recommendations = ticker.recommendations
        
        if recommendations is not None:
            return TickerResponse(data=dataframe_to_dict(recommendations))
        return TickerResponse(data=[])
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/news", response_model=TickerResponse)
async def get_ticker_news(symbol: str):
    """
    Get news for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        news = ticker.news
        
        if news:
            return TickerResponse(data=news)
        return TickerResponse(data=[])
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/major_holders", response_model=TickerResponse)
async def get_ticker_major_holders(symbol: str):
    """
    Get major holders for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        holders = ticker.major_holders
        
        if holders is not None:
            return TickerResponse(data=holders.to_dict())
        return TickerResponse(data={})
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/institutional_holders", response_model=TickerResponse)
async def get_ticker_institutional_holders(symbol: str):
    """
    Get institutional holders for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        holders = ticker.institutional_holders
        
        if holders is not None:
            return TickerResponse(data=dataframe_to_dict(holders))
        return TickerResponse(data=[])
    except Exception as e:
        return TickerResponse(success=False, error=str(e))

@router.get("/{symbol}/mutualfund_holders", response_model=TickerResponse)
async def get_ticker_mutualfund_holders(symbol: str):
    """
    Get mutual fund holders for a ticker.
    """
    try:
        ticker = yf.Ticker(symbol)
        holders = ticker.mutualfund_holders
        
        if holders is not None:
            return TickerResponse(data=dataframe_to_dict(holders))
        return TickerResponse(data=[])
    except Exception as e:
        return TickerResponse(success=False, error=str(e)) 