"""tuat-feed
農工大の掲示板のデータを取得するライブラリです。使い方としては次のように使うことができます。

>>> import tuat_feed
>>> feed = tuat_feed.fetch()
>>> len(feed)
40
>>> feed[0]
Post(...)

"""

from .fetch import fetch
