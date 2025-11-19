import argparse
import os
import sys
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_ready(driver, timeout: int = 20):
	WebDriverWait(driver, timeout).until(
		lambda d: d.execute_script("return document.readyState") == "complete"
	)


def auto_scroll(driver, pause: float = 0.3, max_steps: int = 50):
	last_height = driver.execute_script("return document.body.scrollHeight")
	steps = 0
	while steps < max_steps:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
		time.sleep(pause)
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height
		steps += 1
	driver.execute_script("window.scrollTo(0, 0)")


def save_as_mhtml(driver, out_path: str):
	# 使用 Chrome DevTools Protocol 保存为单文件 MHTML
	driver.execute_cdp_cmd("Page.enable", {})
	result = driver.execute_cdp_cmd("Page.captureSnapshot", {"format": "mhtml"})
	data = result.get("data") if isinstance(result, dict) else result
	if not data:
		raise RuntimeError("Failed to capture MHTML snapshot")

	os.makedirs(os.path.dirname(out_path), exist_ok=True)
	with open(out_path, "w", encoding="utf-8") as f:
		f.write(data)


def build_driver(headless: bool = True) -> webdriver.Chrome:
	options = Options()
	if headless:
		# 新版 headless，渲染效果更接近非无头
		options.add_argument("--headless=new")
	options.add_argument("--disable-gpu")
	options.add_argument("--window-size=1920,1080")
	options.add_argument("--no-sandbox")
	options.add_argument("--disable-dev-shm-usage")
	# 让 Selenium 4+ 自动用 Selenium Manager 管理 ChromeDriver（无需 webdriver_manager）
	return webdriver.Chrome(options=options)


def default_out_path(url: str) -> str:
	ts = datetime.now().strftime("%Y%m%d-%H%M%S")
	safe_title = url.rstrip("/").split("/")[-1] or "page"
	return os.path.join(
		os.path.dirname(__file__),
		"downloads",
		f"{safe_title}-{ts}.mhtml",
	)


def main(argv=None):
	parser = argparse.ArgumentParser(
		description="Download a web page with Selenium and save as a complete MHTML file."
	)
	parser.add_argument(
		"--url",
		default="https://en.macromicro.me/series/22748/cnn-fear-and-greed",
		help="Target page URL",
	)
	parser.add_argument(
		"--out",
		default=None,
		help="Output .mhtml file path (default: selenium/downloads/...)",
	)
	parser.add_argument(
		"--delay",
		type=float,
		default=0.0,
		help="Extra seconds to wait before capture (for manual actions like cookie consent)",
	)
	parser.add_argument(
		"--no-headless",
		action="store_true",
		help="Run browser in non-headless mode",
	)

	args = parser.parse_args(argv)
	out_path = args.out or default_out_path(args.url)

	driver = None
	try:
		driver = build_driver(headless=not args.no_headless)
		driver.get(args.url)

		# 页面就绪
		wait_for_ready(driver, timeout=25)

		# 可选：滚动触发懒加载，以便资源内嵌到 MHTML
		time.sleep(2)
		auto_scroll(driver, pause=0.4, max_steps=60)

		# 再等待一小会儿，给异步资源加载时间；可叠加 --delay
		time.sleep(2 + max(0.0, args.delay))

		save_as_mhtml(driver, out_path)
		print(out_path)
	finally:
		if driver is not None:
			driver.quit()


if __name__ == "__main__":
	sys.exit(main())

