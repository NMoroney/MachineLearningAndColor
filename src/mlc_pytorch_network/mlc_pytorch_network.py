# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from sklearn.model_selection import train_test_split

import sys
sys.path.insert(0, '../')
import mlc_utilities as mlc


def train_network():

    path_zip = "../../data/"
    name_zip = "mlcolor_11_terms_min_670_rgbn.tsv.zip"

    lines = mlc.zip_to_lines(path_zip, name_zip)
    rgbs, names = mlc.split_rgbn(lines, '\t')
    unique_names, to_index, to_name, classes = mlc.to_classes(names)
        
    X = np.divide(np.array(rgbs), 255.0)

    indices = []
    for name in names:
        indices.append(to_index[name])

    Y = np.array(indices)

    X_train, X_test, Y_train, Y_test = (
        train_test_split(X, Y, test_size=0.33, random_state=42))

    class Data(Dataset):
        def __init__(self, X_train, y_train):
            self.X = torch.from_numpy(X_train.astype(np.float32))
            self.y = torch.from_numpy(y_train).type(torch.LongTensor)
            self.len = self.X.shape[0]

        def __getitem__(self, index):
            return self.X[index], self.y[index]
        def __len__(self):
            return self.len

    traindata = Data(X_train, Y_train)


    batch_size = 100
    trainloader = DataLoader(traindata, batch_size=batch_size, 
                             shuffle=True, num_workers=0)

    # define the neural network, input is normalized RGB and output is
    # color term or name
    #
    input_dim = 3
    hidden_layers_one = 17
    output_dim = 11

    class Network(nn.Module):
        def __init__(self):
            super(Network, self).__init__()
            self.linear1 = nn.Linear(input_dim, hidden_layers_one)
            self.linear2 = nn.Linear(hidden_layers_one, output_dim)
        def forward(self, x):
            x = torch.sigmoid(self.linear1(x))
            x = self.linear2(x)
            return x

    clf = Network()

    print(clf.parameters)


    # train the neural network classifier
    #
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(clf.parameters(), lr=0.1)

    epochs = 301
    for epoch in range(epochs):
        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            optimizer.zero_grad()
            outputs = clf(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        if epoch % 50 == 0:
            rl = running_loss / 2000.0
            print("[ epoch : " + str(epoch) + " ] loss : " + format(rl, '.5f'))

    if True:
        torch.save(clf.state_dict(), 'color_network_11.pth')


    testdata = Data(X_test, Y_test)
    testloader = DataLoader(testdata, batch_size=batch_size, 
                            shuffle=True, num_workers=0)

    dataiter = iter(testloader)
    inputs, labels = next(dataiter)       

    print("labels :\n" + str(labels))

    # single inference and using all test data
    #
    outputs = clf(inputs)
    __, predicted = torch.max(outputs, 1)
    print("predicted :\n" + str(predicted))

    correct, total = 0, 0
    with torch.no_grad():
        for data in testloader:
            inputs, labels = data
            outputs = clf(inputs)
            __, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct // total
    print("accuracy : " + str(accuracy) + "%")


if __name__ == '__main__':
  train_network()

