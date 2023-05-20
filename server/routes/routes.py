import os
from flask import request
from image.image import transformImg

class Routes:
    def __init__(self, model) -> None:
        self.model = model

    def analyseImage(self):
        file = request.files['image']
        if file.filename != '':
            file.save('./assets/' + file.filename)
            print('File uploaded successfully')
        else:
            print('No file selected')
        digit = transformImg('./assets/' + file.filename)
        result = self.model.analyseImage(digit)
        print(result)
        os.remove('./assets/' + file.filename)
        return {'Image analyse': str(result)}, 200