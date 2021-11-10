import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        content = requests.get("https://www.b mkg.go.id/")
    except Exception:
        return None

    print(content.status_code)
    # soup = BeautifulSoup(content)
    if content.status_code == 200:
        hasil = dict()
        hasil['tanggal'] = "24 Agustus 2021"
        hasil['waktu'] = "12:05:52 WIB"
        hasil['magnitudo'] = 4.0
        hasil['lokasi'] = {'LS': 1.48, 'bt': 134.01}

        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak menemukan data gempa terkini")
        return
    print("Gempa terakhir berdasakan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi {result['lokasi']}")

