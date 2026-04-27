import time
from atproto import Client

# --- GİRİŞ BİLGİLERİ ---
HANDLE = "becaecosystem.bsky.social" 
PASSWORD = "2222-1111-0000-1111"         

def bsky_temizlik():
    client = Client()
    try:
        client.login(HANDLE, PASSWORD)
        print(f"Başarıyla giriş yapıldı: {HANDLE}")
    except Exception as e:
        print(f"Giriş hatası: {e}")
        return
    
    print("Veriler çekiliyor, lütfen bekle...")

    following = {}
    cursor = None
    while True:
        res = client.get_follows(actor=HANDLE, cursor=cursor)
        for follow in res.follows:
            following[follow.did] = follow.handle
        if not res.cursor:
            break
        cursor = res.cursor

    followers = set()
    cursor = None
    while True:
        res = client.get_followers(actor=HANDLE, cursor=cursor)
        for follower in res.followers:
            followers.add(follower.did)
        if not res.cursor:
            break
        cursor = res.cursor

    print(f"Takip ettiklerin: {len(following)}")
    print(f"Takipçilerin: {len(followers)}")
    print("-" * 30)

    sayac = 0
    for did, handle in following.items():
        if did not in followers:
            try:
                relationship = client.app.bsky.graph.get_relationships({'actor': HANDLE, 'others': [did]})
                if relationship.relationships[0].following:
                    # GÜNCEL SİLME KOMUTU:
                    uri = relationship.relationships[0].following
                    client.unfollow(uri) 
                    
                    sayac += 1
                    print(f"{sayac}. Takipten çıkıldı: {handle}")
                    time.sleep(3) # Senin istediğin 3 saniye
            except Exception as e:
                print(f"Hata oluştu ({handle}): {e}")
                time.sleep(2)

    print(f"\nİşlem bitti! {sayac} kişi takipten çıkarıldı.")

if __name__ == "__main__":
    bsky_temizlik()