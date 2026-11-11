import http.server
import socketserver
import os

# Render يقوم بتحديد المنفذ تلقائياً عبر متغير البيئة PORT
PORT = int(os.environ.get("PORT", 8000))

# إعداد الخادم لتقديم الملفات من المجلد الحالي
Handler = http.server.SimpleHTTPRequestHandler

# تشغيل الخادم
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
