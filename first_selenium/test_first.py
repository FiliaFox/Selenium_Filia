# Код для авторизации в приложении php4dvd

from first_selenium.model.user import User


def test_login_with_valid_credentials(app):
    app.ensure_logout()
    app.login(User.admin())
    assert app.is_logged_in()


def test_login_with_invalid_credentials(app):
    app.ensure_logout()
    app.login(User.rand())
    assert app.is_not_logged_in()
