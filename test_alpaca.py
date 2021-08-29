import alpaca_trade_api as tradeapi

api = tradeapi.REST() #Works as the environment-variables are set

# Get our account information.
account = api.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))

# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')

# Get a list of all active assets.
#active_assets = api.list_assets(status='active')

#Check what exchanges that can be traded
# exchange_types = set()

# for asset in active_assets:
#     exchange_types.add(asset.exchange)

# print(exchange_types)

# Filter the assets down to just those on NASDAQ.
# nasdaq_assets = [a for a in active_assets if a.exchange == 'NASDAQ']
# print(nasdaq_assets)


# Check if AAPL is tradable on the Alpaca platform.
aapl_asset = api.get_asset('AAPL')
if aapl_asset.tradable:
    print('We can trade AAPL.')
else:
    print("GOODDDAMMIT")

# Check if the market is open now.
clock = api.get_clock()
is_open = 'open' if clock.is_open else 'closed'
print(f'The market is {is_open}.')

# Check when the market was open on Dec. 1, 2018
# date = '2018-12-01'
# calendar = api.get_calendar(start=date, end=date)[0]
# print('The market opened at {} and closed at {} on {}.'.format(
#     calendar.open,
#     calendar.close,
#     date
# ))


# Get daily price data for AAPL over the last 5 trading days.
num_days = 365
barset = api.get_barset('AAPL', 'day', limit=num_days)
aapl_bars = barset['AAPL']

# See how much AAPL moved in that timeframe.
week_open = aapl_bars[0].o
week_close = aapl_bars[-1].c
percent_change = (week_close - week_open) / week_open * 100
print(f"AAPL moved {percent_change}% over the last {num_days} days")



# Get a list of all of our positions.
portfolio = api.list_positions()

print(portfolio)
# Print the quantity of shares for each position.
for position in portfolio:
    print(f"{position.qty} shares of {position.symbol}")


# Submit a market order to buy 1 share of Apple at market price
# api.submit_order(
#     symbol='AAPL',
#     qty=1,
#     side='buy',
#     type='market',
#     time_in_force='gtc'
# )

# # Submit a limit order to attempt to sell 1 share of AMD at a
# # particular price ($20.50) when the market opens
# api.submit_order(
#     symbol='AMD',
#     qty=1,
#     side='sell',
#     type='limit',
#     time_in_force='opg',
#     limit_price=20.50
# )


# Get our position in AAPL.
# aapl_position = api.get_position('AAPL')
