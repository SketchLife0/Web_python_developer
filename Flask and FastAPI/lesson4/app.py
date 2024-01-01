import argparse
import asyncio
import concurrent.futures
import datetime
import os
import requests


def get_filename_from_url(url):
    filename = os.path.basename(url)
    if filename.endswith("/"):
        filename = filename[:-1]
    return filename


def download_image(url, filename):
    start_time = datetime.datetime.now()
    response = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    end_time = datetime.datetime.now()
    print(f"Downloaded image {filename} in {end_time - start_time}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="+", help="List of URL addresses")
    args = parser.parse_args()

    # Многопоточный подход

    start_time = datetime.datetime.now()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_image, url, get_filename_from_url(url)) for url in args.urls]
        for future in futures:
            future.result()
    end_time = datetime.datetime.now()
    print(f"Multithreaded download in {end_time - start_time}")

    # Многопроцессорный подход

    start_time = datetime.datetime.now()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(download_image, url, get_filename_from_url(url)) for url in args.urls]
        for future in futures:
            future.result()
    end_time = datetime.datetime.now()
    print(f"Multiprocessing download in {end_time - start_time}")

    # Асинхронный подход

    start_time = datetime.datetime.now()
    tasks = [asyncio.ensure_future(download_image(url, get_filename_from_url(url))) for url in args.urls]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    end_time = datetime.datetime.now()
    print(f"Async download in {end_time - start_time}")


if __name__ == "__main__":
    main()