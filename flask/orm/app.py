from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask
app = Flask(__name__)

#sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#sqlalchemy 초기화
db = SQLAlchemy(app)

#Migrate 초기화
migrate = Migrate(app, db)

# tables 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
        #정보를 많이 보여주도록 수정한 코드.
    
# 명령어
# flask db init
# flask db migrate
# flask db upgrade

# 정리
# [Create]
# INSERT INTO users (username, email) VALUES ('intaekShin', 'sit921212@gmail.com')
# user = User(username='intaekShin', email='sit921212@gmail.com') 유저 객체 인스턴스 생성.
# db.session.add(user) 추가해줍니다.
# db.session.commit() 데이터베이스에 반영.

# [Read]
# SELECT * FROM users;
# users = User.query.all() # 복수가 출력된다. 보통 변수에 저장해서 씀!;)

# SELECT * FROM users WHERE username='intaekShin';
# users = User.query.filter_by(username='intaekShin').all()

# SELECT * FROM users WHERE username='intaekShin' LIMIT 1;
# user = User.query.filter_by(username='intaekShin').first()

# SELECT * FROM users WHERE id=2 LIMIT 1;
# user = User.query.get(2)
# primary key만 get으로 가져올 수 있음.

# SELECT * FROM users WHERE email LIKE '%gmail%';
# users = User.query.filter(User.email.like("%gmail%")).all()

# ORDER
# users = User.query.order_by(User.username).all()

# LIMIT
# users = User.query.limit(1).all()

# OFFSET
# users = User.query.offset(2).all()

# ORDER + LIMIT + OFFSET 중복해서 한 줄로 코드를 작성할 수 있음.
# users = User.query.order_by(User.username).limit(1).offset(2).all()

# [DELETE]
# DELETE FROM users WHERE id=1;
# user = User.query.get(1)
# db.session.delete(user)
# db.session.commit()

# [UPDATE]
# UPDATE users SET username='intaek' WHERE id=2;
# user = User.query.get(2)
# user.username = 'intaek'
# db.session.commit()

