	# Код для авторизации в приложении php4dvd
from selenium import webdriver
from first_selenium.model.user import User
from selenium.common.exceptions import *
from first_selenium.selenium_fixture import app

def test_login_with_valid_credentials(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert not app.is_logged_in()

def test_login_with_invalid_credentials(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.logout()
