import requests
import re
from secret import cookie

headers = {
    'cookie': cookie,
}

response = requests.get('https://adventofcode.com/2020/day/2/input', headers=headers)

in_data = response.text.split('\n')[:-1]
#in_data =['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']
valid = 0
for row in in_data:
    min = int(re.findall('.+?(?=-)',row)[0])
    max = int(re.findall('(?<=-)(.*?)(?= )',row)[0])
    letter = re.findall('(?<= )(.*?)(?=:)',row)[0]
    pwd = re.findall('(?<=: )(.*?)$',row)[0]
    matches = len(re.findall(letter,pwd))
    if min <=  matches <= max:
        valid +=1
print(valid)
valid = 0

for row in in_data:
    pos1 = int(re.findall('.+?(?=-)',row)[0])
    pos2 = int(re.findall('(?<=-)(.*?)(?= )',row)[0])
    letter = re.findall('(?<= )(.*?)(?=:)',row)[0]
    pwd = re.findall('(?<=: )(.*?)$',row)[0]
    if (pwd[pos1-1] == letter) != (pwd[pos2-1] == letter):
        valid +=1

print(valid)
