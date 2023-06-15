import os.path
import re
import time

from urllib import parse

from image_url import get_image_info, get_image_content


def download_image(url):
    album = re.findall(r"telegra.ph/(.+)", parse.unquote(url))[0]
    path_data = os.path.join("data", album)

    image_name_url_list = get_image_info(url)

    if not os.path.exists(path_data):
        os.mkdir(path_data)

    for name, url in image_name_url_list:
        filename = os.path.join(path_data, name)
        if not os.path.exists(filename):
            with open(filename, "wb") as f:
                f.write(get_image_content(url))
            print(f">>> {filename} done!")
            time.sleep(1)
        else:
            print(f">>> {filename} existed, pass")


def main():
    # url = "https://telegra.ph/NO001-%E6%98%AF%E4%B8%80%E5%8F%AA%E5%BA%9F%E5%96%B5%E4%BA%86-%E5%A5%B6%E7%89%9B-10-01-2"
    url = "https://telegra.ph/E3Eva2-03-18-2"
    download_image(url)
    print(">>> all task done!")


if __name__ == "__main__":
    main()
