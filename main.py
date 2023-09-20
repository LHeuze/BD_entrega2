import pandas as pd
import numpy as np

df_apariciones = pd.DataFrame(pd.read_csv('info_apariciones.csv'))
df_liga = pd.DataFrame(pd.read_csv('info_competencia.csv'))
df_jugadores = pd.DataFrame(pd.read_csv('info_jugadores.csv'))
df_club = pd.DataFrame(pd.read_csv('info_club.csv'))
df_partido = pd.DataFrame(pd.read_csv('info_juegos.csv'))

## CREANDO LIGA
columnas_deseadas = ['competition_id','country_name']
#filtro = df_liga['competition_id'] == 'BE1' 
liga_new = df_liga[columnas_deseadas]
nuevo_liga_csv = 'liga.csv'
liga_new.to_csv(nuevo_liga_csv, index=False)


## CREANDO JUGADOR 
columnas_deseadas = ['player_id', 'name_x','last_season_x','current_club_id_x','date_of_birth','position','market_value_in_eur_x']
#filtro = df_jugadores["player_id"] == 148365
jugadores_new = df_jugadores[columnas_deseadas]
nuevo_jugador_csv = 'jugador.csv'
jugadores_new.to_csv(nuevo_jugador_csv, index=False)


## CREANDO CLUB
columnas_deseadas = ['club_id','name','domestic_competition_id','average_age','net_transfer_record','own_goals','own_position']
#filtro = df_club['domestic_competition_id'] == 'BE1'
club_new = df_club[columnas_deseadas]
nuevo_club_csv = 'club.csv'
club_new.to_csv(nuevo_club_csv, index=False)


## CREANDO PARTIDO
columnas_deseadas = ['game_id','home_club_id','away_club_id','home_club_goals','away_club_goals','home_club_position','away_club_position','attendance','referee']
#filtro = df_partido['away_club_id'] == 3948
partido_new = df_partido[columnas_deseadas]
nuevo_partido_csv = 'partido.csv'
partido_new.to_csv(nuevo_partido_csv, index=False)

## CREANDO APARICIONES
columnas_deseadas = ['appearance_id','player_id','yellow_cards','red_cards','goals','assists','minutes_played']
#filtro = df_apariciones['player_id'] == 148365
apariciones_new = df_apariciones[columnas_deseadas]
nuevo_apariciones_csv = 'apariciones.csv'
apariciones_new.to_csv(nuevo_apariciones_csv, index=False)


    


