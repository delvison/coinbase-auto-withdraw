import os
from coinbase.wallet.client import Client
from cryptotools import Xpub

coinbase_API_key = os.environ.get('COINBASE_API_KEY')
coinbase_API_secret = os.environ.get('COINBASE_API_SECRET')
withdrawal_threshold = int(os.environ.get('WITHDRAWAL_THRESHOLD', 100))
withdrawal_max = int(os.environ.get('WITHDRAWAL_MAX', 3000))

client = Client(coinbase_API_key, coinbase_API_secret)


def get_btc_address():
    addr = os.environ.get('BITCOIN_WALLET')
    if addr is None:
        xpub_addr = os.environ.get('XPUB_ADDRESS')
        key = Xpub.decode(xpub_addr)
        pubkey0 = key/0/0
        addr = pubkey0.address('P2WPKH')

    return str(addr)


def send_btc(bal):
    bal = bal - (bal * 0.01)  # skim some off for covering the fees
    amount = "{:.8f}".format(bal)
    account = client.get_primary_account()
    btc_addr = get_btc_address()
    print(f"[*] sending {bal} to {btc_addr}")
    tx = account.send_money(to=btc_addr,
                            amount=amount,
                            currency='BTC')
    print(tx)

if __name__ == "__main__":
    accounts = client.get_accounts()
    for wallet in accounts.data:
        if str(wallet['name']) == "BTC Wallet":
            usd_bal = float(str(wallet['native_balance']).replace('USD', '').strip())
            bal = float(str(wallet['balance']).replace('BTC', '').strip())

            if usd_bal > withdrawal_threshold:
                if usd_bal > withdrawal_max:
                    cost_basis = usd_bal/bal
                    capped_bal = withdrawal_threshold/cost_basis
                    send_btc(capped_bal)
                else:
                    send_btc(bal)
            else:
                print(f"[*] skipping since ${usd_bal} < ${withdrawal_threshold}")
