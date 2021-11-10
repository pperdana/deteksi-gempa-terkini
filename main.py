"""
Aplikasi deteksi gempa terkini
"""


def ekstraksi_data():
    hasil = dict()
    hasil['tanggal'] = "24 Agustus 2021"
    hasil['waktu'] = "12:05:52 WIB"
    hasil['magnitudo'] = 4.0
    hasil['lokasi'] = {'LS': 1.48, 'bt': 134.01}

    return hasil


def tampilkan_data(result):
    print("Gempa terakhir berdasakan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi {result['lokasi']}")


if __name__ == '__main__':
    print("Aplikasi Utama")
    result = ekstraksi_data()
    tampilkan_data(result)
