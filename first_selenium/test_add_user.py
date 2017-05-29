from first_selenium.model.user import User

def test_add_user(app):
    new_user = User.rand()
    app.ensure_login_as(User.admin())
    app.add_user(new_user)
    app.logout()
    app.login(new_user)
    assert app.is_logged_in_as(new_user)
