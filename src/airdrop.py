import os
import json
from log import loggingSetting
from ut import pushaction, unlock, getAccounts, runPool, buyram

logger = loggingSetting("airdrop")


def main(password):
    pass

    # for i in x[1:]:
    # print(pushaction("betdicetoken", "signup", [i, "1000.0000 DICE"], i))  # 1000dice
    # print(
    #     pushaction("xxxsevensxxx", "signup", [i, "10000.0000 SEVEN"], i)  # 10000 SEVEN
    # )
    # print(pushaction("efinitysicbo", "claim", [i], i))  # 100 CHIPS
    # print(pushaction("roulettespin", "login", [i, "gy2dgmztgqge"], i))
    # print(pushaction("efinitychips", "claim", [i, "gy2dgmztgqge"], i))
    # print(pushaction("grandpacoins", "mine", [i, "4,BTC", "gy2dgmztgqge"], i))
    # print(pushaction("grandpacoins", "mine", [i, "4,ETH", "gy2dgmztgqge"], i))
    # print(pushaction("grandpacoins", "mine", [i, "4,DOGE", "gy2dgmztgqge"], i))
    # print(pushaction("poormantoken", "signup", [i, "0.0000 POOR"], i))
    # print(pushaction("trybenetwork", "claim", [i], i))
    # print(pushaction("wizznetwork1", "signup", [i, "0.0000 WIZZ"], i))


if __name__ == "__main__":
    password = "1"
    unlock(password)
    accounts = getAccounts()

    def run(i):
        print(pushaction("grandpacoins", "mine", [i, "4,BTC", "gy2dgmztgqge"], i))
        print(pushaction("grandpacoins", "mine", [i, "4,ETH", "gy2dgmztgqge"], i))
        print(pushaction("grandpacoins", "mine", [i, "4,DOGE", "gy2dgmztgqge"], i))
        # print(pushaction("eosenbpocket", "signup", [i, "1000.0001 ENB", i], i))
        # t = pushaction("eoscubetoken", "signup", [i, "0.0000 CUBE"], i)
        # print(t)

        # t = pushaction("eosindiegame", "claim", [i, "100.0000 IGC"], i)
        # if b"you have already signed up" not in t:
        #     print(t)
        # if b"has insufficient ram" in t:
        #     buyram("gy2dgmztgqge", i, 2)
        #     print(pushaction("eosindiegame", "claim", ["100.0000 IGC", i], i))

    runPool(run, accounts)
    # run("gy2dgmztgqge")
