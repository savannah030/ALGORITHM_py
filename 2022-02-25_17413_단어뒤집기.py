import sys
import re
input = sys.stdin.readline

s = input().rstrip()
r = re.compile("<[a-z\s]+>|[0-9a-z]+|\s")

answer = '';
for token in r.findall(s):
    if token[0]=='<' or token[0]==' ':
        answer += token
    else:
        answer += token[::-1]
print(answer)
