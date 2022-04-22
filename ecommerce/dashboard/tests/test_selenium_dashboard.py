import pytest
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# @pytest.mark.usefixtures("create_admin_user")
# def test_create_new_admin_user(create_admin_user):
#     assert create_admin_user.__str__() == "admin"

# @pytest.mark.selenium causes warnings
@pytest.mark.usefixtures("chrome_browser_instance", "db_fixture_setup")
def test_dashboard_admin_login(
    live_server, db_fixture_setup, chrome_browser_instance
):

    browser = chrome_browser_instance

    # get urls
    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    # find
    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    # input
    user_name.send_keys("admin")
    user_password.send_keys("admin")
    submit.send_keys(Keys.RETURN)

    # test
    assert "Site administration" in browser.page_source
