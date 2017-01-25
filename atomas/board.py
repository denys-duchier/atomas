from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from .atom import Atom, AtomPlus, AtomMinus, Neutrino, AtomDarkPlus
import random
import math

class Board(Widget):

    margin = NumericProperty(10)
    radius = NumericProperty(100)
    amargin= NumericProperty(3)
    ascale = NumericProperty(0.8)
    adiam  = NumericProperty(30)
    cradius= NumericProperty(100)

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self._test_angle = 0
        self._test_angle_incr = (2.0*math.pi) / 18.0

    def on_touch_down(self, touch):
        self._another_test_atom()

    def _another_test_atom(self):
        self._add_test_atom(random.choice(
            (self._get_test_atom,
             self._get_test_atom,
             self._get_test_atom,
             self._get_test_atom,
             self._get_test_atom,
             self._get_test_atomplus,
             self._get_test_atomminus,
             self._get_test_neutrino,
             self._get_test_atomdarkplus))())

    def _add_test_atom(self, a):
        a.angle = self._test_angle
        self._test_angle += self._test_angle_incr
        a.waiting = False
        self.add_widget(a)

    def _get_test_atom(self):
        n = random.randint(1, 124)
        return Atom(n, self)

    def _get_test_atomplus(self):
        return AtomPlus(self)

    def _get_test_atomminus(self):
        return AtomMinus(self)

    def _get_test_neutrino(self):
        return Neutrino(self)

    def _get_test_atomdarkplus(self):
        return AtomDarkPlus(self)
