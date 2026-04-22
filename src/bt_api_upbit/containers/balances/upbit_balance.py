from __future__ import annotations

import json
import time

from bt_api_base.containers.balances.balance import BalanceData
from bt_api_base.functions.utils import from_dict_get_float, from_dict_get_string
from bt_api_base.logging_factory import get_logger

logger = get_logger("container")


class UpbitBalanceData(BalanceData):
    def __init__(self, balance_info, currency, asset_type, has_been_json_encoded=False) -> None:
        super().__init__(balance_info, has_been_json_encoded)
        self.exchange_name = "UPBIT"
        self.local_update_time = time.time()
        self.currency = currency
        self.asset_type = asset_type
        self.balance_data = balance_info if has_been_json_encoded else None
        self.balance = None
        self.locked = None
        self.avg_buy_price = None
        self.avg_buy_price_modified = None
        self.unit_currency = None
        self.currency_name = None
        self.status = None
        self.available = None
        self.all_data: dict | None = None
        self.has_been_init_data = False

    def init_data(self) -> None:
        try:
            if not self.has_been_json_encoded:
                self.balance_data = json.loads(self.raw_data)

            self.balance = from_dict_get_float(self.balance_data, "balance")
            self.locked = from_dict_get_float(self.balance_data, "locked")
            self.avg_buy_price = from_dict_get_float(self.balance_data, "avg_buy_price")
            self.avg_buy_price_modified = from_dict_get_string(
                self.balance_data,
                "avg_buy_price_modified",
            )

            self.currency_name = from_dict_get_string(self.balance_data, "currency_name")
            self.unit_currency = from_dict_get_string(self.balance_data, "unit_currency")

            self.status = from_dict_get_string(self.balance_data, "status")

            self.available = (
                self.balance - self.locked
                if self.balance and self.locked is not None
                else self.balance
            )

            self.has_been_init_data = True

        except Exception as e:
            logger.error(f"Error initializing Upbit balance data: {e}", exc_info=True)

    def get_all_data(self):
        if self.all_data is None:
            self.all_data = {
                "exchange_name": self.exchange_name,
                "currency": self.currency,
                "asset_type": self.asset_type,
                "local_update_time": self.local_update_time,
                "balance": self.balance,
                "locked": self.locked,
                "available": self.available,
                "avg_buy_price": self.avg_buy_price,
                "avg_buy_price_modified": self.avg_buy_price_modified,
                "currency_name": self.currency_name,
                "unit_currency": self.unit_currency,
                "status": self.status,
            }
        return self.all_data

    def total_balance(self):
        return self.balance

    def available_balance(self):
        return self.available

    def locked_balance(self):
        return self.locked

    def __str__(self) -> str:
        if not self.has_been_init_data:
            self.init_data()

        return (
            f"UpbitBalance(currency={self.currency}, "
            f"total={self.balance:.8f}, "
            f"available={self.available:.8f}, "
            f"locked={self.locked:.8f})"
        )
