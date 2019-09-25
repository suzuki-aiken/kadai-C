"""
C-4: NGワードの複数登録
NGワードを複数登録できるようにしてください
"""

class WordFilter:
    def __init__(self, object):
        self.NG = object
    def censor(self, content):
        print(content.replace(self.NG, '<censored>'))

def main():

    my_filter = WordFilter("アーセナル")

    my_filter.censor("昨日のアーセナルの試合アツかった！")

    my_filter.censor("昨日のリバプールの試合アツかった！")


if __name__ == '__main__':
    main()