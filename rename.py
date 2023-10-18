import torch
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)


original_list = [
    'adj_aluminum/2005-Ford-Shelby-GR-.jpg',
    'adj_aluminum/50f39c533f536.jpg',
    'adj_aluminum/67111d1328929671-i-n.jpg',
    'adj_aluminum/7075-Aluminum-Alloy-.jpg',
    'adj_aluminum/alumaloy.jpg',
    'adj_aluminum/aluminium-foil-tape2.jpg',
    'adj_aluminum/aluminum-alloys-1.jp.jpg'
]

# 创建一个新的列表，其中双斜杠被替换为单斜杠
new_list = [path.replace('/', '\\') for path in original_list]

# 打印新的列表
print(new_list)
original_string = 'adj_aluminum/2005-Ford-Shelby-GR-.jpg'

# 使用 replace 方法将双斜杠替换为单斜杠
original_string = original_string.replace('/', '\\')



# 打印新的字符串
print(original_string)
print("house-design-exterior-ancient-greek-temple-views-portrait-with-characteristics-of-greek-architecture-designs-great-ancient-building-with-characteristics-of-greek-architecture-designs-600x480.jpg"=="house-design-exterior-ancient-greek-temple-views-portrait-with-characteristics-of-greek-architecture-designs-great-ancient-building-with-characteristics-of-greek-architecture-designs-600x480.jpg")
from PIL import Image
img = Image.open('DataBase\MIT-ST~1\images\ANCIEN~1\HOUSE-~1.JPG').convert('RGB')
# img = Image.open('mit-states\\images\\ancient_building\\house-design-exterior-ancient-greek-temple-views-portrait-with-characteristics-of-greek-architecture-designs-great-ancient-building-with-characteristics-of-greek-architecture-designs-600x480.jpg'
#                  ).convert('RGB')
print(img)