#%%
import pandas as pd

#Data cleaning
# %%
data = pd.read_csv('../data/attacks.csv', encoding='ISO-8859-1')
df = pd.DataFrame(data)
# %%
df.drop(columns=['Name'], inplace=True)
# %%
df
# %%
df.drop(columns=['Investigator or Source',
                 'Case Number.1',
                 'Case Number.2',
                 'original order',
                 'Unnamed: 22',
                 'Unnamed: 23'], inplace=True)

# %%
df.drop(columns=['pdf',
                 'href formula',
                 'href'], inplace=True)
df
# %%
df.tail()
# %%
condicao = df[df.isna().sum(axis=1) == 13]
df = df.drop(condicao.index)
# %%
df
# %%
df.drop(columns=['Case Number'], inplace=True)
# %%
df
# %%
print(df.columns.tolist())
# %%
df.columns = df.columns.str.strip()

# %%
df['Species'].isna().mean()

# %%
df.isna().mean()
# %%
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# %%
df = df[df['Year'].notna()]
# %%
df.loc[:, 'Year'] = df['Year'].astype(int)
# %%
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
# %%
df.loc[:, 'Age'] = pd.to_numeric(df['Age'], errors='coerce')

# %%
df
# %%

# %%
df
# %%
df['Year'].isna().sum()

# %%
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)

# %%
df
# %%
# %%
print(df.columns)

# %%
df
# %%
print(type(df))

# %%
nat_count = (df['Date'].isna()).sum()
nat_count
# %%
df
# %%
df['Age'].isna().sum()
# %%
df['Age'].dtype
# %%
df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[0, 12, 19, 60, 120],  # Adjusted bins to match your desired categories
    labels=['Child', 'Teen', 'Adult', 'Senior']
)

# %%
df
# %%
df.drop(columns=['Age'], inplace=True)
# %%
df
# %%
df['AgeGroup'] = df['AgeGroup'].fillna('Unknown')

# %%
df['AgeGroup'] = df['AgeGroup'].cat.add_categories('Unknown')

# %%
df['AgeGroup'] = df['AgeGroup'].fillna('Unknown')

# %%
df
# %%
df['Injury'] = df['Injury'].apply(lambda x: 'Fatal injury' if pd.notnull(x) and 'fatal' in str(x).lower() else 
                                  ('Minor injury' if pd.notnull(x) and 'minor' in str(x).lower() else 
                                   ('No injury' if pd.notnull(x) and 'no injury' in str(x).lower() else 'Unknown')))

# %%
df
# %%
df['Fatal (Y/N)'] = df['Fatal (Y/N)'].map({'Y': True, 'N': False})

# %%
df['Fatal (Y/N)'] = df['Fatal (Y/N)'].fillna(False)

# %%
df
# %%
df.columns = df.columns.str.strip()

# %%
print(df['Species'].unique())

# %%
# Drop NaN and sort
species_list = sorted(df['Species'].dropna().unique())

# Print each species value
for species in species_list:
    print(species)

# %%
species_keywords = {
    'angel': 'Angel Shark',
    'basking': 'Basking Shark',
    'blacktip reef': 'Blacktip Reef Shark',
    'blacktip': 'Blacktip Shark',
    'blue whaler': 'Bronze Whaler Shark',
    'bronze whaler': 'Bronze Whaler Shark',
    'bonito': 'Bonito Shark',
    'broadnose sevengill': 'Broadnose Sevengill Shark',
    'bull': 'Bull Shark',
    'caribbean reef': 'Caribbean Reef Shark',
    'carpet': 'Carpet Shark',
    'cookie cutter': 'Cookiecutter Shark',
    'copper': 'Copper Shark',
    'cow': 'Cow Shark',
    'dusky': 'Dusky Shark',
    'galapagos': 'Galapagos Shark',
    'goblin': 'Goblin Shark',
    'gray reef': 'Gray Reef Shark',
    'grey nurse': 'Grey Nurse Shark',
    'grey reef': 'Gray Reef Shark',
    'gummy': 'Gummy Shark',
    'hammerhead': 'Hammerhead Shark',
    'horn': 'Horn Shark',
    'lemon': 'Lemon Shark',
    'leopard': 'Leopard Shark',
    'longfin mako': 'Longfin Mako Shark',
    'mako': 'Shortfin Mako Shark',
    'nurse': 'Nurse Shark',
    'oceanic whitetip': 'Oceanic Whitetip Shark',
    'porbeagle': 'Porbeagle Shark',
    'port jackson': 'Port Jackson Shark',
    'raggedtooth': 'Sand Tiger Shark',
    'reef': 'Reef Shark',
    'salmon': 'Salmon Shark',
    'sandbar': 'Sandbar Shark',
    'sand tiger': 'Sand Tiger Shark',
    'sand shark': 'Sand Shark',
    'sevengill': 'Broadnose Sevengill Shark',
    'shovelnose': 'Shovelnose Guitarfish',
    'silky': 'Silky Shark',
    'silvertip': 'Silvertip Shark',
    'sixgill': 'Sixgill Shark',
    'smooth hound': 'Smoothhound Shark',
    'soupfin': 'Soupfin Shark',
    'spinner': 'Spinner Shark',
    'spurdog': 'Spurdog',
    'tawny nurse': 'Tawny Nurse Shark',
    'thresher': 'Thresher Shark',
    'tiger': 'Tiger Shark',
    'whale': 'Whale Shark',
    'white shark': 'Great White Shark',
    'white': 'Great White Shark',
    'whitetip reef': 'Whitetip Reef Shark',
    'wobbegong': 'Wobbegong Shark',
    'zambezi': 'Bull Shark'
}

# %%
def clean_species(value):
    if pd.isna(value):
        return 'Unknown Shark'
    
    value_lower = value.lower()
    for keyword, clean_name in species_keywords.items():
        if keyword in value_lower:
            return clean_name
    return 'Unknown Shark'

# Apply the cleaning function
df['Species'] = df['Species'].apply(clean_species)

# %%
df
# %%
df['Sex'] = df['Sex'].str.upper().str.strip()
# %%
df['Sex'] = df['Sex'].replace({
    'M': 'Male',
    'F': 'Female',
    'MALE': 'Male',
    'FEMALE': 'Female'
})

# %%
df['Sex'] = df['Sex'].fillna('Unknown')
df.loc[~df['Sex'].isin(['Male', 'Female']), 'Sex'] = 'Unknown'

# %%
df
# %%
df = df.rename(columns={'Fatal (Y/N)': 'Fatal'})

# %%
activities_list = sorted(df['Activity'].dropna().unique())

# Print each species value
for activity in activities_list:
    print(activity)
# %%
df
# %%
