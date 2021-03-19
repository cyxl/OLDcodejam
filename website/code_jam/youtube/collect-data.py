import json
from urllib import request
from config import YT_DEVELOPER_KEY, FIREBASE_URL
import time
import firebase_admin
from firebase_admin import credentials, db

creds = credentials.Certificate('../../../serviceAccountKey.json')

firebase_admin.initialize_app(creds, {
    'databaseURL': f'{FIREBASE_URL}'
})
ref = db.reference('/')
ref.set({

    'Youtube':
        {
            "youtubers": [
                {
                    "name": "Tech With Tim",
                    "id": "UC4JX40jDee_tINbkjycV4Sg"
                },
                {
                    "name": "Corey Schafer",
                    "id": "UCCezIgC97PvUuR4_gbFUs5g"
                },
                {
                    "name": "Kimberly Brehm",
                    "id": "UCcbu9qaBn3MNFYr96mbg72w"
                },
                {
                    "name": "Program With Erik",
                    "id": "UCshZ3rdoCLjDYuTR_RBubzw"
                },
                {
                    "name": "Florin Pop",
                    "id": "UCeU-1X402kT-JlLdAitxSMA"
                },
                {
                    "name": "Nick White",
                    "id": "UC1fLEeYICmo3O9cUsqIi7HA"
                },
                {
                    "name": "Ben Awad",
                    "id": "UC-8QAzbLcRglXeN_MY9blyw"
                },
                {
                    "name": "Clément Mihailescu",
                    "id": "UCaO6VoaYJv4kS-TQO_M-N_g"
                },
                {
                    "name": "Engineer Man",
                    "id": "UCrUL8K81R4VBzm-KOYwrcxQ"
                },
                {
                    "name": "mayuko",
                    "id": "UCEDkO7wshcDZ7UZo17rPkzQ"
                },
                {
                    "name": "Web Dev Simplified",
                    "id": "UCFbNIlppjAuEX4znoulh0Cw"
                },
                {
                    "name": "Kalle Hallden",
                    "id": "UCWr0mx597DnSGLFk1WfvSkQ"
                },
                {
                    "name": "sentdex",
                    "id": "UCfzlCWGWYyIQ0aLC5w48gBQ"
                },
                {
                    "name": "The Coding Train",
                    "id": "UCvjgXvBlbQiydffZU7m1_aw"
                },
                {
                    "name": "Traversy Media",
                    "id": "UC29ju8bIPH5as8OGnQzwJyA"
                },
                {
                    "name": "thenewboston",
                    "id": "UCJbPGzawDH1njbqV-D5HqKw"
                },
                {
                    "name": "freeCodeCamp.org",
                    "id": "UC8butISFwT-Wl7EV0hUK0BQ"
                }
            ]
        }
})


if __name__ == "__main__":
    with open('youtubers.json') as f:
        db = json.loads(f.read())
        # Get new data
        all_recs = []
        for i in db['youtubers']:
            print(i)

            time.sleep(2)
            url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={i["id"]}&key={YT_DEVELOPER_KEY}'
            print(url)
            results = request.urlopen(url).read()
            data = json.loads(results)

            for _nextItem in data["items"]:
                d = dict(viewCount=_nextItem["statistics"]["viewCount"],
                         subCount=_nextItem["statistics"]["subscriberCount"],
                         hidSubCount=_nextItem["statistics"]["hiddenSubscriberCount"],
                         vidCount=_nextItem["statistics"]["videoCount"])
                r = dict(yt_name=i["name"],
                         dev_key=i["id"],
                         time=time.time(),
                         data=d)
                all_recs.append(r)
        # Record data
        with open("records.json") as recf:
            recs = json.loads(recf.read())
            recs.extend(all_recs)

            with open("records.json", 'w') as recf:
                recf.write(json.dumps(recs))
