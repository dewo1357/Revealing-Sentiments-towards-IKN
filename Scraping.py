from itertools import islice
from youtube_comment_downloader import *
import pandas as pd
downloader = YoutubeCommentDownloader()

link_list = ['https://www.youtube.com/watch?v=9s67hA2naWg',
             'https://www.youtube.com/watch?v=DYnxa7GQUcY&t=5s',
             'https://www.youtube.com/watch?v=mIOfV4U2R4o',
             'https://www.youtube.com/watch?v=dAopfpsH88g',
             'https://www.youtube.com/watch?v=37xbS2Z0eNA',
             'https://www.youtube.com/watch?v=DYnxa7GQUcY&t=24s',
             'https://www.youtube.com/watch?v=dRLKnike1FQ',
             'https://www.youtube.com/watch?v=8re8iKyWk7s',
             'https://www.youtube.com/watch?v=qQEmAgYFB38',
             'https://www.youtube.com/watch?v=Tw5tWik_oSg',
             'https://www.youtube.com/watch?v=d3sm2CtmRFo']
dataframe = {}
done = 0
for link in link_list:
    comments = downloader.get_comments_from_url(link, sort_by=SORT_BY_POPULAR)
    for comment in islice(comments, 100):
        if done == 0:
            for i in comment:
                dataframe[i] = []
            done = 1
        for data in comment:
            dataframe[data].append(comment[data])

df = pd.DataFrame(dataframe)
df.to_csv('data.csv')



