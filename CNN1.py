import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class CustomCNN(nn.Module):
    def __init__(self):
        super(CustomCNN, self).__init__()

        # Custom 2x2 convolutional layer with 3 kernels, bias=False
        self.conv = nn.Conv2d(1, 3, kernel_size=2, stride=1, padding=0, bias=False)

        # Set kernel weights manually
        with torch.no_grad():
            # Each kernel is of shape (1, 2, 2)
            kernel_weights = torch.tensor([
                [[[1.0, 0.0], [0.0, 1.0]]],   # Kernel 1
                [[[0.0, 1.0], [1.0, 0.0]]],   # Kernel 2
                [[[1.0, 1.0], [1.0, 0.0]]]    # Kernel 3
            ])
            self.conv.weight.copy_(kernel_weights)

        # Add manual bias for after conv
        self.bias = nn.Parameter(torch.tensor([2.0, 2.0, 2.0]))  # Bias = 2 for each kernel

        # Initialize BatchNorm
        self.bn = nn.BatchNorm2d(3)  # eps is 1e-5

        # Fully connected layer
        self.fc = nn.Linear(3, 1, bias=True)
        with torch.no_grad():
            self.fc.weight.fill_(0.5)
            self.fc.bias.fill_(1.0)

    def forward(self, x):
        # shape: (1, 1, 3, 3)
        x = self.conv(x)
        x = x + self.bias.view(1, -1, 1, 1)  # manually add bias
        print(f"After conv:\n{x.detach().cpu().numpy().round(2)}")
        x = self.bn(x)
        print(f"After batch norm:\n{x.detach().cpu().numpy().round(2)}")
        print("BatchNorm stats:")
        print(f"Running mean: {self.bn.running_mean.data}")
        print(f"Running var: {self.bn.running_var.data}")
        print(f"Gamma (weight): {self.bn.weight.data}")
        print(f"Beta (bias): {self.bn.bias.data}")

        x = F.max_pool2d(x, kernel_size=2, stride=2)
        x = x.flatten(start_dim=1)
        x = self.fc(x)
        return x