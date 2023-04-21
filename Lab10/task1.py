class Ensemble:
    def __init__(self, instruments):
        self.instruments = instruments
    
    def genre(self):
        pass

class ClassicalEnsemble(Ensemble):
    def genre(self):
        return "Classical"
    
class JazzEnsemble(Ensemble):
    def genre(self):
        return "Jazz"

def print_ensemble(ensemble):
    print(ensemble.genre())

orchestra = ClassicalEnsemble(["violin", "viola"])
jazz_band = JazzEnsemble(["saxophone", "piano"])

print_ensemble(orchestra)
print_ensemble(jazz_band)