from __future__ import annotations

from bt_api_upbit.feeds.live_upbit.request_base import UpbitRequestData


class UpbitRequestDataSpot(UpbitRequestData):
    def get_exchange_info(self, extra_data=None, **kwargs):
        path, params, extra_data = self._get_exchange_info(extra_data=extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data, is_sign=False)

    async def async_get_exchange_info(self, extra_data=None, **kwargs):
        path, params, extra_data = self._get_exchange_info(extra_data=extra_data, **kwargs)
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=False)
        self.async_callback(rd)
        return rd

    def get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra_data = self._get_tick(symbol, extra_data=extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data, is_sign=False)

    async def async_get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra_data = self._get_tick(symbol, extra_data=extra_data, **kwargs)
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=False)
        self.async_callback(rd)
        return rd

    def get_ticker(self, symbol, extra_data=None, **kwargs):
        return self.get_tick(symbol, extra_data=extra_data, **kwargs)

    async def async_get_ticker(self, symbol, extra_data=None, **kwargs):
        return await self.async_get_tick(symbol, extra_data=extra_data, **kwargs)

    def get_depth(self, symbol, count=50, extra_data=None, **kwargs):
        path, params, extra_data = self._get_depth(
            symbol, count=count, extra_data=extra_data, **kwargs
        )
        return self.request(path, params=params, extra_data=extra_data, is_sign=False)

    async def async_get_depth(self, symbol, count=50, extra_data=None, **kwargs):
        path, params, extra_data = self._get_depth(
            symbol, count=count, extra_data=extra_data, **kwargs
        )
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=False)
        self.async_callback(rd)
        return rd

    def get_kline(self, symbol, period="1h", count=200, extra_data=None, **kwargs):
        path, params, extra_data = self._get_kline(
            symbol, period=period, count=count, extra_data=extra_data, **kwargs
        )
        return self.request(path, params=params, extra_data=extra_data, is_sign=False)

    async def async_get_kline(self, symbol, period="1h", count=200, extra_data=None, **kwargs):
        path, params, extra_data = self._get_kline(
            symbol, period=period, count=count, extra_data=extra_data, **kwargs
        )
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=False)
        self.async_callback(rd)
        return rd

    def get_trade_history(self, symbol, count=50, extra_data=None, **kwargs):
        path, params, extra_data = self._get_trade_history(
            symbol, count=count, extra_data=extra_data, **kwargs
        )
        return self.request(path, params=params, extra_data=extra_data, is_sign=False)

    async def async_get_trade_history(self, symbol, count=50, extra_data=None, **kwargs):
        path, params, extra_data = self._get_trade_history(
            symbol, count=count, extra_data=extra_data, **kwargs
        )
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=False)
        self.async_callback(rd)
        return rd

    def get_trades(self, symbol, count=50, extra_data=None, **kwargs):
        return self.get_trade_history(symbol, count=count, extra_data=extra_data, **kwargs)

    async def async_get_trades(self, symbol, count=50, extra_data=None, **kwargs):
        return await self.async_get_trade_history(
            symbol, count=count, extra_data=extra_data, **kwargs
        )

    def make_order(
        self, symbol, size, price=None, order_type="bid-limit", extra_data=None, **kwargs
    ):
        path, body, extra_data = self._make_order(
            symbol, size, price=price, order_type=order_type, extra_data=extra_data, **kwargs
        )
        return self.request(path, body=body, extra_data=extra_data, is_sign=True)

    async def async_make_order(
        self, symbol, size, price=None, order_type="bid-limit", extra_data=None, **kwargs
    ):
        path, body, extra_data = self._make_order(
            symbol, size, price=price, order_type=order_type, extra_data=extra_data, **kwargs
        )
        rd = await self.async_request(path, body=body, extra_data=extra_data, is_sign=True)
        self.async_callback(rd)
        return rd

    def cancel_order(self, symbol=None, order_id=None, extra_data=None, **kwargs):
        path, params, extra_data = self._cancel_order(
            symbol=symbol, order_id=order_id, extra_data=extra_data, **kwargs
        )
        return self.request(path, params=params, extra_data=extra_data, is_sign=True)

    async def async_cancel_order(self, symbol=None, order_id=None, extra_data=None, **kwargs):
        path, params, extra_data = self._cancel_order(
            symbol=symbol, order_id=order_id, extra_data=extra_data, **kwargs
        )
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=True)
        self.async_callback(rd)
        return rd

    def query_order(self, symbol=None, order_id=None, extra_data=None, **kwargs):
        path, params, extra_data = self._query_order(
            symbol=symbol, order_id=order_id, extra_data=extra_data, **kwargs
        )
        return self.request(path, params=params, extra_data=extra_data, is_sign=True)

    async def async_query_order(self, symbol=None, order_id=None, extra_data=None, **kwargs):
        path, params, extra_data = self._query_order(
            symbol=symbol, order_id=order_id, extra_data=extra_data, **kwargs
        )
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=True)
        self.async_callback(rd)
        return rd

    def get_open_orders(self, symbol=None, extra_data=None, **kwargs):
        path, params, extra_data = self._get_open_orders(
            symbol=symbol, extra_data=extra_data, **kwargs
        )
        return self.request(path, params=params, extra_data=extra_data, is_sign=True)

    async def async_get_open_orders(self, symbol=None, extra_data=None, **kwargs):
        path, params, extra_data = self._get_open_orders(
            symbol=symbol, extra_data=extra_data, **kwargs
        )
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=True)
        self.async_callback(rd)
        return rd

    def get_deals(self, symbol=None, extra_data=None, **kwargs):
        path, params, extra_data = self._get_deals(symbol=symbol, extra_data=extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data, is_sign=True)

    async def async_get_deals(self, symbol=None, extra_data=None, **kwargs):
        path, params, extra_data = self._get_deals(symbol=symbol, extra_data=extra_data, **kwargs)
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=True)
        self.async_callback(rd)
        return rd

    def get_account(self, extra_data=None, **kwargs):
        path, params, extra_data = self._get_account(extra_data=extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data, is_sign=True)

    async def async_get_account(self, extra_data=None, **kwargs):
        path, params, extra_data = self._get_account(extra_data=extra_data, **kwargs)
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=True)
        self.async_callback(rd)
        return rd

    def get_balance(self, extra_data=None, **kwargs):
        path, params, extra_data = self._get_balance(extra_data=extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data, is_sign=True)

    async def async_get_balance(self, extra_data=None, **kwargs):
        path, params, extra_data = self._get_balance(extra_data=extra_data, **kwargs)
        rd = await self.async_request(path, params=params, extra_data=extra_data, is_sign=True)
        self.async_callback(rd)
        return rd
