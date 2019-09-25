"""
C-1: NGワードが含まれているかどうかを判定できる
NGワードが含まれているかどうかを判定できる detect() メソッドを持つ WordFilterクラス を実装してください
下記のコードが動作すればOKです
my_filter = WordFilter("アーセナル")

# NGワードが含まれている場合
my_filter.detect("昨日のアーセナルの試合アツかった！") # Trueを返す ※出力されるわけではありません！

# NGワードが含まれていない場合
my_filter.detect("昨日のリバプールの試合アツかった！") # Falseを返す ※出力されるわけではありません！
"""


class WordFilter:
    def __init__(self, object):
        self.NG = object

    def detect(self, content):
        return f'{self.NG in content}'


def main():
    my_filter = WordFilter("アーセナル")
    #
    my_filter.detect("昨日のアーセナルの試合アツかった！")  # True
    #
    my_filter.detect("昨日のリバプールの試合アツかった！")  # False

    print(my_filter.detect("アーセナルです"))


if __name__ == '__main__':
    main()
