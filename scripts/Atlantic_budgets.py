import numpy as np
import xarray as xr

import warnings
import CM4Xutils
import sectionate as sec
import regionate as reg
import tosnap

import xbudget
import xwmb

# Read all budget files
def open_budget(year):
    datapath = "/work/hfd/codedev/CM4Xutils/data/coarsened/"
    path = f"{datapath}CM4Xp125_budgets_sigma2_{year}-{year+4}.zarr"
    return xr.open_zarr(path)
    
def drop_time_bounds(ds):
    if ds.time.size==ds.time_bounds.size:
        ds = ds.sel(time=slice("0002", None))
    ds = ds.drop_dims("time_bounds")
    if "time_since_init" in ds.coords:
        ds = ds.swap_dims({"time": "time_since_init"}).reset_coords("time")
    else:
        ds = ds.rename({"time": "time_since_init"})
    return ds
    
def drop_time(ds):
    if ds.time.size==ds.time_bounds.size:
        ds = ds.sel(time_bounds=slice("0002", None))
    else:
        ds = ds.isel(time_bounds=slice(1, None))
    ds = ds.drop_dims("time")
    if "time_bounds_since_init" in ds.coords:
        ds = ds.swap_dims({"time_bounds": "time_bounds_since_init"}).reset_coords("time_bounds")
    else:
        ds = ds.rename({"time_bounds": "time_bounds_since_init"})
    return ds

years = np.arange(1750, 2100, 5)
ds = xr.merge([
    xr.concat([       drop_time(open_budget(year)) for year in years], dim="time_bounds_since_init"),
    xr.concat([drop_time_bounds(open_budget(year)) for year in years], dim="time_since_init"       )
]).rename({"time":"time_historical", "time_bounds":"time_bounds_historical", "time_since_init":"time", "time_bounds_since_init":"time_bounds"})

# Create grid
grid = CM4Xutils.ds_to_grid(ds.fillna(0.))

# Break grid into Atlantic regions
atl = tosnap.grid_atlantic(grid)

for region_name, region in atl.region_dict.items():
    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)
    
        budgets_dict = xbudget.load_preset_budget(model="MOM6_3Donly")
        xbudget.collect_budgets(grid, budgets_dict)

        wmb = xwmb.WaterMassBudget(
            grid,
            budgets_dict,
            region
        )
        wmb.mass_budget(
            "sigma2",
            default_bins=False,
            greater_than=True,
            along_section=True
        )
        region.save["wmt"] = wmb.wmt.drop_dims("time_bounds")
        region.save["wmt"].load()

        # Get transports across each child section
        for child_name, child in region.children.items():
            lons_sect, lats_sect = sec.uvcoords_from_qindices(grid, child.i, child.j)
            child_sect = xr.Dataset(
                {
                    "lon_sect": xr.DataArray(lons_sect, dims=("subsect",)),
                    "lat_sect": xr.DataArray(lats_sect, dims=("subsect",))
                },
                coords = {"subsect": xr.DataArray(np.arange(0,lons_sect.size), dims=("subsect",))}
            )

            dist = sec.distance_on_unit_sphere(
                wmb.grid._ds['convergent_mass_transport_along'].lon_sect,
                wmb.grid._ds['convergent_mass_transport_along'].lat_sect,
                child_sect.lon_sect,
                child_sect.lat_sect
            )
            
            child_mask = (dist <= 1.e3).any("subsect")
            child.save["wmt"] = (
                wmb.grid._ds[['convergent_mass_transport_along']]
                .where(child_mask).sum("sect")
            ).rename({"convergent_mass_transport_along":"convergent_mass_transport"})
            child.save["wmt"].load()

atl.to_grs("../data/")
