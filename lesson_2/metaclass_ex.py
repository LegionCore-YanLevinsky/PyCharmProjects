def init(self):
    self.connection

class MyMetaConnection(type):

    def __new__(cls, *args, **kwargs):
        my_new_class = type(cls, *args, **kwargs)

        my_new_class.__init__()