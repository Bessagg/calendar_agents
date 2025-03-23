import logging

from app import create_app


app = create_app()

if __name__ == "__main__":
    logging.info("Flask app started")

    app.run(host="0.0.0.0", port=8000)
    # Then run your ngrok command, example:
    # ngrok http --url=lately-known-mustang.ngrok-free.app 8000 