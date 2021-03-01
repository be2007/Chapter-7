# ar6
Repository for code for everything I do with AR6

## Installation
clone the repo and then run

    pip install -e .

This will ensure that all required dependencies are installed. I highly recommend doing this in a virtual environment to not screw up your base python installation. Conda works well.

## Order
- run the notebooks in numerical order. Some later things depend on earlier things (historical temperature attribution requires working group 3 constrained ensemble, which relies on forcing being generated).

## Data
Small datasets ingested by the code are included (`data_input`). Small output datasets are also included (`data_output`). Most large datasets are automatically downloaded by the code into `data_input_large`, but some cannot be. The following files should be downloaded and placed into `data_input_large`:

### Glossac v2.0 stratospheric aerosol optical depth time series
- Obtained from https://asdc.larc.nasa.gov/project/GloSSAC/GloSSAC_2.0 (registration required).
```
$ cksum GloSSAC_V2.0.nc
938562794 482976764 GloSSAC_V2.0.nc
```

### eVolv v3 stratospheric optical depth, 500 BCE to 1900 CE
- Obtained from https://cera-www.dkrz.de/WDCC/ui/cerasearch/entry?acronym=eVolv2k_v3 (registration required).
```
- $ cksum eVolv2k_v3_EVA_AOD_-500_1900_1.nc
3663959754 22244500 eVolv2k_v3_EVA_AOD_-500_1900_1.nc
```

Detailed instructions on where to download these datasets from and the version numbers will be included eventually, ping me if you need it now.

Large datasets generated (e.g. probablistic time series) are not included due to their size. They should be exactly reproducible thanks to fixed random seeds and live in `data_output_large`.

## Credits
- Glen Harris and Mark Ringer for the two layer climate model in `src/ar6/twolayermodel`, and the CMIP6 tunings
- Matt Palmer: figure 7.3
- Bill Collins: figure 7.21
- Piers Forster: figure 7.22
