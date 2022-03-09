from json import dumps


photo_base_url = '/static/gallery/photos/photo ({0}).jpg'
video_base_url = '/static/gallery/videos/video ({0}).mp4'


gallery_list = list()


for i in range(1, 10):
    gallery_list.append(video_base_url.format(i))

for i in range(1, 38):
    gallery_list.append(photo_base_url.format(i))


def get_photos_from_db():
    return dumps(gallery_list)
