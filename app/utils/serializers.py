import pandas as pd
import numpy as np
import json
from datetime import date, datetime
from decimal import Decimal

class JSONEncoder(json.JSONEncoder):
    """Extended JSON encoder to handle pandas and numpy types."""
    
    def default(self, obj):
        if isinstance(obj, (np.integer, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float64)):
            return float(obj)
        elif isinstance(obj, np.bool_):
            return bool(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, pd.Series):
            return obj.to_dict()
        elif isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        elif isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient="records")
        elif isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif pd.isna(obj):
            return None
        return super().default(obj)

def json_serialize(obj):
    """Serialize object to JSON-compatible format."""
    return json.dumps(obj, cls=JSONEncoder)

def dataframe_to_dict(df, orient="records"):
    """Convert pandas DataFrame to dict."""
    if isinstance(df, pd.DataFrame):
        # Reset index to make it a column
        df_reset = df.reset_index()
        
        # Convert any potential non-serializable objects
        for col in df_reset.columns:
            if df_reset[col].dtype == 'datetime64[ns]':
                df_reset[col] = df_reset[col].dt.strftime('%Y-%m-%d %H:%M:%S')
            elif df_reset[col].dtype == 'object':
                df_reset[col] = df_reset[col].apply(lambda x: str(x) if x is not None else None)
                
        return df_reset.to_dict(orient=orient)
    return df 