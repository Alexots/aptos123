
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

button_follow_selector = str("""#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-1kihuf0.r-18u37iz.r-1pi2tsx.r-1777fci.r-1pjcn9w.r-xr3zp9.r-1xcajam.r-ipm5af.r-9dcw1g > div.css-1dbjc4n.r-z6ln5t.r-14lw9ot.r-1867qdf.r-1jgb5lz.r-pm9dpa.r-1ye8kvj.r-1rnoaur.r-494qqr.r-13qz1uu > div.css-1dbjc4n.r-eqz5dr.r-1hc659g.r-1n2ue9f.r-11c0sde.r-13qz1uu > div.css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-16y2uox.r-6gpygo.r-peo1c.r-1ps3wis.r-1ny4l3l.r-1udh08x.r-1guathk.r-1udbk01.r-o7ynqc.r-6416eg.r-lrvibr.r-3s2u2q > div > span > span""")

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
            btn = driver.find_element(By.CSS_SELECTOR,button_follow_selector)
            btn.click()
            time.sleep(random.randint(sleep_from,sleep_to))

        except:
            print(f"error while following {i}")
            bad.append(i)
            time.sleep(10)
            continue

    print(f'Followed all {len(ident_follow)} except {str(*bad)}')

process = []
if __name__ == '__main__':
    print(profiles_ads)
    for name_profile in profiles_ads:
        print(name_profile)
        p = Process(target=start,args=[name_profile])
        p.start()
        time.sleep(3)
        print('Done')

