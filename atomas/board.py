from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from .atom import Atom, AtomPlus, AtomMinus, Neutrino, AtomDarkPlus
import random
import math
from kivy.clock import Clock

class Board(Widget):

    margin = NumericProperty(10)
    radius = NumericProperty(100)
    amargin= NumericProperty(3)
    ascale = NumericProperty(0.8)
    adiam  = NumericProperty(30)
    cradius= NumericProperty(100)

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.range_start = 1
        self.range_length = 3
        self.atoms = []
        self.center_atom = None
        def reset(dt):
            self.reset()
        Clock.schedule_once(reset, 0.4)

    def _clear(self):
        for a in self.atoms:
            self.remove_widget(a)
        if self.center_atom:
            self.remove_widget(self.center_atom)

    def _random_atom_in_range(self):
        n = random.randint(self.range_start, self.range_start+self.range_length-1)
        return Atom(n, self)

    def _init(self):
        incr  = (2.0*math.pi) / 6.0
        atoms = []
        for i in range(6):
            a = self._random_atom_in_range()
            a.angle = i * incr
            a.waiting = False
            self.add_widget(a)
            atoms.append(a)
        atoms.reverse()
        self.atoms = atoms

    def reset(self):
        self._clear()
        self._init()
        self._spawn()

    def _spawn(self):
        pct = 0.0
        gens = []
        pct += 1.0/5.0
        gens.append((pct, self.plus_generator))
        pct += 1.0/20.0
        gens.append((pct, self.minus_generator))
        below = {a.model.n for a in self.atoms if isinstance(a, Atom) and a.n < self.range_start}
        n = len(self.atoms)
        for a in below:
            pct += 1.0/n
            gens.append((pct, self.atom_generator(a.n)))
        incr = (1.0 - pct) / self.range_length
        for n in range(self.range_start, self.range_start+self.range_length):
            pct += incr
            gens.append((pct, self.atom_generator(n)))
        which = random.uniform(0.0, pct)
        for p,g in gens:
            if which <= p:
                a = g()
                self.add_widget(a)
                return
        raise Exception("spawn failed")

    def atom_generator(self, n):
        def g():
            return Atom(n, self)
        return g

    def plus_generator(self):
        def g():
            return AtomPlus(self)
        return g

    def minus_generator(self):
        def g():
            return AtomMinus(self)
