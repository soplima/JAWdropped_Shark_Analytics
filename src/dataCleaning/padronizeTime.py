#%%
import pandas as pd
import numpy as np
import re
# %%
data = pd.read_csv('../data/attacks.csv', encoding='ISO-8859-1')
df = pd.DataFrame(data)
# %%
df
# %%
attackTime = df['Time'].unique()
attackTime
# %%
time_keywords_mapping = {
    # --- Morning ---
    "06h": "Morning",
    "07h": "Morning",
    "08h": "Morning",
    "09h": "Morning",
    "10h": "Morning",
    "11h": "Morning",
    "Early morning": "Morning",
    "Daybreak": "Morning",
    "Dawn": "Morning",
    "Mid morning": "Morning",
    "Morning": "Morning",

    # --- Afternoon ---
    "12h": "Afternoon",
    "13h": "Afternoon",
    "14h": "Afternoon",
    "15h": "Afternoon",
    "After noon": "Afternoon",
    "Noon": "Afternoon",
    "Midday": "Afternoon",
    "Lunchtime": "Afternoon",
    "P.M.": "Afternoon",

    # --- Evening ---
    "16h": "Evening",
    "17h": "Evening",
    "18h": "Evening",
    "19h": "Evening",
    "Late afternoon": "Evening",
    "Evening": "Evening",
    "Early evening": "Evening",

    # --- Overnight ---
    "20h": "Overnight",
    "21h": "Overnight",
    "22h": "Overnight",
    "23h": "Overnight",
    "00h": "Overnight",
    "01h": "Overnight",
    "02h": "Overnight",
    "03h": "Overnight",
    "04h": "Overnight",
    "05h": "Overnight",
    "Midnight": "Overnight",
    "After midnight": "Overnight",
    "Night": "Overnight",
    "Shortly after midnight": "Overnight",
}


# %%
def map_time_to_period(value: str) -> str:
    for keyword, period in time_keywords_mapping.items():
        if keyword.lower() in value.lower():
            return period
    return "Unknown"

df['TimePeriod'] = df['Time'].astype(str).apply(map_time_to_period)
# %%
df
# %%
df['TimeOfDay'].value_counts()
# %%
df.to_csv('../data/attacks.csv', index=False)
# %%
df
# %%
