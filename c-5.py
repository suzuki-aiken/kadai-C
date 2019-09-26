"""
C-5: NGワードの変更
NGワードを後から変更できるようにしてください
"""


class WordFilter:
    def __init__(self, object):
        self.NG = object

    def censor(self, content):
        for i in self.NG:
            content = content.replace(i, '<censored>')

        return print(f'{content}')


def main():
    NG_list = []

    NG_list.append("アーセナル")

    add_NGword='start'

    while add_NGword != 'fff':

        my_filter = WordFilter(NG_list)

        my_filter.censor("昨日のアーセナルの試合アツかった！")

        my_filter.censor("昨日のリバプールの試合アツかった！")

        add_NGword = input("NGワードを追加してください(止める場合は　'fff' を入力):")

        if add_NGword == 'fff':
            break

        NG_list.clear()
        NG_list.append(add_NGword)


if __name__ == '__main__':
    main()
