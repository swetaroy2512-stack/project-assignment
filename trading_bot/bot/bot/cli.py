import argparse
import logging

from bot.client import create_client
from bot.orders import place_market_order, place_limit_order
from bot.validators import *
from bot.logging_config import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

def main():

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)

        client = create_client()

        print("\nOrder Request Summary")
        print("----------------------")
        print("Symbol:", args.symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.quantity)

        if args.type == "LIMIT":
            print("Price:", args.price)

        if args.type == "MARKET":

            order = place_market_order(
                client,
                args.symbol,
                args.side,
                args.quantity
            )

        else:

            order = place_limit_order(
                client,
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\nOrder Response")
        print("----------------------")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))

        print("\nSUCCESS: Order placed successfully")

    except Exception as e:

        logger.error(str(e))
        print("\nERROR:", str(e))


if __name__ == "__main__":
    main()