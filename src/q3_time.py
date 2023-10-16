import emoji
import json
import pandas as pd

def q3_time(path_file: str):

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