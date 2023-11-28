import time
import torch
from torch import nn
from torch.optim.lr_scheduler import CosineAnnealingLR

# 部分参考李沐d2l课程提供的jupyter notebook中的训练函数(有删改)：https://zh-v2.d2l.ai/
def train_model(model, dataloaders, LossFunc, optimizer, coslr=False, num_epochs=30, device=torch.device('cuda'), save_dir='../model/', model_name='Unnamed'):
    scheduler = CosineAnnealingLR(optimizer,T_max=10)
    model = nn.DataParallel(model)
    model = model.to(device)
    since = time.time()
    with open(save_dir + 'result.txt', "w") as f:
        f.write('start training...\n')
    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)
        model.train()  # Set model to training mode
        running_loss = 0.0
        running_corrects = 0
        iter = 0
        for inputs, labels in dataloaders:
            inputs = inputs.to(device)
            labels = labels.to(device)
            optimizer.zero_grad()
            with torch.set_grad_enabled(True):
                outputs = nn.Softmax(dim=1)(model(inputs))
                loss = LossFunc(outputs, labels)
                _, preds = torch.max(outputs, 1)
                loss.backward()
                if coslr:
                    scheduler.step()
                else:
                    optimizer.step()
            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)
            iter += 1
            if iter % 100 == 0:
                time_elapsed = time.time() - since
                print('iter: %d, time: %d'%(iter, int(time_elapsed)))
        iter = 0
        epoch_loss = running_loss / len(dataloaders.dataset)
        epoch_acc = running_corrects.double() / len(dataloaders.dataset)
        print('Train Loss: {:.4f} Acc: {:.4f}'.format(epoch_loss, epoch_acc))
        with open(save_dir + 'result_%s.txt'%(model_name), "a") as f:
            f.write('Type:%s \tEpoch:%d \tLoss%.4f \tACC%.4f\n'%(model_name, epoch, epoch_loss, epoch_acc))
        torch.save(model, save_dir + '%s_Epoch_%d.pt'%(model_name, epoch)) # 后续仍使用4GPU推理，则可直接存model
        # torch.save(model.module.state_dict(), save_dir + '%s_Epoch_%d.pt'%(model_name, epoch)) # 便于后续使用单GPU推理

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
    return model


