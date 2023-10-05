import pandas as pd
import jsonlines

def q2():
    data = []
    # Abre el archivo JSON usando jsonlines
    with jsonlines.open('farmers-protest-tweets-2021-2-4.json', 'r') as reader:
        for obj in reader:
            data.append(obj)

    # Crea el DataFrame
    df = pd.DataFrame(data)

    df['user_id'] = df['user'].apply(lambda x: x['username'])

    return df['user_id'].value_counts().head(10)

# if __name__ == '__main__':
#     q2()