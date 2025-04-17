from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class MarketSummaryParams(BaseModel):
    lang: Optional[str] = Field("en", description="Language for the market summary")
    region: Optional[str] = Field("US", description="Region for the market summary")
    proxy: Optional[str] = Field(None, description="Proxy server")

class MarketMoversParams(BaseModel):
    count: Optional[int] = Field(5, description="Number of movers to return")
    lang: Optional[str] = Field("en", description="Language for the market movers")
    region: Optional[str] = Field("US", description="Region for the market movers")
    proxy: Optional[str] = Field(None, description="Proxy server")

class MarketResponse(BaseModel):
    success: bool = True
    data: Dict[str, Any] = {}
    error: Optional[str] = None 