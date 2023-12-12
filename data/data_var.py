# https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5
PRESSURE_LEVELS_ERA5_37 = (
    1,
    2,
    3,
    5,
    7,
    10,
    20,
    30,
    50,
    70,
    100,
    125,
    150,
    175,
    200,
    225,
    250,
    300,
    350,
    400,
    450,
    500,
    550,
    600,
    650,
    700,
    750,
    775,
    800,
    825,
    850,
    875,
    900,
    925,
    950,
    975,
    1000,
)

# https://www.ecmwf.int/en/forecasts/datasets/set-i
PRESSURE_LEVELS_HRES_25 = (
    1,
    2,
    3,
    5,
    7,
    10,
    20,
    30,
    50,
    70,
    100,
    150,
    200,
    250,
    300,
    400,
    500,
    600,
    700,
    800,
    850,
    900,
    925,
    950,
    1000,
)

# https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020MS002203
PRESSURE_LEVELS_WEATHERBENCH_13 = (
    50,
    100,
    150,
    200,
    250,
    300,
    400,
    500,
    600,
    700,
    850,
    925,
    1000,
)

PRESSURE_LEVELS = {
    13: PRESSURE_LEVELS_WEATHERBENCH_13,
    25: PRESSURE_LEVELS_HRES_25,
    37: PRESSURE_LEVELS_ERA5_37,
}

# The list of all possible atmospheric variables. Taken from:
# https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation#ERA5:datadocumentation-Table9
ALL_ATMOSPHERIC_VARS = (
    "potential_vorticity",
    "specific_rain_water_content",
    "specific_snow_water_content",
    "geopotential",
    "temperature",
    "u_component_of_wind",
    "v_component_of_wind",
    "specific_humidity",
    "vertical_velocity",
    "vorticity",
    "divergence",
    "relative_humidity",
    "ozone_mass_mixing_ratio",
    "specific_cloud_liquid_water_content",
    "specific_cloud_ice_water_content",
    "fraction_of_cloud_cover",
)

TARGET_SURFACE_VARS = (
    "2m_temperature",
    "mean_sea_level_pressure",
    "10m_v_component_of_wind",
    "10m_u_component_of_wind",
    "total_precipitation_6hr",
)
TARGET_SURFACE_NO_PRECIP_VARS = (
    "2m_temperature",
    "mean_sea_level_pressure",
    "10m_v_component_of_wind",
    "10m_u_component_of_wind",
)
TARGET_ATMOSPHERIC_VARS = (
    "temperature",
    "geopotential",
    "u_component_of_wind",
    "v_component_of_wind",
    "vertical_velocity",
    "specific_humidity",
)
TARGET_ATMOSPHERIC_NO_W_VARS = (
    "temperature",
    "geopotential",
    "u_component_of_wind",
    "v_component_of_wind",
    "specific_humidity",
)
EXTERNAL_FORCING_VARS = ("toa_incident_solar_radiation",)
GENERATED_FORCING_VARS = (
    "year_progress_sin",
    "year_progress_cos",
    "day_progress_sin",
    "day_progress_cos",
)
FORCING_VARS = EXTERNAL_FORCING_VARS + GENERATED_FORCING_VARS
STATIC_VARS = (
    "geopotential_at_surface",
    "land_sea_mask",
)

TASK_input_variables = (
    TARGET_SURFACE_VARS + TARGET_ATMOSPHERIC_VARS + FORCING_VARS + STATIC_VARS
)
TASK_target_variables = TARGET_SURFACE_VARS + TARGET_ATMOSPHERIC_VARS
TASK_forcing_variables = FORCING_VARS
TASK_pressure_levels = PRESSURE_LEVELS_ERA5_37
TASK_input_duration = ("12h",)

TASK_13_input_variables = (
    TARGET_SURFACE_VARS + TARGET_ATMOSPHERIC_VARS + FORCING_VARS + STATIC_VARS
)
TASK_13_target_variables = TARGET_SURFACE_VARS + TARGET_ATMOSPHERIC_VARS
TASK_13_forcing_variables = FORCING_VARS
TASK_13_pressure_levels = PRESSURE_LEVELS_WEATHERBENCH_13
TASK_13_input_duration = ("12h",)


TASK_13_PRECIP_OUT_input_variables = (
    (
        TARGET_SURFACE_NO_PRECIP_VARS
        + TARGET_ATMOSPHERIC_VARS
        + FORCING_VARS
        + STATIC_VARS
    ),
)
TASK_13_PRECIP_OUT_target_variables = (TARGET_SURFACE_VARS + TARGET_ATMOSPHERIC_VARS,)
TASK_13_PRECIP_OUT_forcing_variables = (FORCING_VARS,)
TASK_13_PRECIP_OUT_pressure_levels = (PRESSURE_LEVELS_WEATHERBENCH_13,)
TASK_13_PRECIP_OUT_input_duration = ("12h",)
