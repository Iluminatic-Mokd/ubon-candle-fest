from ubcf import app, db
from ubcf.models import User

app.config['TESTING'] = True

with app.test_client() as c:
    rv = c.post('/user/register', data={'username':'testuser','email':'test@example.com','password':'pass123','confirm_password':'pass123'}, follow_redirects=True)
    print('Status code:', rv.status_code)
    body = rv.get_data(as_text=True)
    print('Contains "Login Page" in body?:', 'Login Page' in body)

with app.app_context():
    user = db.session.scalar(db.select(User).where(User.username=='testuser'))
    print('User created in DB:', bool(user))
