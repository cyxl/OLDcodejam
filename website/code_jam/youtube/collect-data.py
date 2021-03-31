import json
from urllib import request
from config import YT_DEVELOPER_KEY, FIREBASE_URL, CREDENTIALS
import time
import firebase_admin
from firebase_admin import credentials, db

creds = credentials.Certificate(CREDENTIALS)

firebase_admin.initialize_app(creds, {
    'databaseURL': f'{FIREBASE_URL}'
})


if __name__ == "__main__":

    ref = db.reference('/Youtube')
    get_yt = ref.get()
    t = time.time()
    all_recs = []
    for i in get_yt['youtubers']:
        print(i)
        time.sleep(2)
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={i["id"]}&key={YT_DEVELOPER_KEY}'
        results = request.urlopen(url).read()
        data = json.loads(results)

        for _nextItem in data["items"]:
            d = dict(viewCount=_nextItem["statistics"]["viewCount"],
                     subCount=_nextItem["statistics"]["subscriberCount"],
                     hidSubCount=_nextItem["statistics"]["hiddenSubscriberCount"],
                     vidCount=_nextItem["statistics"]["videoCount"])
            r = dict(yt_name=i["name"],
                     dev_key=i["id"],
                     data=d)
            all_recs.append(r)
    # Record data
    _ref = db.reference(f'/Youtube/results/{int(t)}')
    _ref.set(all_recs)
