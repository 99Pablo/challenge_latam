import pandas as pd
import jsonlines

def q2_time(path_file: str):
    data = []
    # Abre el archivo JSON usando jsonlines
    with jsonlines.open(path_file, 'r') as reader:
        for obj in reader:
            data.append(obj)

    # Crea el DataFrame
    df = pd.DataFrame(data)

    df['user_id'] = df['user'].apply(lambda x: x['username'])

    return df['user_id'].value_counts().head(10)

# if __name__ == '__main__':
#     q2()