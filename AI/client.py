import httpx

client = httpx.Client(
    base_url="http://127.0.0.1:11434",
    timeout=120.0
)