#%%
import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
from calendar import month_name
#%%
app = dash.Dash(__name__)
#%%
data = pd.read_csv('../data/attacks.csv')
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
    template='plotly_dark',
    plot_bgcolor='rgb(18, 18, 18)',
    paper_bgcolor='rgb(18, 18, 18)',
    hovermode='x unified',
    margin=dict(l=40, r=40, t=40, b=40)
)

fig.show()
#%%
#*Where are the global hotspots for shark attacks? (heatmap-style)
# Get top 10 countries excluding 'Unknown'
attacksByCountry = df['country'].value_counts().reset_index()
attacksByCountry.columns = ['country', 'Count']
filtered_country = attacksByCountry[attacksByCountry['country'] != 'Unknown']
top10countries = filtered_country.head(10)

# Plotly bar chart
fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=top10countries['country'],
    y=top10countries['Count'],
    marker=dict(color='cyan'),
    name='Top 10 Countries by Shark Attacks'
))

fig2.update_layout(
    title='Top 10 Countries by Shark Attacks',
    title_x=0.5,
    xaxis_title='Country',
    yaxis_title='Number of Attacks',
    template='plotly_dark',
    plot_bgcolor='rgb(18, 18, 18)',
    paper_bgcolor='rgb(18, 18, 18)',
    hovermode='x unified',
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis_tickangle=-45
)
#*What months or seasons have the highest frequency of attacks?

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.month_name()
attacksByMonth = df.groupby('Month').size().reset_index(name='Count')
ordered_months = list(month_name[1:]) 
attacksByMonth['Month'] = pd.Categorical(attacksByMonth['Month'], categories=ordered_months, ordered=True)
# Sort the dataframe based on the month order
attacksByMonth = attacksByMonth.sort_values('Month')

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=attacksByMonth['Month'],
    y=attacksByMonth['Count'],
    marker=dict(color='cyan'),
    name='Shark Attacks by Month'
))

fig3.update_layout(
    title='Shark Attacks by Month',
    title_x=0.5,
    xaxis_title='Month',
    yaxis_title='Number of Attacks',
    template='plotly_dark',
    plot_bgcolor='rgb(18, 18, 18)',
    paper_bgcolor='rgb(18, 18, 18)',
    hovermode='x unified',
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis_tickangle=-45
)
#%%
#*What human activities are most associated with shark attacks?
activityAttackRelation = df.groupby('ActivityGroup').size().reset_index(name='Count')
filtered_activities = activityAttackRelation[activityAttackRelation['ActivityGroup'].str.strip() != 'Other/Unknown']

# Plotly bar chart
fig4 = go.Figure()
fig4.add_trace(go.Bar(
    x=filtered_activities['ActivityGroup'],
    y=filtered_activities['Count'],
    marker=dict(color='cyan'),
    name='Shark Attacks by Activity'
))

fig4.update_layout(
    title='Shark Attacks by Activity',
    title_x=0.5,
    xaxis_title='Activity',
    yaxis_title='Number of Attacks',
    template='plotly_dark',
    plot_bgcolor='rgb(18, 18, 18)',
    paper_bgcolor='rgb(18, 18, 18)',
    hovermode='x unified',
    margin=dict(l=40, r=40, t=40, b=80),
    xaxis_tickangle=-45
)
#%%
#*Do attacks happen more often to men or women?
attackByGender = df['Sex'].value_counts().reset_index()
attackByGender.columns = ['Sex', 'Count']
filtered_gender = attackByGender[attackByGender['Sex'] != 'Unknown']

# Plotly bar chart
fig5 = go.Figure()
fig5.add_trace(go.Bar(
    x=filtered_gender['Sex'],
    y=filtered_gender['Count'],
    marker=dict(color='cyan'),
    name='Shark Attacks by Gender'
))

