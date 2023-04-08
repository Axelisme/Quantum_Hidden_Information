
"""define a class to calculate em score"""

import torch
from torch import Tensor
from torchmetrics import Metric
from typing import Optional

class EMScore(Metric):
    """define a class to calculate exact match score"""
    is_differentiable: Optional[bool] = None
    higher_is_better: Optional[bool] = True
    full_state_update: bool = False

    def __init__(self):
        super(EMScore, self).__init__()
        self.add_state("correct", default=torch.tensor(0), dist_reduce_fx="sum")
        self.add_state("total", default=torch.tensor(0), dist_reduce_fx="sum")

    def update(self, output: Tensor, label: Tensor) -> None:
        """update the metric"""
        pred = output.argmax(dim=-1)
        self.correct += (pred == label).sum().item()
        self.total += label.size(0)

    def compute(self) -> Tensor:
        """compute the metric"""
        return self.correct / self.total