import emoji
import json
import pandas as pd

def q1_memory(path_file: str):
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
        
    return final

def q2_memory(path_file: str):
    result = []

    emojis = {}

    with open(path_file) as f:
        for line in f:
            tweet = json.loads(line)
            
            content = tweet['content']
            content_emojis = emoji.emoji_list(content)
            
            for emo in content_emojis:
                try:
                    emojis[emo['emoji']] += 1
                except KeyError:
                    emojis[emo['emoji']] = 1

    for emo, count in sorted(emojis.items(), key=lambda emo: emo[1], reverse=True)[:10]:
        result.append((emo, count))

    return result

def q3_memory(path_file: str):

    df = pd.read_json(path_file, lines=True)

    users = {}

    for i in range(len(df)):
        mu = df['mentionedUsers'].iloc[i]
        
        try:
            for user in mu:

                try:
                    users[user['username']] += 1
                except:
                    users[user['username']] = 1
        except:
            continue
            
    final = []

    for user, count in sorted(users.items(), key=lambda user: user[1], reverse=True)[:10]:
        final.append((user, count))
        #print(f"{user}: {count}")

    return final