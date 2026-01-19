import time

def otobüs_sorgula():
    print("--- ISPARTA AKILLI ULAŞIM REHBERİ ---")
    duraklar = {
        "37": "SDÜ Batı Yerleşkesi - Çarşı - KYK Hattı",
        "22": "Işıkkent - Şehir Hastanesi - Çarşı",
        "9": "Vatan Mahallesi - Çarşı"
    }
    
    no = input("Sorgulamak istediğiniz otobüs numarasını girin (Örn: 37): ")
    
    if no in duraklar:
        print(f"\n[BİLGİ] {no} numaralı hat: {duraklar[no]}")
        print("[DURUM] Hat aktif. Bir sonraki sefer yaklaşık 15 dakika içinde.")
    else:
        print("\n[HATA] Bu hat numarası sistemde tanımlı değil.")

if __name__ == "__main__":
    otobüs_sorgula() 
 
