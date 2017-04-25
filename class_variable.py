class X:
    v = False

    def ab(self):
        c = '1'

        if self.v:
            c = '2'

        print c


x = X()
x.ab()

x = X()
x.v = True
x.ab()

x = X()
x.ab()

