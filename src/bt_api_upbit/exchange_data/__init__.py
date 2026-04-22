from bt_api_base.containers.exchanges.exchange_data import ExchangeData

_FALLBACK_REST_PATHS = {
    "get_exchange_info": "GET /v1/market/all",
    "get_tick": "GET /v1/ticker",
    "get_depth": "GET /v1/orderbook",
    "get_trades": "GET /v1/trades/ticks",
    "get_kline_minutes": "GET /v1/candles/minutes/{unit}",
    "get_kline_days": "GET /v1/candles/days",
    "get_kline_weeks": "GET /v1/candles/weeks",
    "get_kline_months": "GET /v1/candles/months",
    "get_account": "GET /v1/accounts",
    "get_balance": "GET /v1/accounts",
    "make_order": "POST /v1/orders",
    "cancel_order": "DELETE /v1/order",
    "query_order": "GET /v1/order",
    "get_open_orders": "GET /v1/orders",
    "get_api_keys": "GET /v1/api_keys",
    "get_wallet_status": "GET /v1/status/wallet",
}


class UpbitExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "UPBIT___SPOT"
        self.rest_url = "https://api.upbit.com"
        self.wss_url = "wss://api.upbit.com/websocket/v1"
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1",
            "3m": "3",
            "5m": "5",
            "10m": "10",
            "15m": "15",
            "30m": "30",
            "1h": "60",
            "2h": "120",
            "4h": "240",
            "6h": "360",
            "8h": "480",
            "12h": "720",
            "1d": "D",
            "3d": "3D",
            "1w": "W",
            "1M": "M",
        }
        self.reverse_kline_periods = {v: k for k, v in self.kline_periods.items()}
        self.legal_currency = ["KRW", "USDT", "BTC", "ETH"]


class UpbitExchangeDataSpot(UpbitExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"

    def get_symbol(self, symbol: str) -> str:
        return symbol

    def get_period(self, key: str) -> str:
        return self.kline_periods.get(key, key)

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            msg = f"[{self.exchange_name}] REST path not found: {key}"
            raise ValueError(msg)
        return self.rest_paths[key]

    def get_wss_path(self, channel, symbol: str | None = None, **kwargs) -> str:
        tpl = self.wss_paths.get(channel, "")
        if symbol and tpl:
            return tpl.replace("{market}", symbol)
        return tpl
