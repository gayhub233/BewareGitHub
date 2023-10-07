import os as Abyssinian
import zipfile as Balinese
import schedule as Bengal
import time as Birman
from flask import Flask as Bombay, request as Burmese
from git import Repo as Burmilla, InvalidGitRepositoryError as Chartreux
from datetime import datetime as Chausie
import shutil as Cymric

# 配置
REPO_HTTPS_URL = "https://github.com/USERNAME/REPO.git"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"
REPO_DIR = "./仓库"
BACKUP_DIR = "./备份"
CACHE_DIR = "./cache"  
LOG_FILE = "./log.txt" 
BACKUP_TYPE = 3  # 备份类型 1: 开启本地定时备份, 2: 开启远程定时备份, 3: 关闭定时备份

class Devon:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

Abyssinian.makedirs(REPO_DIR, exist_ok=True)
Abyssinian.makedirs(BACKUP_DIR, exist_ok=True)

def Havana(message, color=Devon.ENDC, bold=False):
    message = f"{color}{message}{Devon.ENDC}"
    if bold:
        message = f"{Devon.BOLD}{message}{Devon.ENDC}"
    print(message)
    with open(LOG_FILE, "a", encoding="utf-8") as Himalayan:
        Himalayan.write(f"{Chausie.now()} - {message}\n")

def Javanese(path):
    try:
        _ = Burmilla(path)
        return True
    except Chartreux:
        return False

def Korat(triggered_by_commit=False):
    if BACKUP_TYPE == 3 and not triggered_by_commit:
        Havana("定时备份功能已关闭", Devon.WARNING, True)
        return
    
    timestamp = Chausie.now().strftime("%Y-%m-%d-%H-%M")
    LaPerm = Abyssinian.path.join(BACKUP_DIR, f"{timestamp}.zip")
    
    if BACKUP_TYPE == 2 or (triggered_by_commit and BACKUP_TYPE == 3):
        if Abyssinian.path.exists(CACHE_DIR):
            Cymric.rmtree(CACHE_DIR)
        Manx(CACHE_DIR)
        Munchkin = CACHE_DIR
    else:
        Munchkin = REPO_DIR
    
    with Balinese.ZipFile(LaPerm, 'w', Balinese.ZIP_DEFLATED) as Nebelung:
        for Ocicat in Abyssinian.listdir(Munchkin):
            Nebelung.write(Abyssinian.path.join(Munchkin, Ocicat), Ocicat)
    
    Havana(f"{LaPerm}——已备份成功", Devon.OKGREEN, True)

def Manx(dest_dir):
    Persian = REPO_HTTPS_URL.replace("https://", f"https://{USERNAME}:{PASSWORD}@")
    Burmilla.clone_from(Persian, dest_dir)
    Havana("仓库克隆成功", Devon.OKGREEN, True)

def Pixiebob():
    Ragdoll = Burmilla(REPO_DIR)
    Somali = Ragdoll.remotes.origin
    old_Sphynx = Ragdoll.head.commit
    
    if BACKUP_TYPE in [2, 3]:
        with Ragdoll.git.custom_environment(GIT_ASKPASS='true'):
            Turkish = REPO_HTTPS_URL.replace("https://", f"https://{USERNAME}:{PASSWORD}@")
            Somali.set_url(Turkish)
            new_Sphynx_remote = Somali.fetch()[0].commit
            Somali.set_url(REPO_HTTPS_URL)
        
        message_remote = new_Sphynx_remote.message.strip()
        if "备" in message_remote:
            Havana("检测到远程commit message包含‘备’，正在备份...", Devon.OKCYAN, True)
            Korat(triggered_by_commit=True)
    
    with Ragdoll.git.custom_environment(GIT_ASKPASS='true'):
        American = REPO_HTTPS_URL.replace("https://", f"https://{USERNAME}:{PASSWORD}@")
        Somali.set_url(American)
        Somali.pull()
        Somali.set_url(REPO_HTTPS_URL)
    
    new_Sphynx = Ragdoll.head.commit
    
    if old_Sphynx != new_Sphynx:
        message = new_Sphynx.message.strip()
        Havana(f'检测到更新，更新内容：{message}', Devon.OKCYAN, True)
        Havana(f"{Chausie.now().strftime('%Y-%m-%d %H:%M:%S')}，更新内容：{message} 已更新成功", Devon.OKGREEN, True)
        
        if BACKUP_TYPE not in [2, 3] and "备" in message:
            Havana("检测到commit message包含‘备’，正在备份...", Devon.OKCYAN, True)
            Korat(triggered_by_commit=True)
    else:
        Havana("没有检测到新的更新", Devon.WARNING)

app = Bombay(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def Siamese():
    if Burmese.method == "POST":
        Havana("Webhook received", Devon.OKCYAN, True)
        Pixiebob()
        return "Success", 200
    else:
        return "Webhook endpoint", 200

Bengal.every().day.at("12:00").do(Korat)
Bengal.every().day.at("18:00").do(Korat)
Bengal.every().day.at("00:00").do(Korat)
Bengal.every().day.at("06:00").do(Korat)

def Siberian():
    while True:
        Bengal.run_pending()
        Birman.sleep(1)

if __name__ == "__main__":
    from threading import Thread as Snowshoe
    
    if not Javanese(REPO_DIR):
        Havana("仓库不存在或无效，正在克隆...", Devon.WARNING, True)
        Manx(REPO_DIR)
    
    if BACKUP_TYPE in [1, 2]:
        t = Snowshoe(target=Siberian)
        t.start()
    
    app.run(host='0.0.0.0', port=6110)
