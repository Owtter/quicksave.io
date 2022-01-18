from website import create_app

app = create_app()

# prevents run.py from accidentally being run from another file
if __name__ == "__main__":
    # run flask webserver
    # TODO: debug=True -> rerun webserver after each change. Turn off in production.
    app.run(debug=True)
