# -*- coding: utf-8 -*-
"""
Atria: Cyber-Nexus - 极简全息本地服务器
基于 Python 标准库，免安装额外第三方库，开箱即用。
"""
import http.server
import socketserver
import webbrowser
import os
import sys
import threading

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class AtriaServer(socketserver.TCPServer):
    allow_reuse_address = True


class AtriaHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # 允许跨域与缓存友好
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def main():
    os.chdir(DIRECTORY)
    # 尝试绑定端口，若被占用自动递增
    port = PORT
    httpd = None
    for p in range(PORT, PORT + 20):
        try:
            httpd = AtriaServer(("", p), AtriaHandler)
            port = p
            break
        except OSError:
            continue

    if not httpd:
        print(f"[!] 无法绑定端口 {PORT}-{PORT+20}，请检查端口占用。")
        sys.exit(1)

    url = f"http://localhost:{port}/index.html"
    print("=" * 60)
    print("  Atria: Cyber-Nexus (全息量子智算星网)")
    print(f"  服务已在本地启动: {url}")
    print("  按 Ctrl + C 可终止服务")
    print("=" * 60)

    # 自动在默认浏览器中打开（独立守护线程，避免无头/远程环境下阻塞主服务）
    def _open_browser():
        try:
            webbrowser.open(url)
        except Exception:
            print(f"[*] 提示：请在浏览器中手动访问 {url}")
    threading.Thread(target=_open_browser, daemon=True).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] 服务已平稳停止。")

if __name__ == '__main__':
    main()
