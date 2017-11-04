# set path for image uploads
def image_path_rename(instance, filename):
    ext = filename.split('.')[-1]
    return '{}/{}.{}'.format(instance.platform.slug, instance.slug, ext)

def user_game_image_upload(instance, filename):
    ext = filename.split('.')[-1]
    return '{}/{}/{}.{}'.format(instance.gamelisting.user, instance.gamelisting.game.slug, instance.id, ext)

CONDITIONS = (
    ('new', "Brand New"),
    ('Complete In Box', (
            ('cibvgood', 'Very Good'),
            ('cibgood', 'Good'),
            ('cibacceptable', 'Acceptable'),
        )
    ),
    ('Loose', (
            ('loosevgood', 'Very Good'),
            ('loosegood', 'Good'),
            ('looseacceptable', 'Acceptable'),
        )
    ),
)