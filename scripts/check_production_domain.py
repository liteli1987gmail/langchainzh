#!/usr/bin/env python3
"""Check that the production domain is serving the generated docs site."""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass


DEFAULT_DOMAIN = "https://langchain.asia"
DEFAULT_DOC_PATH = "/oss/python/langchain/overview.html"


@dataclass(frozen=True)
class Response:
    url: str
    status: int
    headers: dict[str, str]
    body: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--domain", default=DEFAULT_DOMAIN)
    parser.add_argument("--doc-path", default=DEFAULT_DOC_PATH)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument(
        "--use-proxy",
        action="store_true",
        help="Use proxy variables from the environment.",
    )
    return parser.parse_args()


def normalize_domain(domain: str) -> str:
    domain = domain.strip().rstrip("/")
    if not domain.startswith(("http://", "https://")):
        domain = "https://" + domain
    return domain


def fetch(url: str, timeout: int, *, use_proxy: bool) -> Response:
    opener = (
        urllib.request.build_opener()
        if use_proxy
        else urllib.request.build_opener(urllib.request.ProxyHandler({}))
    )
    request = urllib.request.Request(url, headers={"User-Agent": "langchainzh-domain-check/1.0"})
    try:
        with opener.open(request, timeout=timeout) as response:
            body = response.read(600_000).decode("utf-8", errors="replace")
            return Response(
                url=response.geturl(),
                status=response.status,
                headers={key.lower(): value for key, value in response.headers.items()},
                body=body,
            )
    except urllib.error.HTTPError as exc:
        body = exc.read(600_000).decode("utf-8", errors="replace")
        return Response(
            url=exc.geturl(),
            status=exc.code,
            headers={key.lower(): value for key, value in exc.headers.items()},
            body=body,
        )


def assert_ok(response: Response, label: str) -> None:
    server = response.headers.get("server", "")
    marker = response.body[:1000]
    if response.status >= 400:
        raise SystemExit(
            f"{label} failed: HTTP {response.status} at {response.url}\n"
            f"server={server}\n"
            f"body={marker.strip()}"
        )
    if "DEPLOYMENT_DISABLED" in response.body:
        raise SystemExit(f"{label} still points to a disabled Vercel deployment.")


def main() -> int:
    args = parse_args()
    domain = normalize_domain(args.domain)
    root = fetch(domain + "/", args.timeout, use_proxy=args.use_proxy)
    assert_ok(root, "root")

    doc_path = "/" + args.doc_path.lstrip("/")
    doc = fetch(domain + doc_path, args.timeout, use_proxy=args.use_proxy)
    assert_ok(doc, "doc page")
    if "LangChain" not in doc.body and "LangGraph" not in doc.body:
        raise SystemExit(f"doc page did not look like LangChain docs: {doc.url}")

    print(f"production domain ok: {domain}")
    print(f"root: HTTP {root.status} server={root.headers.get('server', '')}")
    print(f"doc: HTTP {doc.status} {doc.url}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except urllib.error.URLError as exc:
        print(f"domain check failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
