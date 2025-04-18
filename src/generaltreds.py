#%%
import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
#%%
app = dash.Dash(__name__)
#%%
data = pd.read_csv('../../data/attacks.csv')
# %%
df = pd.DataFrame(data)
# %%
df
# %%
#*How have shark attacks changed over time?
attacksByYear = df.groupby('Year').size().reset_index(name='Count')
attacksByYear = attacksByYear[attacksByYear['Year'] > 1900]


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=attacksByYear['Year'],
    y=attacksByYear['Count'],
    mode='lines+markers',
    marker=dict(color='cyan'),
    name='Shark Attacks'
))

fig.update_layout(
    title='Shark Attacks Over Time',
    title_x=0.5,
    xaxis_title='Year',
    yaxis_title='Number of Attacks',
    template='plotly',
    plot_bgcolor='white',
    hovermode='x unified',
    margin=dict(l=40, r=40, t=40, b=40)
)

fig.show()
#%%
#*Which countries or regions have the highest number of shark attacks?
attacksByCountry = df.groupby('CleanedCountry').size().reset_index(name= 'Count')
#%%
# Normalize the values: strip whitespace and lowercase
# Lista de categorias que queremos excluir do gráfico
excluir = ['Unknown', 'Other/Unknown', 'Ocean', 'Africa/Asia', 'Europe/Asia', 'Indian Ocean', 'Pacific Ocean']

# Normalizando e filtrando
attacksByCountry['CleanedCountry'] = attacksByCountry['CleanedCountry'].astype(str).str.strip().str.title()

filtered_attacks = attacksByCountry[~attacksByCountry['CleanedCountry'].isin([x.title() for x in excluir])]

# Plot
fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=filtered_attacks['CleanedCountry'],
    y=filtered_attacks['Count'],
    marker=dict(color='cyan'),
    name='Shark Attacks by Country'
))

fig2.update_layout(
    title='Shark Attacks by Country ',
    title_x=0.5,  
    xaxis_title='Country',
    yaxis_title='Number of Attacks',
    template='plotly',
    plot_bgcolor='white',
    hovermode='x unified',
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis_tickangle=-45  
)
#*What months or seasons have the highest frequency of attacks?


app.layout = html.Div(
    children=[
        html.H1('Shark Attack Analysis Dashboard', style={'textAlign': 'center'}),

        # First Graph
        dcc.Graph(
            id='shark-attack-graph1',
            figure=fig
        ),

        # Second Graph
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig2
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8050)
    print("Server is running on http://127.0.0.1:8050")

# %%
#*What months or seasons have the highest frequency of attacks?
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
#*What human activities are most associated with shark attacks?
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


#*Do attacks happen more often to men or women?

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

#*What time of day do most attacks occur?
# %%

attackTime = df['TimePeriod'].value_counts().reset_index()
attackTime.columns = ['TimePeriod', 'Count']
# %%
filtered_time = attackTime[attackTime['TimePeriod'] != 'Unknown']

ordered_periods = ["Morning", "Afternoon", "Evening", "Overnight"]

#* Transforma a coluna em categórica com ordem
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

#*Where are the global hotspots for shark attacks? (heatmap-style)
df['country'].value_counts()
# %%
attacksByCountry = df['country'].value_counts().reset_index()
attacksByCountry.columns = ['country', 'Count']
# %%
filtered_country = attacksByCountry[attacksByCountry['country'] != 'Unknown']
top10countries = filtered_country.head(10)

# %%
plt.figure(figsize=(12, 6))
plt.bar(top10countries['country'], top10countries['Count'], color='blue')
plt.title('Attacks by Country')
plt.xlabel('Countries')
plt.ylabel('Attack Numbers')
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
# %%
#*Are there specific beaches or coastlines that are more dangerous than others?
df
# %%
df['Location'].value_counts
# %%
attacksByLocation = df['Location'].value_counts().reset_index()
attacksByLocation.columns = ['Location', 'Count']
# %%
filtered_Location = attacksByLocation[attacksByLocation['Location'] != 'Unknown']
top10L = filtered_Location.head(10)
# %%
plt.figure(figsize=(12, 6))
plt.bar(top10L['Location'], top10L['Count'], color='blue')
plt.title('Attacks by Location')
plt.xlabel('Location')
plt.ylabel('Attack Numbers')
plt.xticks(rotation=45, ha='right')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

# %%
#*Which age group (Child/Adult) is most vulnerable to shark attacks? Does this vary by country?
# %%
df['AgeGroup'].value_counts()
filtered_top10 = df[df['country'].isin(top10countries['country'])]
# %%
attack_by_age_country = filtered_top10.groupby(['AgeGroup', 'country']).size().reset_index(name='attack_count')
filtered_Age = attack_by_age_country[attack_by_age_country['AgeGroup'] != 'Unknown']
# %%
plt.figure(figsize=(12, 6))
pivot_table = filtered_Age.pivot(index='AgeGroup', columns='country', values='attack_count').fillna(0)

sns.heatmap(pivot_table, annot=True, cmap='Blues', cbar=True, fmt='g', linewidths=0.5)

plt.title('Attacks by Age Group and Top 10 Countries')
plt.xlabel('Country')
plt.ylabel('Age Group')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# %%
#*Has the male/female victim ratio changed over decades?
df['Sex'].value_counts()
df['Decade'] = (df['Year'] // 10) * 10
filterYear = df[df['Year'] > 1900]
#%%
top10Decades = (
    filterYear["Decade"]
    .value_counts()
    .sort_values(ascending=False)
    .head(10)
    .index.tolist()
)
# %%
filtered_top10Decades = filterYear[filterYear['Decade'].isin(top10Decades)]
# %%
atttackGenderRatio = (
    filtered_top10Decades
    .groupby(['Sex', 'Decade'])
    .size()
    .reset_index(name='attack_count')
)

filtered_gender_ratio = atttackGenderRatio[atttackGenderRatio['Sex'] != 'Unknown']
# %%
plt.figure(figsize=(12, 6))
pivot_table = filtered_gender_ratio.pivot(index='Sex', columns='Decade', values='attack_count').fillna(0)
sns.heatmap(pivot_table, annot=True, cmap='Blues', cbar=True, fmt='g', linewidths=0.5)

plt.title('Victim Gender Ratio over Decades')
plt.xlabel('Decades')
plt.ylabel('Gender')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# %%

#*Are certain age groups or genders more likely to survive an attack?
df
filtered_df = df[
    (df['Sex'].notna()) & (df['AgeGroup'].notna()) &
    (df['Sex'] != 'Unknown') & (df['AgeGroup'] != 'Unknown')
]

filtered_df['SexageGroup'] = (filtered_df['Sex'].astype(str) + ' ' + filtered_df['AgeGroup'].astype(str))
# %%
filtered_df = filtered_df[filtered_df['Injury'] != 'Unknown']
# %%
injury_group = (
    filtered_df.groupby(['SexageGroup', 'Injury'])
    .size()
    .reset_index(name='attack_count')
)
#%%
pivot_table = injury_group.pivot(
    index='SexageGroup', 
     columns='Injury', 
     values='attack_count'
     ).fillna(0)


#%%
plt.figure(figsize=(14, 8))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='g', linewidths=0.5)


plt.title('Injury Type by Group Ratio') 
plt.xlabel('Injury Type')
plt.ylabel('SexageGroup')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# %%
#* Do attacks from migratory species (e.g., bull sharks) spike during certain months?
