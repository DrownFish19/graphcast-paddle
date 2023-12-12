from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field


@dataclass
class TrainingArguments:

    data_path: str = field(
        default="/Users/drownfish19/Documents/GitHub/Paddle/GraphCast-data/dataset/source-era5_date-2022-01-01_res-1.0_levels-13_steps-01.nc",
        metadata={"help": "data_path."},
    )
    level: int = field(
        default=13,
        metadata={"help": "level."},
    )
    latent_size: int = field(
        default=512,
        metadata={"help": "latent_size."},
    )
    latent_size: int = field(
        default=512,
        metadata={"help": "latent_size."},
    )
    hidden_layers: int = field(
        default=16,
        metadata={"help": "hidden_layers."},
    )
    gnn_msg_steps: int = field(
        default=16,
        metadata={"help": "gnn_msg_steps."},
    )
    mesh_size: int = field(
        default=6,
        metadata={"help": "mesh_size."},
    )
    resolution: float = field(
        default=0.25,
        metadata={"help": "resolution."},
    )
    radius_query_fraction_edge_length: float = field(
        default=0.6,
        metadata={"help": "radius_query_fraction_edge_length."},
    )
    mesh2grid_edge_normalization_factor: float = field(
        default=None,
        metadata={"help": "mesh2grid_edge_normalization_factor."},
    )

    # 输入数据
    mesh_node_dim: int = field(
        default=3,
        metadata={"help": "mesh_node_dim."},
    )
    grid_node_dim: int = field(
        default=69,
        metadata={"help": "grid_node_dim."},
    )
    mesh_edge_dim: int = field(
        default=4,
        metadata={"help": "mesh_edge_dim."},
    )
    grid2mesh_edge_dim: int = field(
        default=4,
        metadata={"help": "grid2mesh_edge_dim."},
    )
    mesh2grid_edge_dim: int = field(
        default=4,
        metadata={"help": "mesh2grid_edge_dim."},
    )

    # 测试数据
    mesh_node_num: int = field(
        default=2562,
        metadata={"help": "mesh_node_num."},
    )
    grid_node_num: int = field(
        default=32768,
        metadata={"help": "grid_node_num."},
    )
    mesh_edge_num: int = field(
        default=20460,
        metadata={"help": "mesh_edge_num."},
    )
    mesh2grid_edge_num: int = field(
        default=98304,
        metadata={"help": "mesh2grid_edge_num."},
    )
    grid2mesh_edge_num: int = field(
        default=50184,
        metadata={"help": "grid2mesh_edge_num."},
    )
    # 输出结果
    node_output_dim: int = field(
        default=69,
        metadata={"help": "node_output_dim."},
    )

    @property
    def grid_node_emb_dim(self):
        return self.latent_size

    @property
    def mesh_node_emb_dim(self):
        return self.latent_size

    @property
    def mesh_edge_emb_dim(self):
        return self.latent_size

    @property
    def grid2mesh_edge_emb_dim(self):
        return self.latent_size

    @property
    def mesh2grid_edge_emb_dim(self):
        return self.latent_size
