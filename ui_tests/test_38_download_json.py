import json

def  test_download_json(page, tmp_path):
    page.goto(
        "https://practice.expandtesting.com/download",
        wait_until="domcontentloaded",
    )
    with page.expect_download() as waiting_for_download:
        page.get_by_role(
            "link",
            name="some-file.json",
            exact = True,
        ).click()
        received_download = waiting_for_download.value
        saved_file_path = tmp_path / "some-file.json"
        received_download.save_as(saved_file_path)
        assert saved_file_path.is_file()
        download_text = saved_file_path.read_text(
            encoding = "utf-8"
        )
        parsed_data = json.loads(download_text)
        assert(
            parsed_data["Message"]
            == "Welcome to the Practice Web App"
        )
