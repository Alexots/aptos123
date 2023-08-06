
import requests, time
from selenium import webdriver
import random
from multiprocessing import Process
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


ident_follow = ['CharlesXAdkins', 'rgelash', 'dport_apt', 'rpranav', 'alinush407', 'aptoskent', 'wintertoro', 'sherry_apt', 'aptosnames', 'PetraWallet', 'AptosLabs', 'SashaSpiegelman', 'jdhodgkins', 'wgrieskamp', 'rustielin', 'bowen_aptos', 'david_wolinsky', 'neilhar_', 'maxpunger', 'austinvirts', 'Greg_Nazario', 'capcap_max', 'AveryChing', 'moshaikhs', 'aptAlix', 'sitalkedia', 'HC_Xie__', 'aptos_ape', 'zacharyr0th', 'aptosmatt', 'valebrent']


with open('profiles.txt') as file:
    profiles_ads = file.readlines()

if len(profiles_ads) == 0:
    raise Exception('profiles are empty')

for i,v in enumerate(profiles_ads):
    profiles_ads[i] = profiles_ads[i].replace('\n','')
    # profiles_ads[i] = v.replace('\n', ' ')
    # profiles_ads[i] = v.replace(' ','')

print(profiles_ads)




#settings

sleep_from = 10
sleep_to = 20

link_to_go = 'https://twitter.com/intent/follow?screen_name='

button_follow_selector = "//*[@data-testid='confirmationSheetConfirm']"

def start(profile):
    bad = []
    # if True:
    try:
        open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + profile
        resp = requests.get(open_url).json()
        service = Service(executable_path=resp["data"]["webdriver"])
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except:
        print("Не могу подключиться к ads и достать driver")


    for i in ident_follow:
        try:
            driver.get(link_to_go+i)
            time.sleep(random.randint(15,20))
            btn = driver.find_element(By.XPATH,button_follow_selector)
            btn.click()
            time.sleep(random.randint(sleep_from,sleep_to))

        except:
            print(f"error while following {i}")
            bad.append(i)
            time.sleep(10)
            continue

    print(f'{profile} Followed all {len(ident_follow)} except {str(*bad)}')

process = []
if __name__ == '__main__':
    print(profiles_ads)
    for name_profile in profiles_ads:
        print(name_profile)
        p = Process(target=start,args=[name_profile])
        p.start()
        time.sleep(3)
        print('Done')

