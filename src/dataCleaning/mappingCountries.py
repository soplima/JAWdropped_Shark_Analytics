#%%
import pandas as pd
from geopy.geocoders import Nominatim
import pandas as pd
from tqdm import tqdm
import time
# %%

data = pd.read_csv('../../data/attacks.csv')
# %%
df = pd.DataFrame(data)
# %%
df
#%%
# Register tqdm with pandas apply
tqdm.pandas()

# Initialize geocoder and cache
geolocator = Nominatim(user_agent="geo_app")
cache = {}

def get_country(area, location):
    try:
        if pd.isna(area) or pd.isna(location):
            return "Unknown"
        area = str(area).strip()
        location = str(location).strip()
        if not area or not location:
            return "Unknown"
        
        key = (area, location)
        if key in cache:
            return cache[key]

        query = f"{location}, {area}"
        location_data = geolocator.geocode(query, exactly_one=True)
        if location_data:
            country = location_data.address.split(",")[-1].strip()
        else:
            country = "Unknown"

        cache[key] = country
        time.sleep(1)
        return country
    except:
        return "Unknown"



# Apply to your DataFrame (df)
df["country"] = df.progress_apply(lambda row: get_country(row["Area"], row["Location"]), axis=1)
# %%


# %%
print(df['country'].head(20))

# %%
df.to_csv('../../data/attacks.csv', index=False)
# %%
