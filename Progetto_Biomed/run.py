import os

from app import create_app, db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Default sicuro: solo localhost, debugger spento. Per la lezione in aula:
    #   FLASK_DEBUG=1 HOST=0.0.0.0 python3 run.py
    app.run(
        debug=os.environ.get('FLASK_DEBUG') == '1',
        host=os.environ.get('HOST', '127.0.0.1'),
        port=int(os.environ.get('PORT', '5001')),
    )
