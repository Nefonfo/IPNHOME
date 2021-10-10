import json
import os

from django.core.files.images import ImageFile

from wagtail.images.models import Image

from academic_unit.models import AcademicUnit


def run():
    filename = os.path.join(os.path.dirname(__file__), 'units.json')
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)

        for i in data['data']:
            # SAVE UNIT IMAGE
            filename = i['logo']
            path = os.path.join(os.path.dirname(__file__), f'images/{filename}')
            image_file = ImageFile(open(path, 'rb'), name=i['logo'])
            image = Image(title=i['logo'], file=image_file)
            image.save()

            if('many' in i.keys()):
                for unit in i['many']:
                    academic_unit = AcademicUnit(
                        name = i['name'] + ' - ' + unit ,
                        little_name = i['little_name'] + ' - ' + unit,
                        level = i['level'],
                        logo = image
                    )
                    academic_unit.save()
            else:
                academic_unit = AcademicUnit(
                    name = i['name'],
                    little_name = i['little_name'],
                    level = i['level'],
                    logo = image
                )
                academic_unit.save()
    print('--- SEEDED SUCCESSFULLY ---')


            


