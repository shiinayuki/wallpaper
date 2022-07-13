import requests
from lxml import etree
import re
import fileutil


class SpiderCdn:
    def __init__(self):
        self.pn = 1
        self.url = f"https://www.eso.org/public/images/list/{self.pn}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
        }
        self.path_dir = "Alphacoders"
        self.path_dir_html = f"{self.path_dir}/html"
        self.path_dir_img = f"{self.path_dir}/img"
        self.path_file_html = f"{self.path_dir_html}/{self.pn}.html"

    def get_data(self):
        res = requests.get(self.url, headers=self.headers).text

        return res

    def pares_page(self, data):
        res = re.findall(r"""var images = (.*?)</script>""", data, flags=re.S)
        res = str(res)
        res = res.replace("\\n", "").replace("  ", "")
        res = res[2:-5] + "]"
        print(res)
        id, title, width, height, src, url, potw = "id", "title", "width", "height", "src", "url", "potw"
        res = eval(res)

        return res

    def get_img(self, url_img):
        res_img = requests.get(url_img, headers=self.headers).content

        return res_img


def main(num_all, text, text_l, progressbar):
    count = 0
    my_spider = SpiderCdn()

    page_count_all = num_all//50 + 1

    fileutil.create_dir(my_spider.path_dir)
    fileutil.create_dir(my_spider.path_dir_html)
    fileutil.create_dir(my_spider.path_dir_img)

    for page_count in range(page_count_all):
        my_spider.pn = page_count + 1
        response = my_spider.get_data()

        fileutil.save_text(my_spider.path_file_html, response)
        # print(response)
        response = fileutil.read_text(my_spider.path_file_html)
        response = my_spider.pares_page(response)
        print(response)

        for i, response_i in enumerate(response):
            img_data = my_spider.get_img(response_i["src"])
            fileutil.save_img(my_spider.path_dir_img + f"/{count+1}.jpg", img_data)
            print(count, response_i["src"])

            count = count + 1
            progressbar['value'] = count
            text.set(f"{count}/{num_all}")
            text_l.update()

            if count >= num_all:
                return 0

    return -1


if __name__ == '__main__':
    main(10)

