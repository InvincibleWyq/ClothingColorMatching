word2color = {
    '黑': 'black', '墨': 'black', 'BLACK': 'black', 'Black': 'black', 'black': 'black',

    '白': 'white', '本白': 'white', '珍珠白': 'white', '象牙白': 'white', 
    '乳白': 'white', '奶白': 'white', '象牙': 'white', '珍珠': 'white',

    '灰': 'gray', '灰白': 'gray', '白灰': 'gray','深灰': 'gray',
    '浅灰': 'gray', '灰蓝': 'gray', '蓝灰': 'gray', '黑灰': 'gray',
    '灰黑': 'gray', '烟灰': 'gray', '银': 'gray', '银灰': 'gray',
    '米灰': 'gray',

    '红': 'red', '酒红': 'red', '大红': 'red', '砖红': 'red',
    '枣红': 'red', '红格': 'red', '西瓜红': 'red', '锈红': 'red',
    '红花': 'red', '玫瑰': 'red', 

    '粉': 'pink', '粉红':'pink', '玫红':'pink', '皮粉':'pink',
    '豆沙':'pink', '藕粉':'pink', '藕':'pink', '浅粉':'pink', 
    '豆沙粉':'pink', '豆沙红':'pink', '橘粉':'pink', '樱花粉':'pink',
    '紫粉':'pink', '浅绛':'pink', 

    '紫': 'purple', '紫红': 'purple', '浅紫': 'purple', '香芋紫': 'purple',
    '紫罗兰': 'purple', '粉紫': 'purple', '葡萄紫': 'purple', '深紫': 'purple',
    '香芋': 'purple', '梅子': 'purple', '火龙果': 'purple', '薰衣草': 'purple',

    '蓝': 'blue', '兰': 'blue', '宝蓝': 'blue', '牛仔蓝': 'blue',
    '浅蓝': 'blue', '天蓝': 'blue', '雾霾蓝': 'blue', '孔雀蓝': 'blue',
    '湖蓝': 'blue', '复古蓝': 'blue', '青': 'blue', '蓝绿': 'blue',
    '雾蓝': 'blue', '牛仔': 'blue', '湖': 'blue', 

    '藏青': 'navyblue', '深蓝': 'navyblue', '藏蓝': 'navyblue', '深青': 'navyblue',
    
    '绿': 'green', '浅绿': 'green', '豆绿': 'green', '青绿': 'green',
    '牛油果绿': 'green', '果绿': 'green', '灰绿': 'green', '橄榄绿': 'green',
    '抹茶绿': 'green', '薄荷绿': 'green', '牛油果': 'green', '抹茶': 'green',
    '橄榄': 'green', '薄荷': 'green', '芥末': 'green', 

    '军绿': 'olive', '墨绿': 'olive', '深绿': 'olive', '迷彩': 'olive',

    '黄': 'yellow', '姜黄': 'yellow', '柠檬黄': 'yellow', '浅黄': 'yellow',

    '橘': 'orange', '桔': 'orange', '橙': 'orange', '橘红': 'orange',
    '桔红': 'orange', '橙红': 'orange', '橘黄': 'orange', '桔黄': 'orange',
    '橙黄': 'orange', '琥珀': 'orange', '珊瑚': 'orange', '南瓜': 'orange',

    '杏': 'beige', '卡其': 'beige', '卡': 'beige', '浅卡其': 'beige', 
    '米白': 'beige', '米': 'beige', '驼': 'beige', '米黄': 'beige',
    '米杏': 'beige', '香槟': 'beige', '燕麦': 'beige', '浅杏': 'beige',
    '浅咖': 'beige', '浅米': 'beige', '浅驼': 'beige', '浅卡': 'beige',
    '浅米黄': 'beige', '米驼': 'beige', '肉': 'beige', '肤': 'beige',
    '金': 'beige', '奶茶': 'beige', '裸': 'beige', '亚麻': 'beige',
    '坨': 'beige', '沙': 'beige', '香草': 'beige', '奶油': 'beige',
    '麻': 'beige', '茶': 'beige', '浅椰': 'beige', 


    '棕': 'brown', '咖啡': 'brown', '咖': 'brown', '深咖': 'brown',
    '深卡其': 'brown', '焦糖': 'brown', '褐': 'brown', '深褐': 'brown',
    '巧克力': 'brown', '栗': 'brown', '啡': 'brown', '拿铁': 'brown',
    '摩卡': 'brown', '椰': 'brown',
}


color2label = {
    'black': 0, 'white': 1, 'gray': 2, 'red': 3,
    'pink': 4, 'purple': 5, 'blue': 6, 'navyblue': 7,
    'green': 8, 'olive': 9, 'yellow': 10, 'orange': 11,
    'beige': 12, 'brown': 13,
}


# friend_color = {
#     # 'A': ('B') means loss won't be count when predicting A as B
#     'red':      ['pink','purple', 'orange'],
#     'pink':     ['red', 'purple'],
#     'purple':   ['red', 'pink'],
#     'orange':   ['red', 'yellow'],
#     'yellow':   ['orange'],
#     'blue':     ['navyblue'],
#     'navyblue': ['blue'],
#     'green':    ['olive'],
#     'olive':    ['green'],
#     'beige':    ['brown', 'white'],
#     'brown':    ['beige'],
#     'white':    ['beige'],
# }


# friend_label = {
#     3:  [4, 5, 11],
#     4:  [3, 5],
#     5:  [3, 4],
#     11: [3, 10],
#     10: [11],
#     6:  [7],
#     7:  [6],
#     8:  [9],
#     9:  [8],
#     12: [13, 1],
#     13: [12],
#     1: [12],
# }


import json
import os
json_dir = './json/'
if not os.path.exists(json_dir):
    os.makedirs(json_dir)
with open(json_dir + 'word2color.json', 'w', encoding='utf-8') as f:
    json.dump(word2color, f, ensure_ascii=False, indent=4)
with open(json_dir + 'color2label.json', 'w', encoding='utf-8') as f:
    json.dump(color2label, f, ensure_ascii=False, indent=4)
# with open(json_dir + 'friend_color.json', 'w', encoding='utf-8') as f:
#     json.dump(friend_color, f, ensure_ascii=False, indent=4)
# with open(json_dir + 'friend_label.json', 'w', encoding='utf-8') as f:
#     json.dump(friend_label, f, ensure_ascii=False, indent=4)