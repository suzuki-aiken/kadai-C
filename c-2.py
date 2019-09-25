"""
C-2: NGワードを変換できる
NGワードが含まれていた場合に、NGワードを <censored> という文字に変換できる censor メソッドを実装してください
下記のコードが動作すればOKです
my_filter = WordFilter("アーセナル")

# NGワードが含まれている場合
my_filter.censor("昨日のアーセナルの試合アツかった！") # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

# NGワードが含まれていない場合
my_filter.censor("昨日のリバプールの試合アツかった！") # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！
"""


class WordFilter:
    def __init__(self, object):
        self.NG = object

    def censor(self, content):
        print(content.replace(self.NG, '<censored>'))


def main():
    my_filter = WordFilter("アーセナル")

    # "昨日の<censored>の試合アツかった！"
    my_filter.censor("昨日のアーセナルの試合アツかった！")

    # "昨日のリバプールの試合アツかった！"
    my_filter.censor("昨日のリバプールの試合アツかった！")


if __name__ == '__main__':
    main()
