import mitmproxy.http
import redis

server = 'ak-gs-gf.hypergryph.com'
conn_pool = redis.ConnectionPool(host='localhost',port=6379)

class BattleResult():
    def __init__(self) :
        self.re_pool = redis.Redis(connection_pool = conn_pool)

    def response(self,flow:mitmproxy.http.HTTPFlow):
        if flow.request.host == server and "battleFinish" in flow.request.path:
            request = flow.request.get_content()
            response = flow.response.get_content()
            self.re_pool.lpush('battleFinishTime',request)
            self.re_pool.lpush('battleFinish',response)


addons = [
    BattleResult()
]