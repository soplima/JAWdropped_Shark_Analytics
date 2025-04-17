#%%
import pandas as pd
# %%
df = pd.read_csv('../data/attacks.csv')
# %%
df
# %%
print(df['Country'].unique())
# %%
def categorize_country(country):
    country = country.strip()  # Remove extra spaces
    
    # Map ambiguous locations and oceans to 'Unknown' or 'Ocean'
    ocean_keywords = ['Ocean', 'Sea', 'Gulf', 'Bay', 'Strait', 'Coral', 'Pacific', 'Atlantic', 'Indian']
    if any(keyword in country for keyword in ocean_keywords):
        return 'Ocean'
    
    unknown_keywords = ['Africa', 'Asia', 'Unknown', 'NaN', 'The Balkans', 'Mediterranean Sea', 'Southwest Pacific Ocean', 'Central Pacific']
    if any(keyword in country for keyword in unknown_keywords):
        return 'Unknown'
    
    # Expanded list of countries and regions to map to broader regions
    country_map = {
        'United States': 'North America',
        'Australia': 'Oceania',
        'Brazil': 'South America',
        'Mexico': 'North America',
        'Philippines': 'Asia',
        'South Africa': 'Africa',
        'United Kingdom': 'Europe',
        'France': 'Europe',
        'Japan': 'Asia',
        'Russia': 'Europe/Asia',
        'Germany': 'Europe',
        'Canada': 'North America',
        'India': 'Asia',
        'Egypt': 'Africa',
        'England': 'Europe',
        'Thailand': 'Asia',
        'Costa Rica': 'North America',
        'Maldives': 'Asia',
        'Bahamas': 'North America',
        'New Caledonia': 'Oceania',
        'Ecuador': 'South America',
        'Malaysia': 'Asia',
        'Libya': 'Africa',
        'Cuba': 'North America',
        'Mauritius': 'Africa',
        'New Zealand': 'Oceania',
        'Spain': 'Europe',
        'Samoa': 'Oceania',
        'Solomon Islands': 'Oceania',
        'Japan': 'Asia',
        'Egypt': 'Africa',
        'St Helena, British Overseas Territory': 'Africa',
        'Comoros': 'Africa',
        'Reunion': 'Africa',
        'French Polynesia': 'Oceania',
        'United Kingdom': 'Europe',
        'United Arab Emirates': 'Asia',
        'Indonesia': 'Asia',
        'China': 'Asia',
        'Colombia': 'South America',
        'Cape Verde': 'Africa',
        'Fiji': 'Oceania',
        'Dominican Republic': 'Caribbean',
        'Cayman Islands': 'Caribbean',
        'Aruba': 'Caribbean',
        'Mozambique': 'Africa',
        'Puerto Rico': 'Caribbean',
        'Italy': 'Europe',
        'Greece': 'Europe',
        'St. Martin': 'Caribbean',
        'France': 'Europe',
        'Papua New Guinea': 'Oceania',
        'Trinidad & Tobago': 'Caribbean',
        'Kiribati': 'Oceania',
        'Israel': 'Asia',
        'Diego Garcia': 'Indian Ocean',
        'Taiwan': 'Asia',
        'Jamaica': 'Caribbean',
        'Palestinian Territories': 'Asia',
        'Guam': 'Oceania',
        'Seychelles': 'Africa',
        'Belize': 'Central America',
        'Nigeria': 'Africa',
        'Tonga': 'Oceania',
        'Scotland': 'Europe',
        'Canada': 'North America',
        'Croatia': 'Europe',
        'Saudi Arabia': 'Asia',
        'Chile': 'South America',
        'Antigua': 'Caribbean',
        'Kenya': 'Africa',
        'Russia': 'Europe/Asia',
        'Turks & Caicos': 'Caribbean',
        'United Arab Emirates (Uae)': 'Asia',
        'Azores': 'Europe',
        'South Korea': 'Asia',
        'Malta': 'Europe',
        'Vietnam': 'Asia',
        'Madagascar': 'Africa',
        'Panama': 'Central America',
        'Somalia': 'Africa',
        'Nevis': 'Caribbean',
        'British Virgin Islands': 'Caribbean',
        'Norway': 'Europe',
        'Senegal': 'Africa',
        'Yemen': 'Asia',
        'Gulf Of Aden': 'Africa/Asia',
        'Sierra Leone': 'Africa',
        'St. Maartin': 'Caribbean',
        'Grand Cayman': 'Caribbean',
        'Liberia': 'Africa',
        'Vanuatu': 'Oceania',
        'Mexico ': 'North America',
        'Honduras': 'Central America',
        'Venezuela': 'South America',
        'Sri Lanka': 'Asia',
        'Tonga': 'Oceania',
        'Uruguay': 'South America',
        'India': 'Asia',
        'Micronesia': 'Oceania',
        'Caribbean Sea': 'Caribbean',
        'Okinawa': 'Asia',
        'Tanzania': 'Africa',
        'Marshall Islands': 'Oceania',
        'Egypt / Israel': 'Africa/Asia',
        'Northern Arabian Sea': 'Asia',
        'Hong Kong': 'Asia',
        'El Salvador': 'Central America',
        'Angola': 'Africa',
        'Bermuda': 'North America',
        'Montenegro': 'Europe',
        'Iran': 'Asia',
        'Tunisia': 'Africa',
        'Namibia': 'Africa',
        'North Atlantic Ocean': 'Ocean',
        'Portugal': 'Europe',
        'South China Sea': 'Asia',
        'Bangladesh': 'Asia',
        'Palau': 'Oceania',
        'Western Samoa': 'Oceania',
        'Pacific Ocean ': 'Ocean',
        'British Isles': 'Europe',
        'Grenada': 'Caribbean',
        'Iraq': 'Asia',
        'Turkey': 'Asia',
        'Singapore': 'Asia',
        'New Britain': 'Oceania',
        'Sudan': 'Africa',
        'Johnston Island': 'Pacific Ocean',
        'South Pacific Ocean': 'Ocean',
        'New Guinea': 'Oceania',
        'Red Sea': 'Africa/Asia',
        'North Pacific Ocean': 'Ocean',
        'Federated States Of Micronesia': 'Oceania',
        'Mid Atlantic Ocean': 'Ocean',
        'Admiralty Islands': 'Oceania',
        'British West Indies': 'Caribbean',
        'South Atlantic Ocean': 'Ocean',
        'Persian Gulf': 'Asia',
        'Red Sea / Indian Ocean': 'Africa/Asia',
        'Pacific Ocean': 'Ocean',
        'North Sea': 'Europe',
        'Nicaragua ': 'Central America',
        'Maldive Islands': 'Asia',
        'American Samoa': 'Oceania',
        'Andaman / Nicobar Islandas': 'Asia',
        'Gabon': 'Africa',
        'Mayotte': 'Africa',
        'North Atlantic Ocean': 'Ocean',
        'The Balkans': 'Europe',
        'Sudan?': 'Africa',
        'Argentina': 'South America',
        'Martinique': 'Caribbean',
        'Indian Ocean': 'Ocean',
        'Guatemala': 'Central America',
        'Netherlands Antilles': 'Caribbean',
        'Northern Mariana Islands': 'Oceania',
        'Iran / Iraq': 'Asia',
        'Java': 'Asia',
        'Philippines': 'Asia',
        'Nicaragua': 'Central America',
        'Central Pacific': 'Ocean',
        'Solomon Islands / Vanuatu': 'Oceania',
        'Southwest Pacific Ocean': 'Ocean',
        'Bay Of Bengal': 'Asia',
        'Mid-Pacifc Ocean': 'Ocean',
        'Slovenia': 'Europe',
        'Curacao': 'Caribbean',
        'Iceland': 'Europe',
        'Italy / Croatia': 'Europe',
        'Barbados': 'Caribbean',
        'Monaco': 'Europe',
        'Guyana': 'South America',
        'Haiti': 'Caribbean',
        'San Domingo': 'Caribbean',
        'Ireland': 'Europe',
        'Kuwait': 'Asia',
        'Yemen ': 'Asia',
        'Reunion Island': 'Africa',
        'Falkland Islands': 'South America',
        'Crete': 'Europe',
        'Cyprus': 'Europe',
        'Egypt ': 'Africa',
        'West Indies': 'Caribbean',
        'Burma': 'Asia',
        'Lebanon': 'Asia',
        'Paraguay': 'South America',
        'British New Guinea': 'Oceania',
        'Ceylon': 'Asia',
        'Ocean': 'Ocean',
        'Georgia': 'North America',
        'Syria': 'Asia',
        'Tuvalu': 'Oceania',
        'Indian Ocean?': 'Ocean',
        'Guinea': 'Africa',
        'Andaman Islands': 'Asia',
        'Equatorial Guinea / Cameroon': 'Africa',
        'Cook Islands': 'Oceania',
        'Tobago': 'Caribbean',
        'Peru': 'South America',
        'Africa': 'Africa',
        'Algeria': 'Africa',
        'Coast Of Africa': 'Africa',
        'Tasman Sea': 'Oceania',
        'Ghana': 'Africa',
        'Greenland': 'North America',
        'Mediterranean Sea': 'Ocean',
        'Sweden': 'Europe',
        'Roatan': 'Central America',
        'Between Portugal & India': 'Ocean',
        'Djibouti': 'Africa',
        'Bahrein': 'Asia',
        'Korea': 'Asia',
        'Red Sea?': 'Africa/Asia',
        'Asia?': 'Asia',
        'Ceylon (Sri Lanka)': 'Asia'
    }
    
    # Map the country to a broader region if available
    return country_map.get(country, 'Other/Unknown')
# %%
df['Country'] = df['Country'].astype(str)

df['CleanedCountry'] = df['Country'].apply(categorize_country)

# Now group by the new cleaned country column and analyze
attacksByCountry = df.groupby('CleanedCountry').size().reset_index(name='Count')

# %%
df['Country'].dtype
# %%
df
# %%
# %%
print(df['Country'].unique())
# %%
# 1. Ensure every Country is a string (so .strip() won’t fail)
df['Country'] = df['Country'].fillna('Unknown').astype(str)

# 2. Apply your categorization
df['CleanedCountry'] = df['Country'].apply(categorize_country)

# 3. See what unique regions you now have
print(df['CleanedCountry'].unique())

# 4. And—most importantly—see how many attacks per region:
print(df['CleanedCountry'].value_counts())

# %%
df
# %%
df.drop(columns=['Country'], inplace=True)
# %%
dfSharks = df
# %%
dfSharks
# %%
dfSharks.to_csv('../data/attacks.csv', index=False)
# %%
