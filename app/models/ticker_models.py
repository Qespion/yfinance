from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime, date

class HistoryParams(BaseModel):
    period: Optional[str] = Field("1mo", description="Data period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)")
    interval: Optional[str] = Field("1d", description="Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)")
    start: Optional[date] = Field(None, description="Start date in YYYY-MM-DD format")
    end: Optional[date] = Field(None, description="End date in YYYY-MM-DD format")
    prepost: Optional[bool] = Field(False, description="Include Pre and Post market data")
    auto_adjust: Optional[bool] = Field(True, description="Adjust all OHLC automatically")
    back_adjust: Optional[bool] = Field(False, description="Back-adjust data to match prices with auto_adjust")
    repair: Optional[bool] = Field(False, description="Attempt repair of missing data")
    keepna: Optional[bool] = Field(False, description="Keep NaN values")
    proxy: Optional[str] = Field(None, description="Proxy server")
    rounding: Optional[bool] = Field(False, description="Round values to 2 decimal places")
    timeout: Optional[float] = Field(None, description="Timeout in seconds")
    debug: Optional[bool] = Field(False, description="Debug mode")

class DividendParams(BaseModel):
    start: Optional[date] = Field(None, description="Start date in YYYY-MM-DD format")
    end: Optional[date] = Field(None, description="End date in YYYY-MM-DD format")

class SplitParams(BaseModel):
    start: Optional[date] = Field(None, description="Start date in YYYY-MM-DD format")
    end: Optional[date] = Field(None, description="End date in YYYY-MM-DD format")

class FinancialStatementParams(BaseModel):
    frequency: Optional[str] = Field("yearly", description="Statement frequency (yearly, quarterly)")
    proxy: Optional[str] = Field(None, description="Proxy server")
    as_dict: Optional[bool] = Field(False, description="Return as dictionary")

class EarningsDateParams(BaseModel):
    limit: Optional[int] = Field(12, description="Number of earnings dates to show")
    proxy: Optional[str] = Field(None, description="Proxy server")

class TickerResponse(BaseModel):
    success: bool = True
    data: Dict[str, Any] = {}
    error: Optional[str] = None 