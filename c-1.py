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