import json
import sys
import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

p = json.dumps(response.json(), indent=2)

json_dict = json.loads(p)
# json.loads converts the json data into a python dictionary
btcusd = json_dict['bpi']['USD']['rate_float']
btcusd2 = float(btcusd)
# source: (https://stackoverflow.com/questions/12788217/how-to-extract-a-single-value-from-json-response)

try:
    x = float(sys.argv[1])
    y = x*btcusd2
#    z = format(y, ".4f")
#    print(f"${z}")
    print(f"$""{:,}".format(y, ".4f"))

except IndexError:
    sys.exit("Missing command-line argument")
except requests.RequestException:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")