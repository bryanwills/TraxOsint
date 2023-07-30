from helpers.utils import *
from lib.colors import *
import random

async def vpnchecker(ip):
    with open("useragents.txt", "r") as user_file:
        user = user_file.read().split('\n')

    url = "https://api.protonmail.ch/vpn/logicals"

    response = await Requests(url, headers={"User-Agent": random.choice(user)}).sender()

    try:
        if ip in response.text:
            output = f"{GREEN}Proton{WHITE} | ✔️ | {WHITE}This IP address is currently affiliated with ProtonVPN.{WHITE}"

        else:
            output =  f"{RED}Proton{WHITE} | ❌ | {WHITE}This IP address is not currently affiliated with ProtonVPN.{WHITE}"
    except Exception:
        output =  f"[-] ProtonRate limit."

    return output