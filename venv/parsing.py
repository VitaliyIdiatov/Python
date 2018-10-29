import re
import requests

url = 'https://olympiaperm.ru/price/'
r = requests.get(url)
r_str = repr(r.text)
r_str = re.sub(r' {2,}', '', r_str)
r_str = re.sub(r'\\t', '', r_str)
r_str = re.sub(r'\\n', '', r_str)
r_str = re.sub(r'<br>', '', r_str)
r_str = re.sub(r'</br>', '', r_str)

with open('test.html', 'w') as output_file:
    output_file.write(r_str)

regex = '<thead><tr><th>(.*)</th></tr></thead>'
r_pattern = re.compile(regex)
r_result = re.search(r_pattern, r_str)

print(r_result.group(0))