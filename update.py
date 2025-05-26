import requests

def check_version():
    current_version = "1.2.2"
    url = "https://raw.githubusercontent.com/kullaniciadi/projeadi/main/version.txt"
    remote_version = requests.get(url).text.strip()

    if current_version != remote_version:
        print("Yeni güncelleme var!")
        return True
    else:
        print("Güncel sürüm.")
        return False
    
def download_latest():
    download_url = "https://github.com/yunusemretom/whatsapp-bulk-messenger/main.py"
    r = requests.get(download_url)

    with open("main_updated.py", "w", encoding="utf-8") as f:
        f.write(r.text)
    print("Yeni sürüm indirildi.")



if __name__ == "__main__":
    if check_version():
        download_latest()
    else:
        print("Zaten en son sürümdesiniz.")