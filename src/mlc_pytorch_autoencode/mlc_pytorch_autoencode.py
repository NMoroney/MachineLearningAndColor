# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import zipfile
from io import StringIO
import pandas as pd

import torch
from torch import nn, optim
import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from sklearn.preprocessing import MinMaxScaler

print("pytorch - spectra autoencoder :")


path_zip = "../../data/"
name_zip = "mlcolor_osa_uniform_color_scales_spectra.tsv.zip"

with zipfile.ZipFile(path_zip + name_zip) as archive :
    item = archive.read(name_zip[:-4])
    s = item.decode()
    tsv = StringIO(s)
    df = pd.read_csv(tsv, sep="\t", header=None, skiprows=1)

ns = range(0,5,1)
df.drop(df.columns[ns], axis=1, inplace=True)
df = df / 100.0

X = df.to_numpy()

print(X)
print(X.shape)

device = ('cuda' if torch.cuda.is_available() else 'cpu')
x = torch.from_numpy(X).to(device)
print(device)

h1 = 21
h2 = 11
class Autoencoder(nn.Module):

    def __init__(self, in_shape, enc_shape):
        super(Autoencoder, self).__init__()
        
        self.encode = nn.Sequential(
            nn.Linear(in_shape, h1),
            nn.ReLU(True),
            nn.Linear(h1, h2),
            nn.ReLU(True),
            nn.Linear(h2, enc_shape),
        )
        
        self.decode = nn.Sequential(
            nn.BatchNorm1d(enc_shape),
            nn.Linear(enc_shape, h1),
            nn.ReLU(True),
            nn.Linear(h1, h2),
            nn.ReLU(True),
            nn.Linear(h2, in_shape),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        x = self.encode(x)
        x = self.decode(x)
        return x
    
encoder = Autoencoder(in_shape=36, enc_shape=3).double().to(device)

error = nn.MSELoss()

optimizer = optim.Adam(encoder.parameters())

def train(model, error, optimizer, n_epochs, x):
    model.train()
    for epoch in range(1, n_epochs + 1):
        optimizer.zero_grad()
        output = model(x)
        loss = error(output, x)
        loss.backward()
        optimizer.step()
        
        if epoch % 2000 == 0:
            print("epoch : " + str(epoch) + " - loss : " + 
                   format(loss.item(), '.4g'))

train(encoder, error, optimizer, 20000, x)

with torch.no_grad():
    encoded = encoder.encode(x)
    decoded = encoder.decode(encoded)
    mse = error(decoded, x).item()
    enc = encoded.cpu().detach().numpy()
    dec = decoded.cpu().detach().numpy()

if False:
    fig = plt.figure(figsize=(15,6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(dec[:,0], dec[:,1], dec[:,2], alpha=0.2)
    plt.title('Decoded')
    plt.axis('equal')
    plt.show()


print(dec)
print(dec.shape)

n = 256

print(dec[n,:])

rs = dec[n,:]
nm = range(380,740,10)

if True:
    plt.plot(nm, rs, label="autoencoded")
    plt.plot(nm, X[n,:], label="original")
    plt.xlabel("Nanometers")
    plt.ylabel("Reflectance")
    plt.title("Spectra from OSA Uniform Color Scales")
    plt.legend()
    plt.savefig("mlc_osa_ucs_autoencode-01.jpg")
    plt.show()

