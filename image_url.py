import random
import re

import requests

request_session = requests.session()
request_session.keep_alive = False


user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko)"
    " Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko)"
    " Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko)"
    " Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko)"
    " Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko)"
    " Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)"
    " Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko)"
    " Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)"
    " Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)"
    " Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)"
    " Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)"
    " Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko)"
    " Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)"
    " Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko)"
    " Chrome/19.0.1055.1 Safari/535.24",
]


def get_html_text(url):
    headers = {
        "User-Agent": random.choice(user_agent),
        "Referer": "https://telegra.ph/",
    }

    return request_session.get(url=url, headers=headers).text


def get_image_src(html_text):
    """
    the src uri: /file/bee617899a0de07c122ae.jpg
    the website combine domain name and uri
    """
    return re.findall(r'img src="(\S+)"', html_text)


def get_image_url_name(image_path_list):
    name_url_list = []
    for image_path in image_path_list:
        name = image_path.replace("/file/", "")
        url = "https://telegra.ph" + image_path
        name_url_list.append([name, url])
    return name_url_list


def get_image_content(url):
    headers = {
        "User-Agent": random.choice(user_agent),
        "Referer": "https://telegra.ph/",
    }
    return request_session.get(url=url, headers=headers).content


def get_image_info(url):
    html_text = get_html_text(url)
    image_path_list = get_image_src(html_text)
    image_name_url_dict = get_image_url_name(image_path_list)

    return image_name_url_dict
