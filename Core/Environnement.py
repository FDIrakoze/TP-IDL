class Environnement():
    instance = None
    class __Environnement:
        def __init__(self, arg, torique):
            self.espace = arg
            self.torique = torique
    def __init__(self, arg, torique):
        if not Environnement.instance:
            Environnement.instance = Environnement.__Environnement(arg, torique)
        else:
            Environnement.instance.espace = arg
            Environnement.instance.torique = torique

