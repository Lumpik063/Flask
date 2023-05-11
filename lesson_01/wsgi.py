# from blog import app
from blog.app import create_app, db

# if __name__ == "__main__":
#     app.run(
#         host="0.0.0.0",
#         debug=True,
#     )

app = create_app()

