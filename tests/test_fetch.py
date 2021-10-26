import tuat_feed


def test_fetch():
    posts = tuat_feed.fetch()
    print(posts)

    assert len(posts) > 0
