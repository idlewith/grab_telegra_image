import os.path
import random
import re
import time
from urllib import parse

import requests


def get_html_text(url, session, headers):
    return session.get(url=url, headers=headers).text


def get_image_src(html_text):
    """
    the src uri: /file/bee617899a0de07c122ae.jpg
    the website combine domain name and uri
    """
    return re.findall(r'img src="(\S+)"', html_text)


def gen_image_url_name(image_path_list):
    name_url_list = []
    for image_path in image_path_list:
        name = image_path.replace("/file/", "")
        url = "https://telegra.ph" + image_path
        name_url_list.append([name, url])
    return name_url_list


def get_image_content(url, session, headers):
    return session.get(url=url, headers=headers).content


def get_image_info(url, session, headers):
    html_text = get_html_text(url, session, headers)
    image_path_list = get_image_src(html_text)
    image_name_url_dict = gen_image_url_name(image_path_list)

    return image_name_url_dict


def gen_headers():
    user_agent = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like"
        " Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like"
        " Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko)"
        " Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like"
        " Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko)"
        " Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like"
        " Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko)"
        " Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)"
        " Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like"
        " Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)"
        " Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like"
        " Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko)"
        " Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)"
        " Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like"
        " Gecko) Chrome/19.0.1055.1 Safari/535.24",
    ]
    headers = {
        "User-Agent": random.choice(user_agent),
        "Referer": "https://telegra.ph/",
    }
    return headers


def download_image(url):
    # create folder
    album = re.findall(r"telegra.ph/(.+)", parse.unquote(url))[0]
    path_data = os.path.join("data", album)
    if not os.path.exists(path_data):
        os.mkdir(path_data)

    # get image url
    headers = gen_headers()
    session = requests.session()
    image_name_url_list = get_image_info(url, session, headers)

    # save image to local folder
    for name, url in image_name_url_list:
        filename = os.path.join(path_data, name)
        if not os.path.exists(filename):
            with open(filename, "wb") as f:
                f.write(get_image_content(url, session, headers))
            print(f">>> {filename} done!")
            time.sleep(1)
        else:
            print(f">>> {filename} existed, pass")


def main():
    # url = "https://telegra.ph/NO001-%E6%98%AF%E4%B8%80%E5%8F%AA%E5%BA%9F%E5%96%B5%E4%BA%86-%E5%A5%B6%E7%89%9B-10-01-2"
    # url = "https://telegra.ph/E3Eva2-03-18-2"
    # url = "https://telegra.ph/6raYJv-06-03"
    # url = "https://telegra.ph/2qUZfe-03-18"
    # url = "https://telegra.ph/mINNBf-10-01"
    url = "https://telegra.ph/aqA3yi-02-06"
    download_image(url)
    print(">>> all task done!")


if __name__ == "__main__":
    main()
