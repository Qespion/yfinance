# YFinance API

A RESTful API for accessing Yahoo Finance data using the yfinance library.

## Features

- Get ticker information, history, dividends, and more
- Access market summaries and movers
- Screen for equities and funds
- Search for securities by name or ticker symbol
- Swagger/OpenAPI documentation included

## API Endpoints

### Ticker Endpoints

- `GET /api/ticker/{symbol}` - Get basic information for a ticker
- `GET /api/ticker/{symbol}/fast_info` - Get fast basic information for a ticker
- `GET /api/ticker/{symbol}/history` - Get historical market data for a ticker
- `GET /api/ticker/{symbol}/dividends` - Get dividend data for a ticker
- `GET /api/ticker/{symbol}/splits` - Get stock splits data for a ticker
- `GET /api/ticker/{symbol}/actions` - Get dividend and stock splits data for a ticker
- `GET /api/ticker/{symbol}/income` - Get income statement data for a ticker
- `GET /api/ticker/{symbol}/balance` - Get balance sheet data for a ticker
- `GET /api/ticker/{symbol}/cashflow` - Get cash flow data for a ticker
- `GET /api/ticker/{symbol}/earnings` - Get earnings data for a ticker
- `GET /api/ticker/{symbol}/earnings_dates` - Get earnings dates for a ticker
- `GET /api/ticker/{symbol}/sustainability` - Get sustainability data for a ticker
- `GET /api/ticker/{symbol}/recommendations` - Get analyst recommendations for a ticker
- `GET /api/ticker/{symbol}/news` - Get news for a ticker
- `GET /api/ticker/{symbol}/major_holders` - Get major holders for a ticker
- `GET /api/ticker/{symbol}/institutional_holders` - Get institutional holders for a ticker
- `GET /api/ticker/{symbol}/mutualfund_holders` - Get mutual fund holders for a ticker

### Market Endpoints

- `GET /api/market/summary` - Get market summary data
- `GET /api/market/movers/gainers` - Get top gainers in the market
- `GET /api/market/movers/losers` - Get top losers in the market
- `GET /api/market/movers/active` - Get most active stocks in the market

### Screener Endpoints

- `POST /api/screener/equity` - Screen for equities based on specified parameters
- `POST /api/screener/fund` - Screen for funds based on specified parameters
- `GET /api/screener/sectors` - Get list of available sectors
- `GET /api/screener/industries` - Get list of available industries

### Search Endpoints

- `GET /api/search` - Search for securities by name or ticker symbol

## Deployment with Coolify

This project is designed to be easily deployed on Coolify. Use the provided Dockerfile for container deployment.

### Coolify Deployment Steps

1. Clone this repository to your Coolify instance
2. Create a new service in Coolify using the Docker build method
3. Point to the repository and use the default Dockerfile
4. Set any necessary environment variables
5. Deploy the service

## Local Development

```bash
# Clone the repository
git clone <repository-url>
cd yfinance-api

# Install dependencies
pip install -r requirements.txt

# Run the API locally
uvicorn app.main:app --reload
```

## API Documentation

Once the API is running, you can access the Swagger documentation at:

- http://localhost:3000/ (local development)
- https://your-coolify-domain/ (Coolify deployment)

## License

MIT 