import streamlit as st
import pandas as pd
import numpy as np
import chart_studio.plotly as py
import plotly.express as px
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go

nobel = pd.read_csv("nobel.csv")

st.title('Nobel Prize')
image3 = Image.open('nobelprize.jpg')
st.image(image3, caption='source: nobelprize.org',
use_column_width=True)
image3
st.write('The Nobel Prize is awarded to those who, during the preceding year, shall have conferred the greatest benefit on mankind. Prizes in physics, chemistry, physiology or medicine, literature and peace have been awarded since 1901 – and economic sciences since 1968')

st.header('Exploratory Data Analysis')

st.write("Click below to display the table of Nobel prize winners over the decade")
df_sample = nobel.head(10)
if st.checkbox('Show Table'):
    df_sample

import seaborn as sns

df_birthcountry = nobel['birth_country'].value_counts().head(10)
st.write("Click below to display the table of The Nationalities of Nobel prize winners over the decade")
if st.checkbox('Show'):
    df_birthcountry
nobel['usa_born_winner'] = nobel['birth_country']=="United States of America"
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()
st.write("Proportion of US Born Nobel Prize Winners")
if st.checkbox('Display'):
    prop_usa_winners 
sns.set()
plt.rcParams['figure.figsize'] = [11, 7]
ax = px.line(nobel, x=prop_usa_winners['decade'], y=prop_usa_winners['usa_born_winner'], title="USA Born Nobel Prize Winners", labels={
	"x" : "Year",
	"y" : "Percentage",
	})
ax.update_layout(yaxis= { 'tickformat': ',.0%'}, hovermode='closest', legend_orientation="h")
st.plotly_chart(ax)
nobel['female_winner'] = nobel['sex']=='Female'
prop_female_winners = nobel.groupby(['decade','category'], as_index=False)['female_winner'].mean()
fig = px.bar(prop_female_winners, x=prop_female_winners["decade"], y=prop_female_winners["female_winner"], color="category", barmode="group", title= "Percentage of Female Winners Throughout A Decade By Category")
fig.update_layout(yaxis= { 'tickformat': ',.0%'}, hovermode='closest', legend_orientation="h")
st.plotly_chart(fig)
st.write("The First Female To Win The Nobel Prize")
from PIL import Image
image = Image.open('Marie.jpg')
st.image(image, caption='source: Slideshare',
use_column_width=True)
First_Female_Nobel= nobel[nobel['female_winner']==True].nsmallest(1,'year')
First_Female_Nobel
st.write("The Laureates That Have Received 2 or More Prizes")
Laureates = nobel.groupby('full_name').filter(lambda x: len(x)>1)
Laureates
nobel['birth_date'] =  pd.to_datetime(nobel['birth_date'], format='%Y-%m-%d')
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year
import statsmodels.api as sm
st.write("Scatterplot Representing The Age of The Nobel Prize Winners")
fig3 = px.scatter(nobel, x="year", y="age",trendline="lowess")
st.plotly_chart(fig3)

sns.lmplot(x='year', y='age', data=nobel, row='category')

fig5 = px.scatter(nobel, x="year", y="age",trendline="lowess", title= "The Age of Winners Throughout A Decade By Category", facet_col = "category")
st.plotly_chart(fig5)
st.write("The oldest winner of a Nobel Prize as of 2016")
Oldestt = nobel.nlargest(1, 'age')
image1 = Image.open('leonidhurwicz.jpg')
st.image(image1, caption='source: Wikipedia',
use_column_width=True)
image1
Oldestt
st.write("The youngest winner of a Nobel Prize as of 2016")
Youngest = nobel.nsmallest(1, 'age')
image2 = Image.open('malala.jpg')
st.image(image2, caption='source: Wikipedia',
use_column_width=True)
image2
Youngest
