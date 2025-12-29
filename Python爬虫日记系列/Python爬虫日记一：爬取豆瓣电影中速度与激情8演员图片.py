import requests
import os
import re


def douban(url):
    r = requests.get(url)
    html = r.text
    result = re.findall(r'https://img\d.doubanio.com/img/celebrity/medium/.*.jpg', html)
    result2 = re.findall(r'(?<=title=").\S+', html)
    result2.pop()
    result3 = sorted(set(result2), key=result2.index)
    result3.pop(-3)
    if not os.path.exists('douban'):
        os.makedirs('douban')
    i = 0
    for link in result:
        filename = 'douban\\' + str(result3[i]) + '.jpg'
        i += 1
        with requests.get(link, stream=True) as response:
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)


url = 'https://movie.douban.com/subject/26260853/celebrities'
if __name__ == '__main__':
    douban(url)
