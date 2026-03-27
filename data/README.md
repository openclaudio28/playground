# data/README.md — Dataset Documentation

## Source

**Kaggle House Prices: Advanced Regression Techniques**
- Competition: https://www.kaggle.com/c/house-prices-advanced-regression-techniques
- Download script: `src/data/download.py`

## Files

| File | Rows | Description |
|------|------|-------------|
| `raw/train.csv` | 1,460 | Training set with SalePrice target |
| `raw/test.csv` | 1,459 | Test set (no SalePrice) |
| `raw/data_description.txt` | — | Full column documentation from Kaggle |

> **Note:** Raw CSV files are gitignored. Run `python src/data/download.py` to populate `data/raw/`.

## Target Variable

- **SalePrice** — the property's sale price in USD
- For modeling, always apply `log1p(SalePrice)` to normalize the distribution
- Metric: **RMSE on log-transformed SalePrice** (lower is better)

## Column Overview (81 total)

### Identity
| Column | Type | Description |
|--------|------|-------------|
| Id | int | Row identifier |

### Location & Zoning
| Column | Type | Description |
|--------|------|-------------|
| MSSubClass | int | Type of dwelling |
| MSZoning | str | General zoning classification |
| Street | str | Road access type |
| Alley | str | Alley access type (many NaN = no alley) |
| LotShape | str | General shape of property |
| LandContour | str | Flatness of the property |
| Utilities | str | Type of utilities available |
| LotConfig | str | Lot configuration |
| LandSlope | str | Slope of property |
| Neighborhood | str | Physical locations within Ames city limits |
| Condition1 | str | Proximity to main road or railroad |
| Condition2 | str | Proximity to main road or railroad (if second is present) |

### Dwelling Characteristics
| Column | Type | Description |
|--------|------|-------------|
| BldgType | str | Type of dwelling |
| HouseStyle | str | Style of dwelling |
| OverallQual | int | Overall material and finish quality (1–10) |
| OverallCond | int | Overall condition rating (1–10) |
| YearBuilt | int | Original construction year |
| YearRemodAdd | int | Remodel date |
| RoofStyle | str | Type of roof |
| RoofMatl | str | Roof material |
| Exterior1st | str | Exterior covering on house |
| Exterior2nd | str | Exterior covering (if more than one) |
| MasVnrType | str | Masonry veneer type |
| MasVnrArea | float | Masonry veneer area in sq ft |
| ExterQual | str | Exterior material quality |
| ExterCond | str | Exterior material condition |
| Foundation | str | Foundation type |

### Basement
| Column | Type | Description |
|--------|------|-------------|
| BsmtQual | str | Basement height quality (NaN = no basement) |
| BsmtCond | str | Basement condition |
| BsmtExposure | str | Walkout or garden level basement walls |
| BsmtFinType1 | str | Quality of basement finished area |
| BsmtFinSF1 | float | Type 1 finished square feet |
| BsmtFinType2 | str | Quality of second finished area |
| BsmtFinSF2 | float | Type 2 finished square feet |
| BsmtUnfSF | float | Unfinished basement square feet |
| TotalBsmtSF | float | Total basement square feet |

### Utilities & Systems
| Column | Type | Description |
|--------|------|-------------|
| Heating | str | Heating type |
| HeatingQC | str | Heating quality and condition |
| CentralAir | str | Central air conditioning (Y/N) |
| Electrical | str | Electrical system |

### Above Ground Living Area
| Column | Type | Description |
|--------|------|-------------|
| 1stFlrSF | int | First floor square feet |
| 2ndFlrSF | int | Second floor square feet |
| LowQualFinSF | int | Low quality finished sq ft (all floors) |
| GrLivArea | int | Above grade (ground) living area sq ft |
| BsmtFullBath | float | Basement full bathrooms |
| BsmtHalfBath | float | Basement half bathrooms |
| FullBath | int | Full bathrooms above grade |
| HalfBath | int | Half baths above grade |
| BedroomAbvGr | int | Bedrooms above basement level |
| KitchenAbvGr | int | Kitchens above grade |
| KitchenQual | str | Kitchen quality |
| TotRmsAbvGrd | int | Total rooms above grade (excludes bathrooms) |
| Functional | str | Home functionality rating |
| Fireplaces | int | Number of fireplaces |
| FireplaceQu | str | Fireplace quality (NaN = no fireplace) |

### Garage
| Column | Type | Description |
|--------|------|-------------|
| GarageType | str | Garage location (NaN = no garage) |
| GarageYrBlt | float | Year garage was built |
| GarageFinish | str | Interior finish of the garage |
| GarageCars | float | Size of garage in car capacity |
| GarageArea | float | Size of garage in sq ft |
| GarageQual | str | Garage quality |
| GarageCond | str | Garage condition |

### Outdoor & Lot
| Column | Type | Description |
|--------|------|-------------|
| LotFrontage | float | Linear feet of street connected to property (many NaN) |
| LotArea | int | Lot size in sq ft |
| PavedDrive | str | Paved driveway |
| WoodDeckSF | int | Wood deck area in sq ft |
| OpenPorchSF | int | Open porch area in sq ft |
| EnclosedPorch | int | Enclosed porch area in sq ft |
| 3SsnPorch | int | Three season porch area in sq ft |
| ScreenPorch | int | Screen porch area in sq ft |
| PoolArea | int | Pool area in sq ft |
| PoolQC | str | Pool quality (NaN = no pool) |
| Fence | str | Fence quality (NaN = no fence) |
| MiscFeature | str | Miscellaneous feature not covered in other categories |
| MiscVal | int | Value of miscellaneous feature |

### Sale
| Column | Type | Description |
|--------|------|-------------|
| MoSold | int | Month sold |
| YrSold | int | Year sold |
| SaleType | str | Type of sale |
| SaleCondition | str | Condition of sale |
| SalePrice | int | **TARGET** — sale price in USD (train only) |

## Missing Values (Notable)

| Column | % Missing | Meaning of NaN |
|--------|-----------|----------------|
| PoolQC | 99.5% | No pool |
| MiscFeature | 96.3% | No misc feature |
| Alley | 93.8% | No alley |
| Fence | 80.8% | No fence |
| FireplaceQu | 47.3% | No fireplace |
| LotFrontage | 17.7% | Unknown |
| GarageType/Finish/Qual/Cond | ~5.5% | No garage |
| BsmtQual/Cond/Exposure/FinType | ~2.5% | No basement |
