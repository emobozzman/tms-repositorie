import pytest

from tests.functional.pages import MainPage
from tests.functional.utils import screenshot_on_failure

url = "http://localhost:8000"


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request):
    page = MainPage(browser, url)

    validate_title(page)
    validate_content(page)


def validate_title(page: MainPage):
    assert "emobozzman is my name" in page.title


def validate_content(page: MainPage):
    assert page.h1.tag_name == "h1"
    assert page.h1.text == "emobozzman is my name"
    assert page.p.tag_name == "p"
    assert page.p.text == "No more."

    html = page.html
    assert "<hr>" in html
