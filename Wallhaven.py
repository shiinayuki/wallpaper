# wallhaven 壁纸下载

import os
import re
import time
import urllib.parse
import urllib.request
import urllib.error


def main(menu, text, text_l, progressbar):
    jishu = 0
    print("*" * 8, "[+] Wallhaven.cc壁纸批量下载", "*" * 8)
    page_start = int(1)
    page_end = int(menu / 18 + 1)
    url = 'https://wallhaven.cc/toplist?page='
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    for page in range(page_start, page_end + 1):
        print("[+] 开始传输第%s页数据" % page)
        resquest = request_get(url, headers, page)
        countent = urllib.request.urlopen(resquest).read().decode()
        jishu = img_download(countent, headers, menu, jishu, text, text_l, progressbar)

        print("[+] 第%s页数据传输完成" % page)
        print()
        if jishu == 0:
            print("完成")
            return 0
        time.sleep(0.5)

    if jishu < menu:
        return -1
    else:
        return 0


def img_download(countent, headers, menu, jishu, text, text_l, progressbar):

    lt = re.findall(r'<li><figure.*?>.*?<a class="preview" href="(.*?)" .*?></a>.*?</figure></li>', countent,
                    flags=re.S)
    dirname = 'wallhaven'
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    download_src = 'https://w.wallhaven.cc/full/'
    for img_src in lt:
        img_src = download_src + img_src[-6:-4] + '/wallhaven-' + img_src[-6:] + '.jpg'
        file_name = dirname + '/' + img_src[-10:]
        request = urllib.request.Request(url=img_src, headers=headers)
        try:
            response = urllib.request.urlopen(request)
            with open(file_name, 'wb') as f:
                jishu = count(1, jishu)
                f.write(response.read())
            progressbar['value'] = jishu
            text.set(f"{jishu}/{menu}")
            text_l.update()
            if jishu >= menu:
                return 0
        except urllib.error.HTTPError as e:
            print("[-] 重试中...")

    return jishu


def count(shu, jishu):
    jishu += 1
    print("[+] 第 %s 张图片下载完成" % jishu)
    return jishu


def request_get(url, headers, page):
    page_url = url + str(page)
    request = urllib.request.Request(url=page_url, headers=headers)
    return request


if __name__ == "__main__":
    menu = int(input("[~] 请输入爬取图片的数量:"))
    main(menu)
