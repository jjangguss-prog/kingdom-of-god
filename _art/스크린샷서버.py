# 게임 화면을 찍어 파일로 남기는 시험용 서버 v0.1 (2026-10-18)
# 사용: py -3.13 스크린샷서버.py [포트]   (.claude/launch.json의 kog-shot, 8770)
# 저장소 뿌리를 그대로 내보내고(http.server와 같음), 페이지가 POST /_shot?name=<이름> 으로 보낸 JPEG을 _art/sk_raw/<이름>.jpg로 남긴다.
# 기술 카드(탑 4단계 기술의 예시 화면) 후보를 찍을 때 쓴다. 고른 것만 art/sk/로 옮긴다.
import http.server, os, re, sys, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, '_art', 'sk_raw')


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        name = urllib.parse.parse_qs(u.query).get('name', [''])[0]
        if u.path != '/_shot' or not re.fullmatch(r'[A-Za-z0-9_\-]{1,60}', name):
            self.send_error(400)
            return
        n = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(n)
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, name + '.jpg'), 'wb') as f:
            f.write(data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'ok')

    def log_message(self, *a):
        pass


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8770
    http.server.ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()
