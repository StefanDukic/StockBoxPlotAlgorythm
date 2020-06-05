import websocket, json

def on_open(ws):
    print("opened connection")

    subscribe_messsage = {
        "type": "subscribe",
        "channels": [
            {
                "name": "ticker",
                "product_ids": [
                    "BTC-USD"
                ]
            }
        ]

    }

    ws.send(json.dumps(subscribe_messsage))

def on_message(ws, message):
    print("received message")
    print(json.loads(message))

socket = "wss://ws-feed.pro.coinbase.com"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()