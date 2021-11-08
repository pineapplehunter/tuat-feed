import tuat_feed
from tuat_feed.post import Post


def test_fetch():
    posts = tuat_feed.fetch()
    print(posts)

    assert len(posts) > 0
    for p in posts:
        assert type(p) is Post


def test_other_fetch():
    posts = tuat_feed.fetch_technology()
    print(posts)

    assert len(posts) > 0
    for p in posts:
        assert type(p) is Post

    posts = tuat_feed.fetch_agriculture()
    print(posts)

    assert len(posts) > 0
    for p in posts:
        assert type(p) is Post
