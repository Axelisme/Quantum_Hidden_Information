
"""some tools for the project"""

import torch
import numpy as np
import random
from torch.backends import cudnn

def set_seed(seed: int) -> None:
    """set seed for reproducibility"""
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    cudnn.deterministic = True
    cudnn.benchmark = False

class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

class Result:
    """handle the training result"""
    def __init__(self) -> None:
        self.data = dict()

    def add(self,**result_dict) -> None:
        """add some result"""
        for key,value in result_dict.items():
            if key not in self.data.keys():
                self.data[key] = list()
            self.data[key].append(value)

    def shows(self, keylist) -> None:
        """show the result"""
        for key in keylist:
            print(f'{key}: {self.data[key][-1]:.3f}')

    def show(self, key) -> None:
        """show a result"""
        print(f'{key}: {self.data[key][-1]:.3f}')

    def get(self, key) -> list:
        """get a result"""
        return self.data[key]
