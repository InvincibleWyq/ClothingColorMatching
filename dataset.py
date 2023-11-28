import torch
from torch.utils.data import Dataset

class ClothesColorDataset(Dataset):
    def __init__(self, img_tensor_dir, label_tensor_dir): 
        self.Xlst = torch.load(img_tensor_dir).type(torch.FloatTensor)
        self.ylst = torch.load(label_tensor_dir)
        self.L = self.ylst.shape[0]

    def __len__(self):
        return self.L

    def __getitem__(self, idx):
        return (self.Xlst[idx].reshape(3,224,224), int(self.ylst[idx]))