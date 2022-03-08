from json import dumps


photo_base_url = '/static/gallery/photos/photo ({0}).jpg'


photo_list = list()
for i in range(1, 38):
    photo_list.append(photo_base_url.format(i))


def get_photos_from_db():
    return dumps(photo_list)
