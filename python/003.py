##問題
##"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
##
##補完
##よくreplaceが使われているが、これは本来置換で使われいる、
##削除だけならstripのほうが複数指定できるので楽
##その後splitで単語で分けてリスト化。forで回しながらlenで数をカウントしてans配列に追加していく
##

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.strip(".,")
str = str.split()

ans = []

for word in str:
    ans.append(len(word))

print(ans)
