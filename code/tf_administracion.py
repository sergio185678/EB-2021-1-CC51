# -*- coding: utf-8 -*-
"""TF-administracion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rtRdidPylL4kN0mCz446QFQMWo8AbWpx
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dff = pd.read_json('IN_category_id.json')
dfg = pd.read_csv('INvideos_cc50_202101.csv')
dfg.info()
dff.info()

import random
dfg.dropna(inplace=True)
dfg.reset_index(drop=True,inplace=True)

def create_videoid():
    list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G',
        'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','','-']
    arr=''
    for i in range(11):
        arr+=random.choice(list)
    return arr

for i in range(len(dfg['video_id'])):
    if(len(dfg['video_id'][i])!=11):
        dfg['video_id'][i]=create_videoid()

    #los que son float a string
    if(type(dfg['category_id'][i])==float):
        dfg['category_id'][i]=str(dfg['category_id'][i])
        dfg['category_id'][i]=dfg['category_id'][i][:-2]

    #los que son str a float
    if(type(dfg['views'][i])==str):
        dfg['views'][i]=float(dfg['views'][i])

    dfg['trending_date'][i]='20'+dfg['trending_date'][i]
    
dfg.drop_duplicates(ignore_index = True, inplace=True)
#transformamos estas 3 columnas
dfg['views']=dfg['views'].astype(np.float64)
dfg['trending_date']=pd.to_datetime(dfg['trending_date'],format='%Y.%d.%m')
dfg['publish_time']=dfg['publish_time'].apply(pd.to_datetime)

#arreglamos y ordenamos el dataframe dff
ercd = []
for a in dff['items']:
    ercd.append(a['id'])

dff.assign(id = '')
dff['id'] = ercd
dff.drop(['kind','etag'], axis = 1, inplace = True)
dff.loc[31]=[{'kind': 'youtube#videoCategory',
 'etag': '"m2yskBQFythfE4irbTIeOgYYfBU/SalkJoBWq_smSEqiAx_qyri6Wa8"',
 'id': '29',
 'snippet': {'channelId': 'UCBR8-60-B28hp2BmDPdntcQ',
  'title': 'Nonprofits & Activism',
  'assignable': True}},'29']

###realizamos join entre los 2 dataframes

dfc = dfg.join(dff.set_index('id'), on='category_id')
dfc.head()

#creamos una nueva columna
months = { 1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio',
          7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

dfc['trending_date_month'] = np.nan

for i in range(len(dfg)):
    dfc['trending_date_month'][i] = months[dfg['trending_date'][i].month] + '-' + str(dfg['trending_date'][i].year)

#valores atipicos de likes
plt.style.use('ggplot')
plt.figure(figsize=(25,10))
plt.title('Número de likes')
sns.set_context('notebook',font_scale=1.4)
ax = sns.boxplot(x='likes', data=dfc, orient="h", palette='mako') #rocket
ax.set_xlim([0, 35*10**5]) 
# 10**6

#valores atipicos de dislikes
plt.style.use('ggplot')
plt.figure(figsize=(25,10))
plt.title('Número de dislikes')
sns.set_context('notebook',font_scale=1.4)
ax = sns.boxplot(x='dislikes', data=dfc, orient="h", palette='mako') #rocket
ax.set_xlim([0.0, 20*10**5])
#0.25*10**6

#valores atipicos de views
plt.style.use('ggplot')
plt.figure(figsize=(25,10))
plt.title('Número de visitas')
sns.set_context('notebook',font_scale=1.4)
ax = sns.boxplot(x='views', data=dfc, orient="h", palette='mako') #rocket
ax.set_xlim([0.0, 800*10**5])
#30*10**6

#valores atipicos de comment_count
plt.style.use('ggplot')
plt.figure(figsize=(25,10))
plt.title('Número de comentarios en vídeos')
sns.set_context('notebook',font_scale=1.4)
ax = sns.boxplot(x='comment_count', data=dfc, orient="h", palette='mako') #rocket
ax.set_xlim([0.0, 12*10**5])
#0.2*10**6

#arreglar valores atípicos
dfc2 = dfc.copy()
def fix_outliers(data, cols_lims):

    for col, lim in cols_lims:
        cap = data[col].quantile(.95)

        for e in range(0, len(data)):
            if data[col][e] > lim or data[col][e] == 0:
                data[col][e] = cap
    return data

#especificamos que columnas arreglar sobre sus valores atipicos
dfc2 = fix_outliers(dfc2, [('views', 30 * 10**6), ('likes', 10**6), ('dislikes', 0.25 * 10**6), ('comment_count', 0.2 * 10**6)])

#likes con outliers arreglados
plt.style.use('ggplot')
plt.figure(figsize=(25,10))
plt.title('Número de likes')
sns.set_context('notebook',font_scale=2)
ax = sns.boxplot(x='likes', data=dfc2, orient="h", palette='mako') #rocket
ax.set_xlim([0, 35*10**5])

#dislikes con outliers arreglados
plt.style.use('ggplot')
plt.figure(figsize=(25,10))
plt.title('Número de dislikes')
sns.set_context('notebook',font_scale=1.4)
ax = sns.boxplot(x='dislikes', data=dfc2, orient="h", palette='mako') #rocket
ax.set_xlim([0.0, 20*10**5])

#views con outliers arreglados
plt.style.use('ggplot')
plt.figure(figsize=(25,10))
plt.title('Número de visitas')
sns.set_context('notebook',font_scale=1.4)
ax = sns.boxplot(x='views', data=dfc2, orient="h", palette='mako') #rocket
ax.set_xlim([0.0, 800*10**5])

#comment_count con outliers arreglados
plt.style.use('ggplot')
plt.figure(figsize=(25,10))
plt.title('Número de comentarios en vídeos')
sns.set_context('notebook',font_scale=1.4)
ax = sns.boxplot(x='comment_count', data=dfc2, orient="h", palette='mako') #rocket
ax.set_xlim([0.0, 12*10**5])

#creando columna con nombres de la categoría
dfc2['category_name'] = np.nan
for e in range(len(dfc2)):
    dfc2['category_name'][e] = dfc2['items'][e]['snippet']['title']

#REQUERIMIENTOS

#1. ¿Qué categorías de videos son las de mayor tendencia?

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
dfc2['sum_numbers'] = dfc2['views'] + dfc2['likes'] + dfc2['comment_count']
plt.style.use('fivethirtyeight')
plt.figure(figsize=(20,10))
sns.barplot(x="category_name", y="sum_numbers", data=dfc2, estimator=np.mean, ci=None)
plt.title('Tendencia por categoría')
plt.xticks(rotation=60)

#2 ¿Qué categorías de vídeos son las que más gustan? ¿Y las que menos gustan?

plt.style.use('fivethirtyeight')
plt.figure(figsize=(20,10))
sns.barplot(x="category_name", y="likes", data=dfc2, estimator=np.mean, palette='magma', ci=None)
plt.title('Cantidad de likes por categoría')
plt.xticks(rotation=60)

plt.style.use('fivethirtyeight')
plt.figure(figsize=(20,10))
sns.barplot(x="category_name", y="dislikes", data=dfc2, estimator=np.mean, palette='magma', ci=None)
plt.title('Cantidad de dislikes por categoría')
plt.xticks(rotation=60)

#3. ¿Qué categorías de videos tienen la mejor proporción (ratio) de “Me gusta” / “No me gusta”?

dfc2['like_dislike_ratio'] = dfc2['likes'] / dfc2['dislikes']
plt.style.use('fivethirtyeight')
plt.figure(figsize=(20,10))
g = sns.barplot(x="category_name", y="like_dislike_ratio", data=dfc2, estimator=np.mean, palette='Paired', ci=None)
plt.title('Proporción "Me gusta" / "No me gusta"  por categoría')
plt.xticks(rotation=60)

#4. ¿Qué categorías de videos tienen la mejor proporción (ratio) de “Vistas” / “Comentarios”?

dfc2['views_comments_ratio'] = dfc2['views'] / dfc2['comment_count']
plt.style.use('fivethirtyeight')
plt.figure(figsize=(20,10))
sns.barplot(x="category_name", y="views_comments_ratio", data=dfc2, estimator=np.mean, palette='Paired', ci=None)
plt.title('Proporción "Vistas" / "Comentarios"  por categoría')
plt.xticks(rotation=60)

#5 ¿Cómo ha cambiado el volumen de videos a largo del tiempo?

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(20,10))
ax = sns.countplot(x="trending_date_month", data=dfc2, palette='tab10')
plt.title('Cantidad de vídeos por mes', size=16)
plt.tick_params(axis='both', labelsize=16)
for p in ax.patches:
    ax.annotate(f'\n{p.get_height()}', (p.get_x()+0.2, p.get_height()), ha='left', va='top', color='white', size=18)

#6. ¿Qué Canales de YouTube son tendencia más frecuentemente? ¿Y cuáles con menos frecuencia?

tab1 = dfc2["channel_title"].value_counts()
fig, axes = plt.subplots(1,1, figsize=(20,10))
axes.plot(tab1[0:15], color='green', alpha=0.5)
axes.tick_params(axis='both', labelsize=13, labelrotation=45)
axes.title.set_text('10 Canales de Youtube más frecuentes en tendencia')

fig, axes = plt.subplots(2,1, figsize=(25,20))
axes[0].plot(tab1[1330:1360], color='green')
axes[0].tick_params(axis='both', labelsize=13,labelrotation=45)
axes[0].title.set_text('Canales de Youtube menos frecuentes en tendencia')

axes[1].plot(tab1[1360:], color='green')
axes[1].tick_params(axis='both', labelsize=13,labelrotation=45)
axes[1].title.set_text('Canales de Youtube menos frecuentes en tendencia')
plt.tight_layout()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#7. ¿En qué Estados se presenta el mayor número de “Vistas”, “Me gusta” y “No me gusta”?

sub_df = dfc2[['state', 'views', 'likes', 'dislikes']]
df_by_state = sub_df.groupby(['state']).mean()
df_by_state.reset_index(inplace=True)
df_by_state

import pandas as pd
import plotly.graph_objects as go

data = go.Choropleth(geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                     featureidkey='properties.ST_NM',
                     locationmode='geojson-id',
                     locations=df_by_state['state'],
                     z=df_by_state['views'],
                     colorscale='dense',
                     colorbar=dict(title={'text': "Vistas"},
                                   thickness=15,
                                   len=0.35,
                                   xanchor='left',
                                   x=0.01,
                                   yanchor='bottom',
                                   y=0.05),
                    )
fig = go.Figure(data)
fig.update_geos(fitbounds = "locations", 
                visible = False,
                lonaxis={'range': [68, 98]},
                lataxis={'range': [6, 38]})

fig.add_scattergeo(
  geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
  locations = df_by_state['state'],
  text = df_by_state['state'],
  featureidkey="properties.ST_NM",
  mode = 'text') 

fig.update_traces(textposition="middle center", textfont_color="orange", selector=dict(type='scattergeo'))

fig.update_layout(
    title=dict(
        text="Promedio de número de vistas por Estado",
        xanchor='center',
        x=0.5,
        yref='paper',
        yanchor='bottom',
        y=1,
        pad={'b': 10}
    ),
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
    height=1000,
    width=1000
)
fig.show()

data = go.Choropleth(geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                     featureidkey='properties.ST_NM',
                     locationmode='geojson-id',
                     locations=df_by_state['state'],
                     z=df_by_state['likes'],
                     colorscale='dense',
                     colorbar=dict(title={'text': '"Me gusta"'},
                                   thickness=15,
                                   len=0.35,
                                   xanchor='left',
                                   x=0.01,
                                   yanchor='bottom',
                                   y=0.05),
                    )
fig = go.Figure(data)
fig.update_geos(fitbounds = "locations", 
                visible = False,
                lonaxis={'range': [68, 98]},
                lataxis={'range': [6, 38]})

fig.add_scattergeo(
  geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
  locations = df_by_state['state'],
  text = df_by_state['state'],
  featureidkey="properties.ST_NM",
  mode = 'text') 

fig.update_traces(textposition="middle center", textfont_color="orange", selector=dict(type='scattergeo'))

fig.update_layout(
    title=dict(
        text='Promedio de número de "Me gusta" por Estado',
        xanchor='center',
        x=0.5,
        yref='paper',
        yanchor='bottom',
        y=1,
        pad={'b': 10}
    ),
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
    height=1000,
    width=1000
)
fig.show()

data = go.Choropleth(geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                     featureidkey='properties.ST_NM',
                     locationmode='geojson-id',
                     locations=df_by_state['state'],
                     z=df_by_state['dislikes'],
                     colorscale='dense',
                     colorbar=dict(title={'text': '"No me gusta"'},
                                   thickness=15,
                                   len=0.35,
                                   xanchor='left',
                                   x=0.01,
                                   yanchor='bottom',
                                   y=0.05),
                    )
fig = go.Figure(data)
fig.update_geos(fitbounds = "locations", 
                visible = False,
                lonaxis={'range': [68, 98]},
                lataxis={'range': [6, 38]})

fig.add_scattergeo(
  geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
  locations = df_by_state['state'],
  text = df_by_state['state'],
  featureidkey="properties.ST_NM",
  mode = 'text') 

fig.update_traces(textposition="middle center", textfont_color="orange", selector=dict(type='scattergeo'))

fig.update_layout(
    title=dict(
        text='Promedio de número de "No me gusta" por Estado',
        xanchor='center',
        x=0.5,
        yref='paper',
        yanchor='bottom',
        y=1,
        pad={'b': 10}
    ),
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
    height=1000,
    width=1000
)
fig.show()

# Commented out IPython magic to ensure Python compatibility.
#Modelizar y evaluar datos

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
plt.style.use('dark_background')

sns.pairplot(dfc2[['views', 'dislikes', 'comment_count']])

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

#¿Es factible predecir el número de “Vistas” o “Me gusta” o “No me gusta”?
#cambiando valores de comments_disabled y ratings_disabled
df = dfc2.copy()
for i in range(len(df)):
    if df['comments_disabled'][i] == 'VERDADERO':
        df['comments_disabled'][i] = 1
    else: df['comments_disabled'][i] = 0
        
    if df['ratings_disabled'][i] == 'VERDADERO':
        df['ratings_disabled'][i] = 1
    else: df['ratings_disabled'][i] = 0
        
df_only_state=df_by_state.copy()

ercd = []
for i in range(len(df_only_state['state'])):
    ercd.append(i)

df_only_state.assign(id = '')
df_only_state['id'] = ercd
df_only_state.drop(['views','likes','dislikes'],axis=1, inplace = True)

df = df.join(df_only_state.set_index('state'), on='state')
df.drop('state', axis=1, inplace=True)
df.rename(columns={'id':'state'}, inplace=True)

#VISTAS
c = pd.cut(df[['views']].stack(), [0.0, 0.4*10**6, 1.0*10**7, 3.5*10**7], labels=['bajo', 'medio', 'alto'])
df_views = df.join(c.unstack().add_suffix('_cat'))
df_views = df_views[['category_id', 'views_cat', 'likes', 'dislikes', 'comment_count', 'comments_disabled', 'ratings_disabled', 'state']]

X_train, X_test, y_train, y_test = train_test_split(df_views.drop('views_cat', axis=1), df_views['views_cat'], test_size=0.30, random_state=101)
logmodel = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000) #Parametros utilizados para problemas con multiclases
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)
print(classification_report(y_test, predictions))

#LIKES
c = pd.cut(df[['likes']].stack(), [0.0, 0.1*10**5, 0.1*10**6, 1.5*10**6], labels=['bajo', 'medio', 'alto'])
df_likes = df.join(c.unstack().add_suffix('_cat'))
df_likes = df_likes[['category_id', 'likes_cat', 'views', 'dislikes', 'comment_count', 'comments_disabled', 'ratings_disabled', 'state']]

X_train, X_test, y_train, y_test = train_test_split(df_likes.drop('likes_cat', axis=1), df_likes['likes_cat'], test_size=0.30, random_state=101)
logmodel = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000) #Parametros utilizados para problemas con multiclases
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)
print(classification_report(y_test, predictions))

#DISLIKES
c = pd.cut(df[['dislikes']].stack(), [0.0, 0.8*10**3, 8*10**3, 200*10**3], labels=['bajo', 'medio', 'alto'])
df_dislikes = df.join(c.unstack().add_suffix('_cat'))
df_dislikes = df_dislikes[['category_id', 'dislikes_cat', 'views', 'likes', 'comment_count', 'comments_disabled', 'ratings_disabled', 'state']]

X_train, X_test, y_train, y_test = train_test_split(df_dislikes.drop('dislikes_cat', axis=1), df_dislikes['dislikes_cat'], test_size=0.30, random_state=101)
logmodel = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000) #Parametros utilizados para problemas con multiclases
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)
print(classification_report(y_test, predictions))

#¿Los videos en tendencia son los que mayor cantidad de comentarios positivos reciben?

dfc2_sddcvsd=dfc2.copy()

dfc2_sddcvsd['comentarios_positivos']=dfc2_sddcvsd['likes']/(dfc2_sddcvsd['likes']+dfc2_sddcvsd['dislikes'])*dfc2_sddcvsd['comment_count']
dfc2_sddcvsd['comentarios_negativos']=dfc2_sddcvsd['dislikes']/(dfc2_sddcvsd['likes']+dfc2_sddcvsd['dislikes'])*dfc2_sddcvsd['comment_count']

import numpy as np
import matplotlib.pyplot as plt
x1 = ['comentarios_positivos']
y1 = [int(dfc2_sddcvsd['comentarios_positivos'].mean())]
x2 = ['comentarios_negativos']
y2 = [int(dfc2_sddcvsd['comentarios_negativos'].mean())]

plt.bar(x1, y1, label="Barra azul", color='b')
plt.bar(x2, y2, label="Barra verde", color='g')

plt.plot()
plt.xlabel("tipos de comentarios")
plt.ylabel("cantidad de comentarios")
plt.title("Promedio de los comentarios positivos y negativos")
plt.show()

dfc2.to_csv('dataframe-final.csv',index=False)