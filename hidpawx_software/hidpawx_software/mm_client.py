import json
import websocket
from .hidpawx_secrets import WS_ENDPOINT, DEVICE_TYPE, DEVICE_NAME, API_KEY

class MMAccessClient(websocket.WebSocketApp):

    def __init__(self):
        url = f"{WS_ENDPOINT}/{DEVICE_TYPE}/{DEVICE_NAME}"
        print(f"Using URL {url}")
        super().__init__(
            url=url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )

    def on_message(self, ws: websocket.WebSocketApp, message: str):
        print(f"Called message {message}")

    def on_close(self, data: websocket.WebSocketApp, status_code: int, message: str):
        print(f"Called close with status code {status_code}, {message}")

    def on_error(self, ws: websocket.WebSocketApp, error: str):
        print(f"Error: {error}")

    def on_open(self, data: websocket.WebSocketApp):
        print(f"Opening connection to {self.url}, sending auth")
        auth_packet = {
            "command": "authenticate",
            "secret_key": API_KEY
        }
        self.send(json.dumps(auth_packet))
