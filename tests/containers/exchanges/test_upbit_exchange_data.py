"""Tests for UpbitExchangeData container."""

from __future__ import annotations

from bt_api_upbit.exchange_data import UpbitExchangeData


class TestUpbitExchangeData:
    """Tests for UpbitExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = UpbitExchangeData()

        assert exchange.exchange_name == "UPBIT___SPOT"
