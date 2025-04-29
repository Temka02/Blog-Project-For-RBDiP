from app import app, db, User, Post, Comment

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', password='1234')
        db.session.add(admin)
        db.session.commit()

    posts = []
    for i in range(5):
        p = Post(title=f"Post {i + 1}", content=f"Content {i + 1}", author=admin)
        db.session.add(p)
        posts.append(p)
    db.session.commit()

    for idx, p in enumerate(posts):
        comment = Comment(
            content=f"Comment {idx + 1} on post {p.title}",
            post_id=p.id
        )
        db.session.add(comment)
    db.session.commit()

    print("Тестовые данные успешно добавлены.")