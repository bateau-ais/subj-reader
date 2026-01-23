import argparse
import asyncio
import logging

from almanach import AlmanachSubscriber
from rich.logging import RichHandler
from rich import print_json
from rich.console import Console
from uuid import uuid4

log = logging.getLogger(__name__)


def main():
    argparser = argparse.ArgumentParser(
        prog="subj-reader",
        description=(
            "Subscribe to one or more Almanach topics and log every received message."
        ),
        epilog=(
            "Examples:\n"
            "  subj-reader some.topic\n"
            "  subj-reader some.topic another.topic\n"
            "  subj-reader 'nats://127.0.0.1/raw_ais.*' --key=msg-uuid\n"
            "\n"
            "Notes:\n"
            "  - NATS wildcards are supported (e.g. raw_ais.* or raw_ais.>)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    argparser.add_argument(
        "topics",
        nargs="+",
        metavar="TOPIC",
        help=(
            "One or more topic names to subscribe to. Supports NATS wildcards like '*' and '>'."
        ),
        type=str,
    )
    argparser.add_argument(
        "--key",
        default="msg_uuid",
        type=str,
        help=(
            "Reserved for future filtering/formatting; currently unused (default: msg_uuid)."
        ),
    )
    args = argparser.parse_args().__dict__

    app = AlmanachSubscriber()

    topics: dict[str, str] = {str(uuid4()): [x] for x in args["topics"]}

    @app.subscribe(**topics, validator=lambda x: x, key=args["key"])
    def handler(msg):
        print_json(data=msg)

    asyncio.run(app.run())


if __name__ == "__main__":
    console = Console(stderr=True)
    logging.basicConfig(level="INFO", handlers=[RichHandler(console=console)])
    main()
