import time
import requests
import pytest

URLS = [
    "https://qualidade.apprbs.com.br/certificacao",
    "https://qualidade.apprbs.com.br/site",
]

@pytest.mark.web
def test_paginas_retornam_200_e_tempo_ok():
    for url in URLS:
        start = time.time()
        r = requests.get(url, timeout=15)
        elapsed = time.time() - start

        assert r.status_code == 200, f"{url} retornou {r.status_code}"
        assert elapsed < 5.0, f"{url} demorou {elapsed:.2f}s (acima de 5s)"