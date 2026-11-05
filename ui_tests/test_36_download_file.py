def test_download_file(page, tmp_path):
    page.goto(
        "https://practice.expandtesting.com/download",
        wait_until="domcontentloaded",
    )
    with page.expect_download() as waiting_for_download:
        page.get_by_role(
            "link",
            name="some-file.txt",
            exact = True,
        ).click()
    received_download = waiting_for_download.value
    assert(
        received_download.suggested_filename
         == "some-file.txt"
    )
    saved_file_path = tmp_path / "some-file.txt"
    received_download.save_as(saved_file_path)
    assert saved_file_path.is_file()