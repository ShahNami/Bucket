from .collection import Collection


class SocialCollection(Collection):
    """ Collection class """

    def __init__(self):
        self.name: str = 'Social Collection'
        self.pages = list()
        self.check = {'domain': True, 'element': True, 'status': False}
        self.keywords = ['facebook', 'twitter',
                         'linkedin', 'reddit', 'instagram']
