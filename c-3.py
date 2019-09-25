"""
C-3: <censored> を自由に変更できるようにする
NGワードが含まれていた場合に置き換える文字列を自由に設定できるようにしてください
"""
class WordFilter:
    def __init__(self, object):
        self.NG = object

    def censor(self, content):
        print(content.replace(self.NG, '<censored>'))


def main():
    my_filter = WordFilter("アーセナル")

    # "昨日の<？？？？？>の試合アツかった！"
    my_filter.censor("昨日のアーセナルの試合アツかった！")

    # "昨日のリバプールの試合アツかった！"
    my_filter.censor("昨日のリバプールの試合アツかった！")


if __name__ == '__main__':
    main()