fig5.update_layout(
    title='Shark Attacks by Gender',
    title_x=0.5,
    xaxis_title='Gender',
    yaxis_title='Number of Attacks',
    template='plotly_dark',
    plot_bgcolor='rgb(18, 18, 18)',
    paper_bgcolor='rgb(18, 18, 18)',
    hovermode='x unified',
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis_tickangle=0
)

#*What time of day do most attacks occur?
attackTime = df['TimePeriod'].value_counts().reset_index()
attackTime.columns = ['TimePeriod', 'Count']
filtered_time = attackTime[attackTime['TimePeriod'] != 'Unknown']

# Define order
ordered_periods = ["Morning", "Afternoon", "Evening", "Overnight"]
filtered_time['TimePeriod'] = pd.Categorical(
    filtered_time['TimePeriod'],
    categories=ordered_periods,
    ordered=True
)
filtered_time = filtered_time.sort_values('TimePeriod')

# Create Plotly bar chart
fig6 = go.Figure()
fig6.add_trace(go.Bar(
    x=filtered_time['TimePeriod'],
    y=filtered_time['Count'],
    marker=dict(color='cyan'),
    name='Shark Attacks by Time of Day'
))

fig6.update_layout(
    title='Shark Attacks by Time of Day',
    title_x=0.5,
    xaxis_title='Time of Day',
    yaxis_title='Number of Attacks',
    template='plotly_dark',
    plot_bgcolor='rgb(18, 18, 18)',
    paper_bgcolor='rgb(18, 18, 18)',
    hovermode='x unified',
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis_tickangle=0
)
#%%
#*Are there specific beaches or coastlines that are more dangerous than others?
attacksByLocation = df['Location'].value_counts().reset_index()
attacksByLocation.columns = ['Location', 'Count']
filtered_Location = attacksByLocation[attacksByLocation['Location'] != 'Unknown']
top10L = filtered_Location.head(10)

# Create Plotly bar chart
fig7 = go.Figure()
fig7.add_trace(go.Bar(
    x=top10L['Location'],
    y=top10L['Count'],
    marker=dict(color='cyan'),
    name='Shark Attacks by Location'
))

fig7.update_layout(
    title='Top 10 Locations with Shark Attacks',
    title_x=0.5,
    xaxis_title='Location',
    yaxis_title='Number of Attacks',
    template='plotly_dark',
    plot_bgcolor='rgb(18, 18, 18)',
    paper_bgcolor='rgb(18, 18, 18)',
    hovermode='x unified',
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis_tickangle=-45
)

#*Which age group (Child/Adult) is most vulnerable to shark attacks? Does this vary by country?
filtered_top10 = df[df['country'].isin(top10countries['country'])]

# Group by AgeGroup and Country
attack_by_age_country = filtered_top10.groupby(['AgeGroup', 'country']).size().reset_index(name='attack_count')
filtered_Age = attack_by_age_country[attack_by_age_country['AgeGroup'] != 'Unknown']

# Pivot to heatmap format
pivot_table = filtered_Age.pivot(index='AgeGroup', columns='country', values='attack_count').fillna(0)

# Plotly Heatmap
fig8 = go.Figure(data=go.Heatmap(
    z=pivot_table.values,
    x=pivot_table.columns,
    y=pivot_table.index,
    colorscale='Blues',
    colorbar=dict(title='Attack Count')
))

fig8.update_layout(
    title='Attacks by Age Group and Top 10 Countries',
    title_x=0.5,
    xaxis_title='Country',
    yaxis_title='Age Group',
    template='plotly_dark',
    plot_bgcolor='rgb(18, 18, 18)',
    paper_bgcolor='rgb(18, 18, 18)',
    margin=dict(l=40, r=40, t=40, b=40)
)

