from Day4 import AdventCoin

coin = AdventCoin()

while True:
    if coin.new_hash().startswith("00000"):
        print "Minimum number is", coin.counter
        break
