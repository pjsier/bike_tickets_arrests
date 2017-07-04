import pandas as pd

if __name__ == '__main__':
    ticket_df = pd.read_csv('output/bike_tickets.csv')
    arrest_df = pd.read_csv('output/bike_arrests.csv')

    arrest_df['STREET_NAME'] = arrest_df['Street Direction'] + ' ' + arrest_df['Street name']
    arrest_df['ZIP_CODE'] = ''
    arrest_df['PLACE_NAME'] = 'Chicago'
    arrest_df['STATE_NAME'] = 'IL'
    arrest_df['ADDRESS_NUMBER'] = arrest_df['Street No'].str.replace('XX', '50')
    arrest_df.rename(columns={'Arrest ID': 'ID'}, inplace=True)
    arrest_df = arrest_df[[
        'ID', 'ADDRESS_NUMBER', 'STREET_NAME', 'PLACE_NAME', 'ZIP_CODE', 'STATE_NAME'
    ]].copy()
    arrest_df.to_csv('output/bike_arrests_to_geocode.csv', index=False)

    ticket_df['STREET_NAME'] = ticket_df['Street Direction'] + ' ' + bike_df['Street Name']
    ticket_df['ZIP_CODE'] = ''
    ticket_df['PLACE_NAME'] = 'Chicago'
    ticket_df['STATE_NAME'] = 'IL'
    ticket_df['ADDRESS_NUMBER'] = ticket_df['Street No'].str.replace('XX', '50')
    ticket_df.rename(columns={'ANOV Number': 'ID'}, inplace=True)
    ticket_df = ticket_df[[
        'ID', 'ADDRESS_NUMBER', 'STREET_NAME', 'PLACE_NAME', 'ZIP_CODE', 'STATE_NAME'
    ]].copy()
    ticket_df.to_csv('output/bike_tickets_to_geocode.csv', index=False)
