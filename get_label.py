def get_label(word, word2color, color2label):
    # 先查词典，若查不到再看某局部是否能查到
    if len(word)>1 and word[-1]=='色':
        word = word[:-1]

    wordlen = len(word)
    if word in word2color:
        color = word2color[word]
        label = color2label[color]
        return label
    else:
        for partlen in range(wordlen-1, 0, -1):
            for startpos in range(wordlen-partlen, -1, -1):
                part = word[startpos:startpos+partlen]
                if part in word2color:
                    color = word2color[part]
                    label = color2label[color]
                    return label
    return -1