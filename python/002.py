##問題
##「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
##
##補完
##zip関数は引数から要素を１つずつ取り出す。
##
##

str1 = "パトカー"
str2 = "タクシー"
ans = ""

for a,b in zip(str1,str2):
    ans = ans + a + b

print(ans)