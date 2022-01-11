from tuat_feed.post import Attachment, Post
from datetime import datetime


def test_parse_post():
    data = {
        "投稿ID": 12345,
        "本文": "テスト本文",
        "タイトル": "テストタイトル",
        "発信元": "テスト発信元",
        "最終更新日": "2021/10/25(Mon)",
        "カテゴリー": "テストカテゴリー",
        "担当者": "テスト担当者",
        "公開期間": ["2021/10/25(Mon)", "2021/10/31(Sun)"],
        "対象": "ABC",
    }

    post = Post.parse_post(data)
    print(post)

    assert post.post_id == 12345
    assert post.title == "テストタイトル"
    assert post.description == "テスト本文"
    assert post.update_date == datetime(2021, 10, 25).date()
    assert post.show_date == (
        datetime(2021, 10, 25).date(),
        datetime(2021, 10, 31).date(),
    )
    assert post.category == "テストカテゴリー"
    assert post.author == "テスト担当者"
    assert post.origin == "テスト発信元"
    assert post.target == "ABC"
    assert post.attachment == []
    assert post.other == {}
    assert repr(post) == "Post(テストタイトル)"


def test_post_with_attachment():
    data = {
        "投稿ID": 12345,
        "本文": "テスト本文",
        "タイトル": "テストタイトル",
        "発信元": "テスト発信元",
        "最終更新日": "2021/10/25(Mon)",
        "カテゴリー": "テストカテゴリー",
        "担当者": "テスト担当者",
        "対象": "ABC",
        "公開期間": ["2021/10/25(Mon)", "2021/10/31(Sun)"],
        "添付ファイル": {"テスト添付ファイル": "http://example.com/test"},
    }

    post = Post.parse_post(data)
    print(post)

    assert post.attachment == [
        Attachment(name="テスト添付ファイル", url="http://example.com/test")
    ]
    assert post.other == {}
    assert repr(post) == "Post(テストタイトル, 添付ファイルあり)"
    assert repr(post.attachment[0]) == "Attachment(テスト添付ファイル)"


def test_post_with_other():
    data = {
        "投稿ID": 12345,
        "本文": "テスト本文",
        "タイトル": "テストタイトル",
        "発信元": "テスト発信元",
        "最終更新日": "2021/10/25(Mon)",
        "カテゴリー": "テストカテゴリー",
        "担当者": "テスト担当者",
        "対象": "ABC",
        "公開期間": ["2021/10/25(Mon)", "2021/10/31(Sun)"],
        "その他の項目": "テスト項目",
    }

    post = Post.parse_post(data)
    print(post)

    assert post.other == {"その他の項目": "テスト項目"}


def test_post_with_long_title():
    data = {
        "投稿ID": 12345,
        "本文": "テスト本文",
        "タイトル": "とてもとてもとてもとてもとても長いタイトル",
        "発信元": "テスト発信元",
        "最終更新日": "2021/10/25(Mon)",
        "カテゴリー": "テストカテゴリー",
        "担当者": "テスト担当者",
        "対象": "ABC",
        "公開期間": ["2021/10/25(Mon)", "2021/10/31(Sun)"],
    }

    post = Post.parse_post(data)
    print(post)

    assert repr(post) == "Post(とてもとてもとてもとてもとても長い...)"
