#!/usr/bin/python3

##Author : Paranoid Ninja
##Email  : paranoidninja@protonmail.com
##Descr  : Calculate the bitcoin transaction fees to be paid by calculating the exact satoshies per byte value

import requests

n_input = input("[!] Enter number of inputs [Default:1]: ")
if n_input == "":
    n_input = 1
else:
    n_input = int(n_input)
n_output = input("[!] Enter number of output [Default:2]: ")
if n_output == "":
    n_output = 2
else:
    n_output = int(n_output)

print ( "[+] Calculating total size of bytes for the transaction..")
transactionBytes = (n_input*180 + n_output*34 + 10)
print ("[+] Total transaction size in bytes: " + str(transactionBytes))

print ("[+] Fetching the latest Satoshi rates per byte..")
f = requests.get("https://bitcoinfees.earn.com/api/v1/fees/recommended")
satoshiVal = f.json()
counter = 0
for x, y in satoshiVal.items():
    print (str(counter) + ". " + x + ":\t" + str(y) + " Satoshies")
    counter += 1

SelectedSatoshi = int(input("[!] Enter your selection [0,1 or 2]: "))
if SelectedSatoshi == 0:
    Satoshi = satoshiVal["fastestFee"]
    BCoinFeesCalc = (transactionBytes * Satoshi) / 100000000
    BCoinFees = '{0:.10f}'.format(BCoinFeesCalc)
    print ("[+] Total fees to be paid in Bitcoin: " + str(BCoinFees) + " BTC")
elif SelectedSatoshi == 1:
    Satoshi = satoshiVal["halfHourFee"]
    BCoinFeesCalc = (transactionBytes * Satoshi) / 100000000
    BCoinFees = '{0:.10f}'.format(BCoinFeesCalc)
    print ("[+] Total fees to be paid in Bitcoin: " + str(BCoinFees) + " BTC")
elif SelectedSatoshi == 2:
    Satoshi = satoshiVal["hourFee"]
    BCoinFeesCalc = (transactionBytes * Satoshi) / 100000000
    BCoinFees = '{0:.10f}'.format(BCoinFeesCalc)
    print ("[+] Total fees to be paid in Bitcoin: " + str(BCoinFees) + " BTC")
else:
    print ("[-] Invalid Selection!")

