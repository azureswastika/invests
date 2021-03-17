import websocket


class Streaming:
    websocket.enableTrace(True)

    def __init__(self, token: str) -> None:
        """
        Args:
            token (str): Api key from https://finnhub.io
        """
        self.token = token
        self.ws = websocket.WebSocketApp(
            "wss://ws.finnhub.io?token=" + token,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )

    def run(self):
        """Run websocket"""
        self.ws.run_forever()

    def on_open(self, ws):
        """On websocket open"""

    def on_message(self, ws, message):
        """On websocket message"""

    def on_error(self, ws, error):
        """On websocket error"""

    def on_close(self, ws):
        """On websocket close"""


if __name__ == "__main__":
    from os import environ

    stream = Streaming(environ.get("TOKEN"))
    stream.run()