#%%
#*Has the male/female victim ratio changed over decades?
df['Decade'] = (df['Year'] // 10) * 10
filterYear = df[df['Year'] > 1900]

top10Decades = (
    filterYear["Decade"]
    .value_counts()
    .sort_values(ascending=False)
    .head(10)
    .index.tolist()
)

filtered_top10Decades = filterYear[filterYear['Decade'].isin(top10Decades)]

atttackGenderRatio = (
    filtered_top10Decades
    .groupby(['Sex', 'Decade'])
    .size()
    .reset_index(name='attack_count')
)

filtered_gender_ratio = atttackGenderRatio[atttackGenderRatio['Sex'] != 'Unknown']

# Create separate dataframes for male and female
male_data = filtered_gender_ratio[filtered_gender_ratio['Sex'] == 'Male']
female_data = filtered_gender_ratio[filtered_gender_ratio['Sex'] == 'Female']

fig9 = go.Figure()

fig9.add_trace(go.Scatter(
    x=male_data['Decade'],
    y=male_data['attack_count'],
    mode='lines',
    name='Male',
    line=dict(color='cyan', width=3)
))

fig9.add_trace(go.Scatter(
    x=female_data['Decade'],
    y=female_data['attack_count'],
    mode='lines',
    name='Female',
    line=dict(color='pink', width=3)
))

fig9.update_layout(
    title='Victim Gender Ratio Over Decades',
    title_x=0.5,
    xaxis_title='Decade',
    yaxis_title='Attack Count',
    template='plotly_dark',
    plot_bgcolor='rgb(18, 18, 18)',
    paper_bgcolor='rgb(18, 18, 18)',
    margin=dict(l=40, r=40, t=40, b=40)
)
#%%
#*Are certain age groups or genders more likely to survive an attack?
filtered_df = df[
    (df['Sex'].notna()) & 
    (df['AgeGroup'].notna()) & 
    (df['Injury'].notna()) &
    (df['Sex'] != 'Unknown') & 
    (df['AgeGroup'] != 'Unknown') & 
    (df['Injury'] != 'Unknown')
]

# Create combined group column
filtered_df['SexageGroup'] = (
    filtered_df['Sex'].astype(str) + ' ' + filtered_df['AgeGroup'].astype(str)
)

# Group by SexageGroup and Injury
injury_group = (
    filtered_df.groupby(['SexageGroup', 'Injury'])
    .size()
    .reset_index(name='attack_count')
)

# Create pivot table for heatmap
pivot_table = injury_group.pivot(
    index='SexageGroup',
    columns='Injury',
    values='attack_count'
).fillna(0)

fig10 = go.Figure(data=go.Heatmap(
    z=pivot_table.values,
    x=pivot_table.columns,
    y=pivot_table.index,
    colorscale='Blues',
    colorbar=dict(title='Attack Count')
))

fig10.update_layout(
    title='Injury Type by Group Ratio',
    title_x=0.5,
    xaxis_title='Injury Type',
    yaxis_title='Sex + Age Group',
    template='plotly_dark',
    plot_bgcolor='rgb(18,18,18)',
    paper_bgcolor='rgb(18,18,18)',
    margin=dict(l=40, r=40, t=40, b=40)
)

fig10.show()

#%%
#* Do attacks from migratory species (e.g., bull sharks) spike during certain months?
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.month_name()
attacksByMonth = df.groupby('Month').size().reset_index(name='Count')
ordered_months = list(month_name[1:])
attacksByMonth['Month'] = pd.Categorical(attacksByMonth['Month'], categories=ordered_months, ordered=True)
attacksByMonth = attacksByMonth.sort_values('Month')

filtered_df = df[
    (df['Species'].notna()) &
    (df['Month'].notna())
]

#Create combined group attack by species
top10 = (
    filtered_df[filtered_df['Species'] != 'Unknown Shark']
    ['Species'].value_counts()
    .head(10)
    .index
)
filtered_df = filtered_df[filtered_df['Species'].isin(top10)]

# Group by SpeciesGroup and Month
species_group = (
    filtered_df.groupby(['Species', 'Month'])
    .size()
    .reset_index(name='attack_count')
)

species_group['Month'] = pd.Categorical(species_group['Month'], categories=ordered_months, ordered=True)


# Create pivot table for heatmap
pivot_table_species = species_group.pivot(
    index='Species',
    columns='Month',
    values='attack_count'
).fillna(0)

fig11 = go.Figure(data=go.Heatmap(
    z=pivot_table_species.values,
    x=pivot_table_species.columns,
    y=pivot_table_species.index,
    colorscale='Blues',
    colorbar=dict(title='Attack Count')
))

fig11.update_layout(
    title='Attacks by Species and Month',
    title_x=0.5,
    xaxis_title='Month',
    yaxis_title='Species',
    template='plotly_dark',
    plot_bgcolor='rgb(18,18,18)',
    paper_bgcolor='rgb(18,18,18)',
    margin=dict(l=40, r=40, t=40, b=40)
)

fig11.show()

#%%
app.layout = html.Div(
    children=[
        html.H1('Shark Attack Analysis Dashboard', style={'textAlign': 'center', 'color': 'white'}),  # White title text

        # First Graph
        dcc.Graph(
            id='shark-attack-graph1',
            figure=fig
        ),
        html.P("""Over the years, there has been a noticeable increase in the number of 
               recorded shark attacks. This trend is likely influenced not only by actual 
               changes in incident rates, but also by improved data collection and greater 
               availability of recent records.""", style={'color': 'white', 'textAlign': 'center'}),


        # Second Graph
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig2
        ),
        html.P("""Most shark attacks were recorded in the United States, likely because data collection 
               efforts have been more concentrated there, making incident records more readily available.""", style={'color': 'white', 'textAlign': 'center'}),
        
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig3
        ),
        html.P("""Shark attacks peak in June, July, and August, likely due to increased water activity 
               during summer vacation in the United States. A smaller peak in January may be explained by summer holidays 
               in Australia, the second country with the highest number of recorded attacks.""", style={'color': 'white', 'textAlign': 'center'}),
        
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig4
        ),
        html.P("""Most shark attacks occurred during water-based activities such as swimming, 
               surfing, or diving. Interestingly, the second-highest number of incidents involved people on boats, where sharks attacked the vessels rather than individuals directly in the water.""", style={'color': 'white', 'textAlign': 'center'}),
        
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig5
        ),
        html.P("""The majority of shark attacks were on males, with a male-to-female ratio of approximately 8:1.""", style={'color': 'white', 'textAlign': 'center'}),
        
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig6
        ),
        html.P("""The majority of shark attacks occurred in the afternoon, followed by the morning, likely due to 
               these being the peak times for water-based activities.""", style={'color': 'white', 'textAlign': 'center'}),
        
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig7
        ),
        html.P("""The location with the most recorded shark attacks is 
               New Smyrna Beach, located in Volusia County, Florida, 
               which is famously known as the 'Shark Bite Capital of the World.""", style={'color': 'white', 'textAlign': 'center'}),
        
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig8
        ),
        html.P("""The distribution of shark attacks by age group reveals 
               that adults are the most affected, followed by teenagers.""", style={'color': 'white', 'textAlign': 'center'}),
        
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig9
        ),
        html.P(""""The distribution of shark attacks over the decades shows a consistent predominance of male victims compared to female victims, highlighting a clear gender disparity in incident occurrence.""", style={'color': 'white', 'textAlign': 'center'}),
        
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig10
        ),
        html.P(""""The distribution indicates that the majority of fatal shark attacks involve adult male victims.""", style={'color': 'white', 'textAlign': 'center'}),
        
        dcc.Graph(
            id='shark-attack-graph2',
            figure=fig11
        ),
        html.P(""""According to the distribution, most attacks are attributed to great white sharks and tend to occur in September. This aligns with their migratory behavior, as white sharks begin
               moving south from their northern feeding grounds when water temperatures drop and food becomes scarce.""", style={'color': 'white', 'textAlign': 'center'}),
        
    ],
    style={'backgroundColor': 'rgb(18, 18, 18)', 'color': 'white', 'padding': '20px'}  # Dark background for the whole page
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8050)
    print("Server is running on http://127.0.0.1:8050")




# %%
