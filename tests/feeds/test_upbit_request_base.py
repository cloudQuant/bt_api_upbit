from bt_api_base.containers.requestdatas.request_data import RequestData

from bt_api_upbit.feeds.live_upbit.request_base import UpbitRequestData


def test_upbit_request_allows_missing_extra_data(monkeypatch) -> None:
    request_data = UpbitRequestData(
        public_key="public-key",
        private_key="secret-key",
        exchange_name="UPBIT___SPOT",
    )

    monkeypatch.setattr(
        request_data,
        "http_request",
        lambda method, url, headers, body, timeout: [{"market": "KRW-BTC"}],
    )

    result = request_data.request("GET /v1/market/all", is_sign=False)

    assert isinstance(result, RequestData)
    assert result.get_extra_data() == {}
    assert result.get_input_data() == [{"market": "KRW-BTC"}]
