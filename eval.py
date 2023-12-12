import paddle

from data.graph import GraphGridMesh
from model.graphcast import GraphCastNet
from train_args import TrainingArguments

config = TrainingArguments()


def eval():
    model = GraphCastNet(config)
    print(model)


if __name__ == "__main__":
    eval()
