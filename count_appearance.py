import json
from collections import Counter
from get_label import get_label

data_dir = "../data/medium/"
with open(data_dir + "train_all.json") as f:
    train_data = json.load(f)
with open(data_dir + "test_all.json") as f:
    test_data = json.load(f)

json_dir = "../json/"
with open(json_dir + "word2color.json") as f:
    word2color = json.load(f)
with open(json_dir + "color2label.json") as f:
    color2label = json.load(f)
with open(json_dir + "friend_label.json") as f:
    friend_label = json.load(f)


train_data_packed = {}
for subdict in train_data.values():
    for subsubdict in subdict['imgs_tags']:
        train_data_packed.update(subsubdict)
train_data_packed = list(train_data_packed.values())
train_label_packed = [get_label(word, word2color, color2label) for word in train_data_packed]
train_labels = Counter(train_label_packed).most_common()
idx = [i for i, x in enumerate(train_label_packed) if x == -1]
notfound = [train_data_packed[i] for i in idx]
notfound_sort = Counter(notfound).most_common()
print(len(train_data_packed), len(notfound))



test_data_packed = []
for subdict in test_data.values():
    for subsublist in subdict['optional_tags']:
        test_data_packed.append(subsublist)
test_label_packed = [get_label(word, word2color, color2label) for word in test_data_packed]
test_labels = Counter(test_label_packed).most_common()
idx = [i for i, x in enumerate(test_label_packed) if x == -1]
notfound = [test_data_packed[i] for i in idx]
notfound_sort = Counter(notfound).most_common()
print(len(test_data_packed), len(notfound))
