# 🧹 Bluesky Unfollow Non-Followers (Auto-Clean)

Bu araç, Bluesky hesabınızda sizi geri takip etmeyen (non-followers) hesapları otomatik olarak tespit eder ve belirlediğiniz aralıklarla takipten çıkarır. Profilinizdeki takip/takipçi oranını korumak ve "ölü" hesaplardan kurtulmak için idealdir.

## ✨ Özellikler

- **Tam Analiz:** Takip ettiklerinizi ve takipçilerinizi karşılaştırarak sizi takip etmeyenleri listeler.
- **Güvenli Temizlik:** Her işlem arasında **3 saniye** bekleyerek Bluesky API limitlerine takılmadan doğal bir şekilde çalışır.
- **Canlı Raporlama:** Terminal üzerinden hangi kullanıcının takipten çıkarıldığını anlık olarak gösterir.
- **İlişki Kontrolü:** `get_relationships` protokolü ile hata payını sıfıra indirir.

## 🛠️ Kurulum ve Kullanım

1. **Bağımlılıkları Yükleyin:**
   ```bash
   pip install atproto
