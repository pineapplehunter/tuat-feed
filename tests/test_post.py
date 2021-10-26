from tuat_feed.post import Attachment, Post
from datetime import datetime


def test_parse_post():
    data = {
        "id": 12345,
        "data": {
            "本文": "テスト本文",
            "タイトル": "テストタイトル",
            "発信元": "テスト発信元",
            "最終更新日": "2021/10/25(Mon)",
            "カテゴリー": "テストカテゴリー",
            "担当者": "テスト担当者",
            "公開期間": "2021/10/25(Mon) 〜 2021/10/31(Sun)",
        },
    }

    post = Post.parse_post(data)
    print(post)

    assert post.post_id == 12345
    assert post.title == "テストタイトル"
    assert post.description == "テスト本文"
    assert post.update_date == datetime(2021, 10, 25).date()
    assert post.show_date_start == datetime(2021, 10, 25).date()
    assert post.show_date_end == datetime(2021, 10, 31).date()
    assert post.category == "テストカテゴリー"
    assert post.author == "テスト担当者"
    assert post.origin == "テスト発信元"
    assert post.attachment == []
    assert post.other == {}


def test_post_with_attachment():
    data = {
        "id": 12345,
        "data": {
            "本文": "テスト本文",
            "タイトル": "テストタイトル",
            "発信元": "テスト発信元",
            "最終更新日": "2021/10/25(Mon)",
            "カテゴリー": "テストカテゴリー",
            "担当者": "テスト担当者",
            "公開期間": "2021/10/25(Mon) 〜 2021/10/31(Sun)",
            "添付ファイル": "[テスト添付ファイル](http://example.com/test)",
        },
    }

    post = Post.parse_post(data)
    print(post)

    assert post.attachment == [
        Attachment(name="テスト添付ファイル", url="http://example.com/test")
    ]
    assert post.other == {}


def test_post_with_other():
    data = {
        "id": 12345,
        "data": {
            "本文": "テスト本文",
            "タイトル": "テストタイトル",
            "発信元": "テスト発信元",
            "最終更新日": "2021/10/25(Mon)",
            "カテゴリー": "テストカテゴリー",
            "担当者": "テスト担当者",
            "公開期間": "2021/10/25(Mon) 〜 2021/10/31(Sun)",
            "その他の項目": "テスト項目",
        },
    }

    post = Post.parse_post(data)
    print(post)

    assert post.other == {"その他の項目": "テスト項目"}
