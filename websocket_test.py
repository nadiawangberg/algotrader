import alpaca_trade_api as tradeapi
import threading
import os

#tutorial - https://algotrading101.com/learn/alpaca-trading-api-guide/
#docs - https://alpaca.markets/docs/api-documentation/api-v2/streaming/#common-events

api = tradeapi.REST() #Works as the environment-variables are set
account = api.get_account()
print(account)

conn = tradeapi.stream2.StreamConn(os.environ["APCA_API_KEY_ID"], os.environ["APCA_API_SECRET_KEY"], os.environ["APCA_API_BASE_URL"])

@conn.on(r'^account_updates$')
async def on_account_updates(conn, channel, account):
    print('account', account)

@conn.on(r'^trade_updates$')
async def on_trade_updates(conn, channel, trade):
    print('trade', trade)

def ws_start():
	conn.run(['account_updates', 'trade_updates'])

#start WebSocket in a thread
ws_thread = threading.Thread(target=ws_start, daemon=True)
ws_thread.start()