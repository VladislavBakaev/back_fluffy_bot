from fluffy_http_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=8000)