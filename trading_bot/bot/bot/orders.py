import logging
from binance.enums import *

logger = logging.getLogger(__name__)

def place_market_order(client, symbol, side, quantity):

    logger.info(f"Sending MARKET order: {symbol} {side} {quantity}")

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=FUTURE_ORDER_TYPE_MARKET,
        quantity=quantity
    )

    logger.info(f"Market order response: {order}")

    return order


def place_limit_order(client, symbol, side, quantity, price):

    logger.info(f"Sending LIMIT order: {symbol} {side} {quantity} price={price}")

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=FUTURE_ORDER_TYPE_LIMIT,
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    logger.info(f"Limit order response: {order}")

    return order