# set path for image uploads
def image_path_rename(instance, filename):
    ext = filename.split('.')[-1]
    return '{}/{}.{}'.format(instance.basegame.slug, instance.slug, ext)