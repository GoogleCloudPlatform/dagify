from project import app

if __name__ == '__main__':
    with app.app_context():  # Ensures db and session availability in routes
        db.create_all()
        app.run(debug=True, host='0.0.0.0', port=app.config['PORT'])