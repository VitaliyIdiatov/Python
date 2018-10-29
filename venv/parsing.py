import re
import requests

url = 'https://olympiaperm.ru/price/'
r = requests.get(url)
r_str = repr(r.text)
r_str = re.sub(r'&nbsp;{1,2}', '', r_str)
r_str = re.sub(r'&nbsp;{3,}', ' ', r_str)
r_str = re.sub(r' {2,}', '', r_str)
r_str = re.sub(r'\\t', '', r_str)
r_str = re.sub(r'\\n', '', r_str)
r_str = re.sub(r'<br>', '', r_str)
r_str = re.sub(r'</br>', '', r_str)
r_str = re.sub(r' <', '<', r_str)
r_str = re.sub(r'> ', '>', r_str)
r_str = re.sub(r'  ', ' ', r_str)

with open('test.html', 'w') as output_file:
    output_file.write(r_str)

regex = '(<thead><tr><th>)(.*?)(</th></tr></thead>)'
r_pattern = re.compile(regex)
r_heads = re.findall(r_pattern, r_str)

csv = open('parsed.csv', 'w')

for x in range(len(r_heads)):
    row = re.sub(r'</th><th>', ', ', r_heads[x][1]) + '\n'
    csv.write(row)  # 17 items inside list
