import argparse
import time
from pathlib import Path

import requests


def download_with_requests(url: str, out_path: str, timeout: int = 20) -> None:
	headers = {
		"User-Agent": (
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
			"AppleWebKit/537.36 (KHTML, like Gecko) "
			"Chrome/120.0.0.0 Safari/537.36"
		),
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
		"Connection": "keep-alive",
	}
	resp = requests.get(url, headers=headers, timeout=timeout)
	resp.raise_for_status()
	Path(out_path).parent.mkdir(parents=True, exist_ok=True)
	with open(out_path, "wb") as f:
		f.write(resp.content)



def download_with_playwright(
	url: str,
	out_html: str | None = None,
	out_png: str | None = None,
	wait_seconds: float = 6.0,
	viewport_width: int = 1440,
	viewport_height: int = 900,
):
	try:
		from playwright.sync_api import sync_playwright
	except Exception as e:
		raise RuntimeError(
			"Playwright 未安装，请先 `pip install playwright`，并在服务器上执行 `python -m playwright install --with-deps chromium`"
		) from e

	with sync_playwright() as p:
		browser = p.chromium.launch(headless=True)
		context = browser.new_context(
			viewport={"width": viewport_width, "height": viewport_height}
		)
		page = context.new_page()
		page.goto(url, wait_until="networkidle")
		time.sleep(wait_seconds)
		page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
		time.sleep(1)

		if out_html:
			Path(out_html).parent.mkdir(parents=True, exist_ok=True)
			html = page.content()
			with open(out_html, "w", encoding="utf-8") as f:
				f.write(html)

		if out_png:
			Path(out_png).parent.mkdir(parents=True, exist_ok=True)
			page.screenshot(path=out_png, full_page=True)

		context.close()
		browser.close()


def main(argv=None):
	parser = argparse.ArgumentParser(
		description="下载网页到本地（支持 requests / playwright）"
	)
	parser.add_argument(
		"url",
		nargs="?",
		default="https://sc.macromicro.me/charts/50108/cnn-fear-and-greed",
		help="目标 URL",
	)
	parser.add_argument(
		"--method",
		choices=["requests", "playwright"],
		default="requests",
		help="下载方式：requests（原始HTML）或 playwright（渲染后HTML/截图）",
	)
	parser.add_argument(
		"--out",
		default=str(Path(__file__).with_name("cnn-fear-and-greed.html")),
		help="使用 requests 时保存的 HTML 路径",
	)
	parser.add_argument(
		"--out-html",
		default=str(Path(__file__).with_name("cnn-fear-and-greed_rendered.html")),
		help="使用 playwright 时保存渲染后 HTML 的路径",
	)
	parser.add_argument(
		"--out-png",
		default=str(Path(__file__).with_name("cnn-fear-and-greed.png")),
		help="使用 playwright 时保存全页截图 PNG 的路径",
	)
	parser.add_argument(
		"--wait",
		type=float,
		default=6.0,
		help="渲染方式额外等待秒数（用于异步内容渲染）",
	)

	args = parser.parse_args(argv)

	if args.method == "requests":
		download_with_requests(args.url, args.out)
		print(f"已保存：{args.out}")
	elif args.method == "playwright":
		download_with_playwright(
			args.url,
			out_html=args.out_html,
			out_png=args.out_png,
			wait_seconds=args.wait,
		)
		print(f"已保存渲染后 HTML：{args.out_html}")
		print(f"已保存截图：{args.out_png}")


if __name__ == "__main__":
	main()

