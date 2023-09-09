import pandas as pd
import numpy as np

df_apariciones = pd.DataFrame(pd.read_csv('info_apariciones.csv'))
df_liga = pd.DataFrame(pd.read_csv('info_competencia.csv'))
df_jugadores = pd.DataFrame(pd.read_csv('info_jugadores.csv'))
df_club = pd.DataFrame(pd.read_csv('info_club.csv'))
df_partido = pd.DataFrame(pd.read_csv('info_juegos.csv'))

## CREANDO LIGA
columnas_deseadas = ['competition_id','country_name']
filtro = df_liga['competition_id'] == 'BE1' 
liga_new = df_liga.loc[filtro][columnas_deseadas].head(1)


## CREANDO JUGADOR 
columnas_deseadas = ['player_id', 'name_x','last_season_x','current_club_id_x','date_of_birth','position','market_value_in_eur_x']
filtro = df_jugadores["player_id"] == 148365
jugadores_new = df_jugadores.loc[filtro][columnas_deseadas].head(1)


## CREANDO CLUB
columnas_deseadas = ['club_id','name','domestic_competition_id','average_age','net_transfer_record','own_goals','own_position']
filtro = df_club['domestic_competition_id'] == 'BE1'
club_new = df_club.loc[filtro][columnas_deseadas].head(1)


## CREANDO PARTIDO
columnas_deseadas = ['game_id','home_club_id','away_club_id','home_club_goals','away_club_goals','home_club_position','away_club_position','attendance','referee']
filtro = df_partido['away_club_id'] == 3948
partido_new = df_partido.loc[filtro][columnas_deseadas].head(1)

## CREANDO APARICIONES
columnas_deseadas = ['appearance_id','player_id','yellow_cards','red_cards','goals','assists','minutes_played']
filtro = df_apariciones['player_id'] == 148365
apariciones_new = df_apariciones.loc[filtro][columnas_deseadas].head()
print(apariciones_new)

    

