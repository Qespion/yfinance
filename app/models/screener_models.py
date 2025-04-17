from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class EquityScreenerParams(BaseModel):
    market_cap_min: Optional[float] = Field(None, description="Minimum market cap")
    market_cap_max: Optional[float] = Field(None, description="Maximum market cap")
    dividend_yield_min: Optional[float] = Field(None, description="Minimum dividend yield")
    dividend_yield_max: Optional[float] = Field(None, description="Maximum dividend yield")
    sector: Optional[str] = Field(None, description="Sector filter")
    industry: Optional[str] = Field(None, description="Industry filter")
    country: Optional[str] = Field(None, description="Country filter")
    exchange: Optional[str] = Field(None, description="Exchange filter")
    limit: Optional[int] = Field(25, description="Number of results to return")
    offset: Optional[int] = Field(0, description="Offset for pagination")

class FundScreenerParams(BaseModel):
    category: Optional[str] = Field(None, description="Fund category")
    fund_family: Optional[str] = Field(None, description="Fund family/provider")
    expense_ratio_min: Optional[float] = Field(None, description="Minimum expense ratio")
    expense_ratio_max: Optional[float] = Field(None, description="Maximum expense ratio")
    net_assets_min: Optional[float] = Field(None, description="Minimum net assets")
    net_assets_max: Optional[float] = Field(None, description="Maximum net assets")
    limit: Optional[int] = Field(25, description="Number of results to return")
    offset: Optional[int] = Field(0, description="Offset for pagination")

class ScreenerResponse(BaseModel):
    success: bool = True
    data: Dict[str, Any] = {}
    count: int = 0
    error: Optional[str] = None 