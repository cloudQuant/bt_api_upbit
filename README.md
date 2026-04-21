# bt_api_upbit

Upbit exchange plugin for `bt_api`, supporting Spot trading.

## Installation

```bash
pip install bt_api_upbit
```

## Usage

```python
from bt_api_upbit import UpbitRequestDataSpot

feed = UpbitRequestDataSpot(public_key="your_key", private_key="your_secret")
ticker = feed.get_ticker("KRW-BTC")
```

## Architecture

```
bt_api_upbit/
├── exchange_data/         # Exchange configuration and REST/WSS paths
├── errors/                # Error translator
├── tickers/               # Ticker data container
├── feeds/live_upbit/      # REST API implementation
├── containers/            # Data containers (balance, order)
└── plugin.py              # PluginInfo registration
```