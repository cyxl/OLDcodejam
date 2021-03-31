import datetime

import firebase_admin
from bokeh.embed import components
from bokeh.palettes import Spectral11
from bokeh.plotting import figure
from bokeh.resources import INLINE
from firebase_admin import credentials, db
from flask import render_template, Blueprint, request

from config import FIREBASE_URL, CREDENTIALS

view = Blueprint("views", __name__)

creds = credentials.Certificate(CREDENTIALS)
firebase_admin.initialize_app(creds, {
    'databaseURL': f'{FIREBASE_URL}'
})

ref = db.reference('Youtube/results')


@view.route("/")
@view.route("/home")
def home():
    return render_template("index.html")


def test_plot(yt_key):
    get_data = ref.get()
    yt_res = dict()
    for _key, _val in get_data.items():
        print(f'Getting data for time {datetime.datetime.fromtimestamp(int(_key))}')

        for _next_yt in _val:
            if _next_yt['dev_key'] == yt_key:
                yt_res['name'] = _next_yt['yt_name']
                yt_res['key'] = _next_yt['dev_key']
                print(f'Getting data for {_next_yt["yt_name"]}')
                yt_res.setdefault('hidsubcnt', []).append(_next_yt['data']['hidSubCount'])
                yt_res.setdefault('subcnt', []).append(_next_yt['data']['subCount'])
                yt_res.setdefault('vidcnt', []).append(_next_yt['data']['vidCount'])
                yt_res.setdefault('viewcnt', []).append(_next_yt['data']['viewCount'])
                yt_res.setdefault('time', []).append(datetime.datetime.fromtimestamp(int(_key)))

    print(yt_res['time'])
    print(yt_res['subcnt'])
    fig = figure(title=f'{yt_res["name"]}',
                 plot_width=800,
                 plot_height=600,
                 x_axis_type='datetime',
                 x_axis_label='time',
                 y_axis_label='count',
                 )
    fig.left[0].formatter.use_scientific = False
    pallet = Spectral11

    for _i, _n in enumerate([
        #  'hidsubcnt',
        'subcnt',
        # 'vidcnt',
        # 'viewcnt',
    ]):
        fig.line(yt_res['time'],
                 yt_res[_n],
                 line_color=pallet[_i],
                 legend_label=_n)
    return components(fig)


@view.route("/cj")
@view.route("/stracker")
def stracker():
    return render_template("cj.html")


@view.route("/cj/youtube")
@view.route("stracker/youtube")
def youtube():
    if request.method == 'POST':
        yt_id = request.form['yt_id']
    else:
        yt_id = 'UC4JX40jDee_tINbkjycV4Sg'

    yt_key = request.args.get('yt_id', f'{yt_id}')
    script, div = test_plot(yt_key)
    return render_template("youtube.html",
                           js_resources=INLINE.render_js(),
                           css_resources=INLINE.render(),
                           bokeh_script=script,
                           bokeh_div=div)
