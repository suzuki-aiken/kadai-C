"""
C-5: NGワードの変更
NGワードを後から変更できるようにしてください
"""


class WordFilter:
    def __init__(self, object, 伏字):
        self.NG = object
        self.hide = 伏字

    def censor(self, content):
        for i in self.NG:
            for j in self.hide:
                content = content.replace(i, j)

        return print(f'{content}')


def main():
    NG_list = ["アーセナル", "アツ", "bbb"]
    NG_list2 = ["アーセナル", "試合", "bbb"]

    my_filter = WordFilter(NG_list, NG_list2)

    my_filter.censor("昨日のアーセナルの試合アツかった！")

    my_filter.censor("昨日のリバプールの試合アツかった！")


if __name__ == '__main__':
    main()
