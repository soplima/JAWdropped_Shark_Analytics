#%%
import pandas as pd
import numpy as npp
import matplotlib.pyplot as plt
from calendar import month_name
import plotly.express as px
import pycountry
#%%
data = pd.read_csv('../data/attacks.csv')
# %%
df = pd.DataFrame(data)
# %%
df
# %%
#How have shark attacks changed over time?
attacksByYear = df.groupby('Year').size().reset_index(name= 'Count')
attacksByYear = attacksByYear[attacksByYear['Year'] > 1900]
attacksByYear

# %%
plt.figure(figsize=(12,6))
plt.plot(attacksByYear['Year'], attacksByYear['Count'], marker='o', color='blue') #plt.plot(x, y)
plt.title('Shark Attacks Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.grid(True)
plt.tight_layout()
plt.show()


#Which countries or regions have the highest number of shark attacks?
attacksByCountry = df.groupby('CleanedCountry').size().reset_index(name= 'Count')
# %%
attacksByCountry
#%%
# Normalize the values: strip whitespace and lowercase
# Lista de categorias que queremos excluir do gráfico
excluir = ['Unknown', 'Other/Unknown', 'Ocean', 'Africa/Asia', 'Europe/Asia', 'Indian Ocean', 'Pacific Ocean']

# Normalizando e filtrando
attacksByCountry['CleanedCountry'] = attacksByCountry['CleanedCountry'].astype(str).str.strip().str.title()

filtered_attacks = attacksByCountry[~attacksByCountry['CleanedCountry'].isin([x.title() for x in excluir])]

# Plot
plt.figure(figsize=(12, 6))
plt.bar(filtered_attacks['CleanedCountry'], filtered_attacks['Count'], color='blue')
plt.title('Shark Attacks by Country (Excluindo Categorias Genéricas)')
plt.xlabel('Região')
plt.ylabel('Número de Ataques')
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
# %%
#What months or seasons have the highest frequency of attacks?
df
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.month_name()
# %%
df.drop(columns=['YearMonth'], inplace=True)
# %%
attacksByMonth = df.groupby('Month').size().reset_index(name='Count')
# %%
attacksByMonth

ordered_months = list(month_name[1:])  # Skip empty string at index 0

# Convert 'Month' to ordered categorical type
attacksByMonth['Month'] = pd.Categorical(attacksByMonth['Month'], categories=ordered_months, ordered=True)

# Sort the dataframe based on the month order
attacksByMonth = attacksByMonth.sort_values('Month')

# %%
plt.figure(figsize=(12, 6))
plt.bar(attacksByMonth['Month'], attacksByMonth['Count'], color='blue')
plt.title('Shark attacks by Month')
plt.xlabel('Months')
plt.ylabel('Attack Numbers')
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
# %%
#What human activities are most associated with shark attacks?
activityAttackRelation = df.groupby('ActivityGroup').size().reset_index(name= 'Count')
# %%
activityAttackRelation
# %%
filtered_activities = activityAttackRelation[activityAttackRelation['ActivityGroup'].str.strip() != 'Other/Unknown']



plt.figure(figsize=(12, 6))
plt.bar(filtered_activities['ActivityGroup'], filtered_activities['Count'], color='blue')
plt.title('Shark attacks x Activity')
plt.xlabel('Activity')
plt.ylabel('Attack Numbers')
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
# %%


#Do attacks happen more often to men or women?

# %%
attackByGender = df['Sex'].value_counts().reset_index()
attackByGender.columns = ['Sex', 'Count']  # Nomear as colunas

# Filtrar valores 'Unknown'
filtered_gender = attackByGender[attackByGender['Sex'] != 'Unknown']


# %%
plt.figure(figsize=(12, 6))
plt.bar(filtered_gender['Sex'], filtered_gender['Count'], color='blue')
plt.title('Shark attacks x Gender')
plt.xlabel('Sex')
plt.ylabel('Attack Numbers')
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
# %%
df

#What time of day do most attacks occur?
# %%

attackTime = df['TimePeriod'].value_counts().reset_index()
attackTime.columns = ['TimePeriod', 'Count']
# %%
filtered_time = attackTime[attackTime['TimePeriod'] != 'Unknown']

ordered_periods = ["Morning", "Afternoon", "Evening", "Overnight"]

# Transforma a coluna em categórica com ordem
filtered_time['TimePeriod'] = pd.Categorical(
    filtered_time['TimePeriod'],
    categories=ordered_periods,
    ordered=True
)

# Ordena o DataFrame
filtered_time = filtered_time.sort_values('TimePeriod')


# %%
plt.figure(figsize=(12, 6))
plt.bar(filtered_time['TimePeriod'], filtered_time['Count'], color='blue')
plt.title('Shark attack by time')
plt.xlabel('TimePeriod')
plt.ylabel('Attack Numbers')
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
# %%

#Where are the global hotspots for shark attacks? (heatmap-style)
country_counts = df['CleanedCountry'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

valid_countries = [country.name for country in pycountry.countries]


# Cria o mapa
fig = px.choropleth(
    country_counts,
    locations="Country",
    locationmode="country names",
    color="Count",
    color_continuous_scale="Reds",
    title="Global Shark Attack Hotspots"
)
fig.update_layout(
    width=1000,  # ou 1200
    height=600,  # ou 800
    title="Global Shark Attack Hotspots",
    title_x=0.5  # centraliza o título
)


fig.show()
print(df['CleanedCountry'].unique())


# %%
