from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from .atom import Atom, AtomPlus, AtomMinus, Neutrino, AtomDarkPlus
import random
import math
from kivy.clock import Clock
from kivy.animation import Animation

TWO_PI = 2.0*math.pi

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
        self.move_number = 0
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
        self.atoms = atoms

    def reset(self):
        self._clear()
        self._init()
        self._spawn()
        self.move_number = 0

    def _move_done(self):
        self.move_number += 1
        if (self.move_number % 40) == 0:
            self.range_start += 1

    def _spawn(self):
        pct = 0.0
        gens = []
        pct += 1.0/5.0
        gens.append((pct, self.plus_generator()))
        pct += 1.0/20.0
        gens.append((pct, self.minus_generator()))
        below = {a.n for a in self.atoms if isinstance(a, Atom) and a.n < self.range_start}
        n = len(self.atoms)
        for m in below:
            pct += 1.0/n
            gens.append((pct, self.atom_generator(m)))
        incr = (1.0 - pct) / self.range_length
        for n in range(self.range_start, self.range_start+self.range_length):
            pct += incr
            gens.append((pct, self.atom_generator(n)))
        which = random.uniform(0.0, pct)
        for p,g in gens:
            if which <= p:
                a = g()
                self.center_atom = a
                self.add_widget(a)
                a.opacity = 0
                Animation(opacity=1, duration=0.5, transition="in_expo").start(a)
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
        return g

    def _normalize_angle(self, angle):
        while angle < 0:
            angle += TWO_PI
        while angle > TWO_PI:
            angle -= TWO_PI
        return angle

    def _angle_animation(self, a, angle):
        beg = a.angle
        end = angle
        if beg <= end:
            if end-beg >= math.pi:
                a.angle += TWO_PI
        else:
            if beg-end >= math.pi:
                a.angle -= TWO_PI
        return Animation(angle=angle, duration=0.5)

    def _insert(self, angle):
        anims = []
        a = self.center_atom
        angle = self._normalize_angle(angle)
        a.angle = a.next_angle = angle
        a.rpercent = 0.0
        anims.append((Animation(rpercent=1.0, duration=0.5), a))
        i = 0
        for b in self.atoms:
            if angle <= b.angle:
                break
            i += 1
        self.atoms.insert(i, a)
        n = len(self.atoms)
        incr = TWO_PI / n
        angle = a.angle
        for j in range(i+1, n):
            angle += incr
            self.atoms[j].next_angle = angle
        angle = a.angle
        for j in reversed(range(0, i)):
            angle -= incr
            self.atoms[j].next_angle = angle
        neg = [b for b in self.atoms if b.next_angle < 0]
        pos = [b for b in self.atoms if b.next_angle >= 0]
        for b in neg:
            b.next_angle += TWO_PI
        pos.extend(neg)
        self.atoms = pos
        for b in self.atoms:
            if b is not a:
                anims.append((self._angle_animation(b, b.next_angle), b))
        a.waiting = False
        for an,at in anims:
            an.start(at)
        self._spawn()

    def on_touch_down(self, touch):
        dx = touch.x - self.center_x
        dy = touch.y - self.center_y
        angle = self._normalize_angle(math.atan2(dy, dx))
        self._insert(angle)
        self._move_done()
