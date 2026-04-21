from bt_api_base.error import ErrorTranslator, UnifiedError, UnifiedErrorCode


class UpbitErrorTranslator(ErrorTranslator):
    ERROR_MAP = {
        "UNAUTHORIZED": (UnifiedErrorCode.INVALID_API_KEY, "Authentication failed"),
        "EXPIRED_ACCESS_KEY": (UnifiedErrorCode.INVALID_API_KEY, "API key expired"),
        "INVALID_QUERY_PAYLOAD": (UnifiedErrorCode.INVALID_PARAMETER, "Invalid request parameters"),
        "JWT_VERIFICATION": (UnifiedErrorCode.INVALID_SIGNATURE, "JWT verification failed"),
        "NO_AUTHORIZATION_IP": (UnifiedErrorCode.PERMISSION_DENIED, "IP not authorized"),
        "NONCE_USED": (UnifiedErrorCode.EXPIRED_TIMESTAMP, "Nonce already used"),
        "TOO_MANY_REQUESTS": (UnifiedErrorCode.RATE_LIMIT_EXCEEDED, "Too many requests"),
        "REQUEST_LIMIT_EXCEEDED": (UnifiedErrorCode.RATE_LIMIT_EXCEEDED, "Request limit exceeded"),
        "INSUFFICIENT_FUNDS_BID": (
            UnifiedErrorCode.INSUFFICIENT_BALANCE,
            "Insufficient funds for buy order",
        ),
        "INSUFFICIENT_FUNDS_ASK": (
            UnifiedErrorCode.INSUFFICIENT_BALANCE,
            "Insufficient funds for sell order",
        ),
        "UNDER_MIN_TOTAL_BID": (UnifiedErrorCode.MINIMUM_NOT_MET, "Below minimum buy amount"),
        "UNDER_MIN_TOTAL_ASK": (UnifiedErrorCode.MINIMUM_NOT_MET, "Below minimum sell amount"),
        "INVALID_MARKET": (UnifiedErrorCode.INVALID_SYMBOL, "Invalid market symbol"),
        "INVALID_PRICE": (UnifiedErrorCode.INVALID_PRICE, "Invalid price"),
        "INVALID_VOLUME": (UnifiedErrorCode.INVALID_VOLUME, "Invalid volume"),
        "ORDER_NOT_FOUND": (UnifiedErrorCode.ORDER_NOT_FOUND, "Order not found"),
        "ORDER_ALREADY_FILLED": (UnifiedErrorCode.ORDER_ALREADY_FILLED, "Order already filled"),
        "ORDER_CANCELLED": (UnifiedErrorCode.ORDER_CANCELLED, "Order cancelled"),
        "DUPLICATE_ORDER": (UnifiedErrorCode.DUPLICATE_ORDER, "Duplicate order"),
        "MARKET_CLOSED": (UnifiedErrorCode.MARKET_CLOSED, "Market is closed"),
        "ORDER_TIMEOUT": (UnifiedErrorCode.ORDER_TIMEOUT, "Order timeout"),
        "MISSING_PARAMETER": (UnifiedErrorCode.MISSING_PARAMETER, "Missing required parameter"),
        "INVALID_PARAMETER": (UnifiedErrorCode.INVALID_PARAMETER, "Invalid parameter value"),
        "INVALID_PARAMETER_TYPE": (UnifiedErrorCode.INVALID_PARAMETER, "Invalid parameter type"),
        "PARAMETER_OUT_OF_RANGE": (UnifiedErrorCode.INVALID_PARAMETER, "Parameter out of range"),
        "INTERNAL_SERVER_ERROR": (UnifiedErrorCode.INTERNAL_ERROR, "Internal server error"),
        "SERVICE_TEMPORARILY_UNAVAILABLE": (
            UnifiedErrorCode.EXCHANGE_OVERLOADED,
            "Service temporarily unavailable",
        ),
        "DATABASE_ERROR": (UnifiedErrorCode.INTERNAL_ERROR, "Database error"),
        "NETWORK_ERROR": (UnifiedErrorCode.NETWORK_TIMEOUT, "Network error"),
    }

    @classmethod
    def translate(cls, raw_error: dict, venue: str) -> UnifiedError | None:
        error_obj = raw_error.get("error", raw_error)

        if isinstance(error_obj, dict):
            error_name = error_obj.get("name", "")
            error_msg = error_obj.get("message", "")

            error_full_msg = f"{error_name}: {error_msg}" if error_name else error_msg

            for error_key, error_data in cls.ERROR_MAP.items():
                if error_key in error_name or error_key in error_full_msg:
                    unified_code, default_msg = error_data
                    if unified_code is None:
                        return None
                    return UnifiedError(
                        code=unified_code,
                        category=cls._get_category(unified_code),
                        venue=venue,
                        message=error_msg or default_msg,
                        original_error=error_full_msg,
                        context={"raw_response": raw_error},
                    )

            if "UNAUTHORIZED" in error_name or "JWT" in error_name:
                return UnifiedError(
                    code=UnifiedErrorCode.INVALID_API_KEY,
                    category=cls._get_category(UnifiedErrorCode.INVALID_API_KEY),
                    venue=venue,
                    message=error_full_msg,
                    original_error=error_full_msg,
                    context={"raw_response": raw_error},
                )
            elif "RATE" in error_name or "TOO_MANY" in error_name:
                return UnifiedError(
                    code=UnifiedErrorCode.RATE_LIMIT_EXCEEDED,
                    category=cls._get_category(UnifiedErrorCode.RATE_LIMIT_EXCEEDED),
                    venue=venue,
                    message=error_full_msg,
                    original_error=error_full_msg,
                    context={"raw_response": raw_error},
                )
            elif "INSUFFICIENT" in error_name or "FUNDS" in error_name:
                return UnifiedError(
                    code=UnifiedErrorCode.INSUFFICIENT_BALANCE,
                    category=cls._get_category(UnifiedErrorCode.INSUFFICIENT_BALANCE),
                    venue=venue,
                    message=error_full_msg,
                    original_error=error_full_msg,
                    context={"raw_response": raw_error},
                )
            elif "INVALID" in error_name:
                return UnifiedError(
                    code=UnifiedErrorCode.INVALID_PARAMETER,
                    category=cls._get_category(UnifiedErrorCode.INVALID_PARAMETER),
                    venue=venue,
                    message=error_full_msg,
                    original_error=error_full_msg,
                    context={"raw_response": raw_error},
                )

            return UnifiedError(
                code=UnifiedErrorCode.INTERNAL_ERROR,
                category=cls._get_category(UnifiedErrorCode.INTERNAL_ERROR),
                venue=venue,
                message=error_full_msg,
                original_error=error_full_msg,
                context={"raw_response": raw_error},
            )

        return super().translate(raw_error, venue)
