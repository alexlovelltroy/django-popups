class Popups(object):
    """
    Main popup object that returns True for everything not marked false in
    the session.  That includes any nonsense session variable.

    Check your spelling
    """
    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        return self.request.session.get("popups_" + key, True)

def popups(request):
    return {"show_popup": Popups(request)}

