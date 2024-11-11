from sglang_router import Router, PolicyType

r = Router(worker_urls=["http://127.0.0.1:30000", "http://127.0.0.1:30001"])
r.start()