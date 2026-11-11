import http.server
import socketserver
import os
import threading
import time
import urllib.request

PORT = int(os.environ.get("PORT", 8000))
# الرابط الخاص بموقعك
MY_URL = "https://jumanfurat.onrender.com"

# دالة الإبقاء على الموقع مستيقظاً
def keep_alive():
    while True:
        # الانتظار لمدة 6 دقائق (360 ثانية)
        time.sleep(360)
        try:
            # إرسال طلب (Ping) للموقع
            req = urllib.request.Request(MY_URL, headers={'User-Agent': 'KeepAliveBot'})
            urllib.request.urlopen(req, timeout=15)
            print(f"[{time.strftime('%H:%M:%S')}] تم إرسال طلب الإبقاء مستيقظاً بنجاح.")
        except Exception as e:
            print(f"فشل إرسال الطلب: {e}")

# تشغيل عملية الإبقاء الحيوي في الخلفية
threading.Thread(target=keep_alive, daemon=True).start()

# إعداد خادم الملفات
Handler = http.server.SimpleHTTPRequestHandler

# استخدام ThreadingServer للسماح باستقبال الطلبات وعدم تعليق الموقع أثناء إرسال الـ Ping
class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

with ThreadingServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
