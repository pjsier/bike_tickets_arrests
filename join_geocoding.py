import pandas as pd

if __name__ == '__main__':
    arrest_df = pd.read_csv('output/bike_arrests.csv')
    ticket_df = pd.read_csv('output/bike_tickets.csv')

    arrest_geo = pd.read_csv('geocoding/bike_arrests_output.csv')
    ticket_geo = pd.read_csv('geocoding/bike_tickets_output.csv')

    arrest_geo = arrest_geo[['id', 'lat', 'lon']].copy()
    arrest_geo.rename(columns={'id': 'Arrest ID'}, inplace=True)
    ticket_geo = ticket_geo[['id', 'lat', 'lon']].copy()
    ticket_geo.rename(columns={'id': 'ANOV Number'}, inplace=True)

    arrest_merge = arrest_df.merge(arrest_geo, on='Arrest ID', how='left')
    ticket_merge = ticket_df.merge(ticket_geo, on='ANOV Number', how='left')

    arrest_merge.to_csv('output/bike_arrests.csv', index=False)
    ticket_merge.to_csv('output/bike_tickets.csv', index=False)
