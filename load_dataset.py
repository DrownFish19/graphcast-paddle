import h5py
import netCDF4 as nc
import numpy as np

_SEC_PER_HOUR = 3600
_HOUR_PER_DAY = 24
SEC_PER_DAY = _SEC_PER_HOUR * _HOUR_PER_DAY
_AVG_DAY_PER_YEAR = 365.24219
AVG_SEC_PER_YEAR = SEC_PER_DAY * _AVG_DAY_PER_YEAR

DAY_PROGRESS = "day_progress"
YEAR_PROGRESS = "year_progress"


def get_year_progress(seconds_since_epoch: np.ndarray) -> np.ndarray:
    """Computes year progress for times in seconds.

    Args:
      seconds_since_epoch: Times in seconds since the "epoch" (the point at which
        UNIX time starts).

    Returns:
      Year progress normalized to be in the [0, 1) interval for each time point.
    """

    # Start with the pure integer division, and then float at the very end.
    # We will try to keep as much precision as possible.
    years_since_epoch = (
        seconds_since_epoch / SEC_PER_DAY / np.float64(_AVG_DAY_PER_YEAR)
    )
    # Note depending on how these ops are down, we may end up with a "weak_type"
    # which can cause issues in subtle ways, and hard to track here.
    # In any case, casting to float32 should get rid of the weak type.
    # [0, 1.) Interval.
    return np.mod(years_since_epoch, 1.0).astype(np.float32)


def get_day_progress(
    seconds_since_epoch: np.ndarray,
    longitude: np.ndarray,
) -> np.ndarray:
    """Computes day progress for times in seconds at each longitude.

    Args:
      seconds_since_epoch: 1D array of times in seconds since the 'epoch' (the
        point at which UNIX time starts).
      longitude: 1D array of longitudes at which day progress is computed.

    Returns:
      2D array of day progress values normalized to be in the [0, 1) inverval
        for each time point at each longitude.
    """

    # [0.0, 1.0) Interval.
    day_progress_greenwich = np.mod(seconds_since_epoch, SEC_PER_DAY) / SEC_PER_DAY

    # Offset the day progress to the longitude of each point on Earth.
    longitude_offsets = np.deg2rad(longitude) / (2 * np.pi)
    day_progress = np.mod(
        day_progress_greenwich[..., np.newaxis] + longitude_offsets, 1.0
    )
    return day_progress.astype(np.float32)


def datetime_features(seconds_since_epoch, longitude_offsets):
    year_progress = get_year_progress(seconds_since_epoch)
    day_progress = get_day_progress(second_since_epoch, longitude_offsets)

    year_progress_phase = year_progress * (2 * np.pi)
    day_progress_phase = year_progress * (2 * np.pi)

    returned_data = {
        "year_progress_sin": np.sin(year_progress_phase),
        "year_progress_cos": np.cos(year_progress_phase),
        "day_progress_sin": np.sin(day_progress_phase),
        "day_progress_cos": np.cos(day_progress_phase),
    }

    return returned_data


nc_data_path = "/Users/drownfish19/Documents/GitHub/Paddle/GraphCast-data/dataset/source-era5_date-2022-01-01_res-1.0_levels-37_steps-04.nc"
# nc_dataset = nc.Dataset(nc_data_path

# )


hdf5_data = h5py.File(nc_data_path, "r")

time_var = nc_dataset.variables["datetime"]
longitude_offsets = nc_dataset.variables["lon"][:].data
print()

second_since_epoch = (
    nc.num2date(time_var[:].data, time_var.units)
    .astype("datetime64[s]")
    .astype(np.int64)
)
get_year_progress(second_since_epoch)
get_day_progress(second_since_epoch, longitude_offsets)

print(datetime_features(second_since_epoch, longitude_offsets))
