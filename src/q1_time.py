import pandas as pd

def q1_time(path_file: str):
    df = pd.read_json(path_file, lines=True)
    # Convierte la columna 'date' al formato DateTime
    df['date'] = pd.to_datetime(df['date'])
    # Crea una nueva columna 'day' que contiene solo la fecha (sin la hora)
    df['day'] = df['date'].dt.date

    def extract_user_id(user_info):
        return user_info['username']

    df['user_id'] = df['user'].apply(extract_user_id)

    ans = df['day'].value_counts().head(10).reset_index()

    final = []

    for day in ans['day']:
        temp = df[(df['day'] == day)]
        temp2 = temp['user_id'].value_counts().head(1).reset_index().iloc[0, 0]

        final.append((day, temp2))
        