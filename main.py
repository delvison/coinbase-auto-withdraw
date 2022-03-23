import os
from coinbase.wallet.client import Client

coinbase_API_key = os.environ.get('COINBASE_API_KEY')
coinbase_API_secret = os.environ.get('COINBASE_API_SECRET')
withdrawal_threshold = int(os.environ.get('WITHDRAWAL_THRESHOLD', 100))

client = Client(coinbase_API_key, coinbase_API_secret)

def send_btc(bal):
    bal = bal - (bal * 0.01)  # skim some off for covering the fees
    account = client.get_primary_account()
    btc_wallet = os.environ.get('BITCOIN_WALLET')
    print(f"sending {bal} to {btc_wallet}")
    tx = account.send_money(to=btc_wallet,
                            amount="{:.8f}".format(bal),
                            currency='BTC')
    print(tx)

if __name__ == "__main__":
    accounts = client.get_accounts()
    for wallet in accounts.data:
        if str(wallet['name']) == "BTC Wallet":
            usd_bal = float(str(wallet['native_balance']).replace('USD', '').strip())
            bal = float(str(wallet['balance']).replace('BTC', '').strip())

            if usd_bal > withdrawal_threshold:
                send_btc(bal)
            else:
                print(f"Skipping since ${usd_bal} < ${withdrawal_threshold}")
