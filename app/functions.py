

def handle_uploaded_file(file):
    with open("app/static/App/img/"+file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
