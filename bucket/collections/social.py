from .collection import Collection


class SocialCollection(Collection):
    """ Collection class """

    def __init__(self):
        self.name = 'Social Collection'
        self.pages = list()
        self.check = {'domain': True, 'content': True, 'status': False}
        self.keywords = ['facebook', 'twitter',
                         'linkedin', 'reddit', 'instagram']
        self.multiplier = 1
