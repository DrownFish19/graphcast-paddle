import os

import numpy as np
import paddle

from model.graphcast import GraphCastNet
from train_args import TrainingArguments

config = TrainingArguments()


def convert(jax_parameters_path, paddle_parameters_path):
    model = GraphCastNet(config)
    state_dict = model.state_dict()
    state_dict_keys = state_dict.keys()
    print(state_dict_keys)
    for key in state_dict_keys:
        print(key, state_dict[key].shape)

    jax_data = np.load(jax_parameters_path)
    for param_name in jax_data.files:
        if jax_data[param_name].size == 1:
            print(param_name, "\t", jax_data[param_name])
        else:
            print(param_name, "\t", jax_data[param_name].shape)

    paddle_state_dict = {}


if __name__ == "__main__":
    jax_parameters_path = os.path.join(
        "params",
        "GraphCast - ERA5 1979-2017 - resolution 0.25 - pressure levels 37 - mesh 2to6 - precipitation input and output.npz",
    )
    paddle_parameters_path = os.path.join(
        "params",
        "paddle-GraphCast-ERA5-1979-2017-resolution-0.25-pressure-levels-37-mesh-2to6-precipitation-input-and-output.pdparams",
    )

    # convert(jax_parameters_path, paddle_parameters_path)

    # for i in range(16):
    #     print(f"graphcast.processor.processor.{i}.node_layer.layer_norm.bias")
    #     print(f"graphcast.processor.processor.{i}.node_layer.layer_norm.weight")
    #     print(f"graphcast.processor.processor.{i}.node_layer.mlp.0.bias")
    #     print(f"graphcast.processor.processor.{i}.node_layer.mlp.0.weight")
    #     print(f"graphcast.processor.processor.{i}.node_layer.mlp.2.bias")
    #     print(f"graphcast.processor.processor.{i}.node_layer.mlp.2.weight")
