import emoji
import json

def q1_time(path_file: str):
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

def q2_time(path_file: str):
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

def q3_time(path_file: str):
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