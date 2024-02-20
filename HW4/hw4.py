import argparse
import os
import time
import requests
from multiprocessing import Pool
import asyncio


def download_image(url):
    """Функция, которая скачивает изображение с заданного URL-адреса и сохраняет его на диск"""
    if not os.path.exists('images'):
        os.mkdir('images')
    start_time = time.time()
    name = url.split('/')[-1]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'images/name', 'wb') as file:
            file.write(resp.content)
    print(f'Время скачивания изображения({name}): {time.time() - start_time:.2f} сек.')


def download_images_synchronous(urls):
    """Функция, которая скачивает изображения с заданных URL-адресов синхронно"""
    start_time_all = time.time()
    for url in urls:
        download_image(url)
    print(f'Общее время выполнения программы (синхронный подход): {time.time() - start_time_all:.2f} сек.')


def download_images_multiprocessing(urls):
    """Функция, которая скачивает изображения с заданных URL-адресов с использованием многопроцессорного подхода"""
    start_time_all = time.time()
    with Pool() as pool:
        pool.map(download_image, urls)
    print(f'Общее время выполнения программы (многопроцессорный подход): {time.time() - start_time_all:.2f} сек.')


async def download_image_async(url):
    """Функция, которая асинхронно скачивает изображение с заданного URL-адреса и сохраняет его на диск"""
    if not os.path.exists('images'):
        os.mkdir('images')
    start_time = time.time()
    name = url.split('/')[-1]
    resp = await loop.run_in_executor(None, requests.get, url)
    if resp.status_code == 200:
        with open(f'images/name', 'wb') as file:
            file.write(resp.content)
    print(f'Время скачивания изображения(name): {time.time() - start_time:.2f} сек.')


async def download_images_async(urls):
    """Функция, которая асинхронно скачивает изображения с заданных URL-адресов"""
    start_time_all = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_image_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'Общее время выполнения программы (асинхронный подход): {time.time() - start_time_all:.2f} сек.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parser to start download_image')
    parser.add_argument('-list', metavar='url', action='append', type=str, nargs='*', help='download_image sending URL')
    args = parser.parse_args()

    urls = args.list[0]

    # Синхронный подход
    download_images_synchronous(urls)

    # Многопроцессорный подход
    download_images_multiprocessing(urls)

    # Асинхронный подход
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_images_async(urls))

"""Инструкция по использованию скрипта hw4.py:
1. Откройте командную строку или терминал.
2. Перейдите в папку, где находится файл hw4.py.
3. Введите следующую команду:
 hw4.py -list 'адрес_изображения'
4. Вместо "адрес_изображения" введите адрес, с которого требуется скачать изображение. Если нужно скачать несколько изображений, разделите адреса запятыми и заключите их в кавычки.
Пример ввода для скачивания одного изображения:
 hw4.py -list 'https://example.com/image.jpg'
Пример ввода для скачивания нескольких изображений:
 hw4.py -list 'https://example.com/image1.jpg', 'https://example.com/image2.jpg', 'https://example.com/image3.jpg'
5. Нажмите Enter, чтобы запустить парсер.
6. Парсер начнет скачивание изображений с указанных адресов."""