class Recoder:
    def __init__(self):
        raise Exception("Singleton Class, use get_instance please")

    __instance = None

    @classmethod
    def get_instance(cls):
        if Recoder.__instance is None:
            Recoder.__instance = Recoder.__new__(cls)
        return Recoder.__instance

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val


if __name__ == "__main__":
    try:
        r1 = Recoder()
    except Exception:
        print("Failed to call const")
    r1 = Recoder.get_instance()
    r1.set_val(5)
    print(r1.get_val())
    r2 = Recoder.get_instance()
    r2.set_val(5)
    print(r2.get_val())
