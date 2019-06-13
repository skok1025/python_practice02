# 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
import re

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""
lastindex = 0
while True:
    firstindex = s.find("<",lastindex)
    if firstindex == -1:
        break;
    lastindex = s.find(">",firstindex)
    if lastindex != -1:
        s = s[:firstindex]+s[lastindex+1:]


print(s)
# s = s.replace(re.compile("/[<][^>]*[>]/gi"),"")
# print(s)
# def istag(word):
#     if str(word).strip().startswith("<"):
#         return ""
#     else:
#         return word
#
# l = s.split("\n")
# print(l)
# for w in l:
#     print(istag(w))
