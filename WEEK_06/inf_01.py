text = [
    '   + -- + - + -   ',
    '   + --- + - +   ',
    '   + -- + - + -   ',
    '   + - + - + - +   ']

l = []
'''
for i in text:
    # 양옆 공백 제거, 사이사이 공백 제거 + 이진법으로 변환
    l.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))

print(''.join(l))
'''

# 한 줄로
print(''.join([chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for i in text]))
