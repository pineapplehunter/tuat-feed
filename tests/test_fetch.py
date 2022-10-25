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


def test_distinct_fetch():
    ta_posts = tuat_feed.fetch(gakubu="technology", category="academic")

    for (g, c) in [
        ("technology", "campus"),
        ("agriculture", "academic"),
        ("agriculture", "campus"),
    ]:
        posts = tuat_feed.fetch(gakubu=g, category=c)
        assert ta_posts != posts
