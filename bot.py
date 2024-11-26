import requests
import json
import os
from colorama import *
from datetime import datetime, timedelta
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class Diamore:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'en,en-US;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'api.diamore.co',
            'Origin': 'https://app.diamore.co',
            'Pragma': 'no-cache',
            'Referer': 'https://app.diamore.co/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Diamore.co - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
        
    def user_visit(self, query: str, retries=3):
        url = "https://api.diamore.co/user/visit"
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
        
    def user_info(self, query: str, retries=3):
        url = "https://api.diamore.co/user"
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def daily_rewards(self, query: str, retries=3):
        url = "https://api.diamore.co/daily/rewards"
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def claim_daily(self, query: str, retries=3):
        url = "https://api.diamore.co/daily/claim"
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                if response.status_code == 429:
                    return None
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def refferal_recruits(self, query: str, retries=3):
        url = "https://api.diamore.co/referral/recruits/"
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def claim_refferal(self, query: str, retries=3):
        url = "https://api.diamore.co/referral/claim"
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                if response.status_code == 429:
                    return None
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def claim_taps(self, query: str, retries=3):
        url = "https://api.diamore.co/taps/claim"
        data = json.dumps({'amount':'100000'})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.post(url, headers=self.headers, data=data, timeout=10)
                if response.status_code == 429:
                    return None
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def ads_info(self, query: str, retries=3):
        url = "https://api.diamore.co/ads"
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                if response.status_code == 429:
                    return None
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def watch_ads(self, query: str, retries=3):
        url = "https://api.diamore.co/ads/watch"
        data = json.dumps({'type':'adsgram'})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.post(url, headers=self.headers, data=data, timeout=10)
                if response.status_code == 429:
                    return None
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def quests(self, query: str, retries=3):
        url = "https://api.diamore.co/quests"
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def finish_quests(self, query: str, quest_name: str, retries=3):
        url = "https://api.diamore.co/quests/finish"
        data = json.dumps({'questName':quest_name})
        self.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Token {query}'
        })

        attempt = 0
        while attempt < retries:
            try:
                response = self.session.post(url, headers=self.headers, data=data, timeout=10)
                if response.status_code in [400, 404, 409]:
                    return response.json()
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, requests.ConnectionError) as e:
                print(
                    f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT}Request Timeout.{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} Retrying {attempt+1}/{retries} {Style.RESET_ALL}",
                    end="\r",
                    flush=True
                )
            attempt += 1
            time.sleep(2)

        return None
    
    def process_query(self, query: str):
        visit = self.user_visit(query)
        if not visit:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Query Id Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if visit:
            user = self.user_info(query)
            if not user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.YELLOW+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} Diamore Server May Down {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                return
            
            if user:
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['first_name']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['balance']} 💎 {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['pinkBalance']} 💗 {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(1)

                check_in = self.daily_rewards(query)
                if check_in:
                    claim = self.claim_daily(query)
                    if claim:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-in{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {check_in['current']} 💎 {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-in{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Check-in{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                refferal = self.refferal_recruits(query)
                if refferal:
                    reward = refferal['totalAvailableBonuses']
                    if reward > 0:
                        claim = self.claim_refferal(query)
                        if claim:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {reward} 💎 {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} No Available Rewards to Claim {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                taps = self.claim_taps(query)
                if taps:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} No Available Attempt {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                ads = self.ads_info(query)
                if ads:
                    count = ads['available']
                    if count > 0 :
                        while count > 0:
                            watch_ads = self.watch_ads(query)
                            if watch_ads:
                                count -= 1
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Watch Ads{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Count{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {count} Left {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                time.sleep(1)

                                taps = self.claim_taps(query)
                                if taps:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT} Is Success {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Tap Tap{Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT} No Available Attempt {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                            
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Watch Ads{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Success {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                break

                            time.sleep(1)

                        if count == 0:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Watch Ads{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} No Available Attempt {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                            
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Watch Ads{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} No Available Attempt {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Ads{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

                quests = self.quests(query)
                if quests:
                    for quest in quests:
                        quest_name = quest['name']
                        type_reward = quest['targetBalance']
                        reward = quest['bonusClicks']

                        if type_reward == "balance":
                            reward_icon = "💎"
                        elif type_reward == "pinkBalance":
                            reward_icon = "💗"
                        else:
                            reward_icon = ""

                        if quest:
                            finish = self.finish_quests(query, quest_name)
                            if finish:
                                message = finish['message']
                                if message == 'Quest marked as finished':
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {quest_name} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {reward} {reward_icon} {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                elif message == 'Quest can not be completed anymore':
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {quest_name} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}Is Already Completed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {quest_name} {Style.RESET_ALL}"
                                        f"{Fore.RED+Style.BRIGHT}Isn't Completed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Diamore.co - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    bot = Diamore()
    bot.main()
    