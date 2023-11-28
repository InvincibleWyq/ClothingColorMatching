import torch
from resnest.torch import resnest50
from torch.utils.data import DataLoader
from torch import nn
from dataset import ClothesColorDataset
from train_model import train_model

img_tensor_dir = '../tensor_data/train_img.pt'
label_tensor_dir = '../tensor_data/train_label.pt'
train_data = ClothesColorDataset(img_tensor_dir, label_tensor_dir)

num_types = 14

net = resnest50(pretrained=True)
net.fc = nn.Linear(net.fc.in_features, num_types)
nn.init.xavier_uniform_(net.fc.weight)

lr, num_epochs, batch_size, weight_decay = 1e-4, 50, 128, 1e-3
optimizer = torch.optim.AdamW(net.parameters(), lr=lr, weight_decay=weight_decay)
train_iter = DataLoader(train_data, batch_size, shuffle=True, num_workers=4, drop_last=True)

train_model(net, train_iter, nn.CrossEntropyLoss(), optimizer, coslr=False, num_epochs=num_epochs, device=torch.device('cuda'), save_dir = '../model/', model_name = 'ResNeSt50_pretrained_nobalanced_cosine')

