from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class SearchParams(BaseModel):
    query: str = Field(..., description="Search query string")
    limit: Optional[int] = Field(10, description="Number of results to return")
    proxy: Optional[str] = Field(None, description="Proxy server")

class SearchResponse(BaseModel):
    success: bool = True
    data: List[Dict[str, Any]] = []
    count: int = 0
    error: Optional[str] = None 