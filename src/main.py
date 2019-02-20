import re
import urllib.request
import bs4

CARTFILE_URL = ""
PODFILE_URL = ""

class Main:

    def getTextFromUrl(self, url):
        response = urllib.request.urlopen(url)
        # text = bs4.BeautifulSoup(response.read())
        text = response.read().decode('utf-8')
        return text

    def getCartfileInfo(self):
        text = self.getTextFromUrl(CARTFILE_URL)
        print(text)
        # 実効行のみ抽出する.
        not_comment_pattern = re.compile(r'^(?!\s*[#]+).+$', flags=(re.MULTILINE))
        result = not_comment_pattern.findall(text)
        lib_list = []
        for element in result:
            # 空白で区切る.
            elem = element.split()
            lib_list.append(elem[1] + " : " + elem[-1])
        return lib_list

    def getPodfileInfo(self):
        text = self.getTextFromUrl(PODFILE_URL)
        print(text)
        # podで始まる行のみ抽出する.
        not_comment_pattern = re.compile(r'^\s*pod .+$', flags=(re.MULTILINE))
        result = not_comment_pattern.findall(text)
        print(result)
        lib_list = []
        for element in result:
            # 空白で区切る.
            elem = element.split()

            print(elem)
            # lib_list.append(elem[1] + " : " + elem[-1])
        return lib_list

main = Main()
# print(main.getCartfileInfo())
# print(main.getPodfileInfo())
main.getPodfileInfo()