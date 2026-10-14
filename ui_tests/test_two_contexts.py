def test_two_contexts(new_context):
    zhenya_context = new_context()
    masha_context = new_context()

    zhenya_context.add_cookies([
        {
            "name": "user",
            "value": "Zhenya",
            "url": "https://example.com"
        }
    ])
    zhenya_cookies = zhenya_context.cookies()
    masha_cookies = masha_context.cookies()
    assert len(zhenya_cookies) == 1
    assert masha_cookies == []

