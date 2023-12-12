import paddle

from data.graph import GraphGridMesh
from model.graphcast import GraphCastNet
from train_args import TrainingArguments

config = TrainingArguments()


graph = GraphGridMesh(
    mesh2mesh_src_index=paddle.randint(
        high=config.mesh_node_num, shape=[config.mesh_edge_num]
    ),
    mesh2mesh_dst_index=paddle.randint(
        high=config.mesh_node_num, shape=[config.mesh_edge_num]
    ),
    grid2mesh_src_index=paddle.randint(
        high=config.grid_node_num, shape=[config.grid2mesh_edge_num]
    ),
    grid2mesh_dst_index=paddle.randint(
        high=config.mesh_node_num, shape=[config.grid2mesh_edge_num]
    ),
    mesh2grid_src_index=paddle.randint(
        high=config.mesh_node_num, shape=[config.mesh2grid_edge_num]
    ),
    mesh2grid_dst_index=paddle.randint(
        high=config.grid_node_num, shape=[config.mesh2grid_edge_num]
    ),
    mesh_num_nodes=config.mesh_node_num,
    grid_num_nodes=config.grid_node_num,
    mesh_num_edges=config.mesh_edge_num,
    grid2mesh_num_edges=config.grid2mesh_edge_num,
    mesh2grid_num_edges=config.mesh2grid_edge_num,
    grid_node_feat=paddle.rand((config.grid_node_num, config.grid_node_dim)),
    mesh_node_feat=paddle.rand((config.mesh_node_num, config.mesh_node_dim)),
    mesh_edge_feat=paddle.rand((config.mesh_edge_num, config.mesh_edge_dim)),
    grid2mesh_edge_feat=paddle.rand(
        (config.grid2mesh_edge_num, config.grid2mesh_edge_dim)
    ),
    mesh2grid_edge_feat=paddle.rand(
        (config.mesh2grid_edge_num, config.mesh2grid_edge_dim)
    ),
)

graphcast_model = GraphCastNet(config)
graph = graphcast_model(graph)

per_variable_level_mean = paddle.rand(
    (config.grid_node_output_dim,), dtype=paddle.float32
)
per_variable_level_std = paddle.rand(
    (config.grid_node_output_dim,), dtype=paddle.float32
)

print(graph.grid_node_feat.shape)
# (32768, 69))
