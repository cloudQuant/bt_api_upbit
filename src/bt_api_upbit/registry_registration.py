from bt_api_base.registry import ExchangeRegistry
from bt_api_upbit.feeds.live_upbit.spot import UpbitRequestDataSpot
from bt_api_upbit.exchange_data import UpbitExchangeDataSpot
from bt_api_base.balance_utils import simple_balance_handler as _upbit_balance_handler


def register_upbit():
    """Register Upbit SPOT to ExchangeRegistry."""
    ExchangeRegistry.register_feed("UPBIT___SPOT", UpbitRequestDataSpot)
    ExchangeRegistry.register_exchange_data("UPBIT___SPOT", UpbitExchangeDataSpot)
    ExchangeRegistry.register_balance_handler("UPBIT___SPOT", _upbit_balance_handler)


register_upbit()
