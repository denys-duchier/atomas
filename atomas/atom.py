from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty
from collections import namedtuple
from kivy.utils import get_color_from_hex

AtomModel = namedtuple('AtomModel', ['n', 'symbol', 'name', 'color'])

ATOMS = (
    AtomModel(1, 'H', 'Hydrogen', '#63B9D5'),
    AtomModel(2, 'He', 'Helium', '#D1C991'),
    AtomModel(3, 'Li', 'Lithium', '#4C6168'),
    AtomModel(4, 'Be', 'Beryllium', '#C8C8C8'),
    AtomModel(5, 'B', 'Boron', '#7D5353'),
    AtomModel(6, 'C', 'Carbon', '#3B3B3B'),
    AtomModel(7, 'N', 'Nitrogen', '#2CC6B2'),
    AtomModel(8, 'O', 'Oxygen', '#6FEC98'),
    AtomModel(9, 'F', 'Fluorine', '#ECC46F'),
    AtomModel(10, 'Ne', 'Neon', '#BE0086'),
    AtomModel(11, 'Na', 'Sodium', '#E69D7A'),
    AtomModel(12, 'Mg', 'Magnesium', '#9E80EA'),
    AtomModel(13, 'Al', 'Aluminum', '#797979'),
    AtomModel(14, 'Si', 'Silicon', '#4A4070'),
    AtomModel(15, 'P', 'Phosphorus', '#D7463F'),
    AtomModel(16, 'S', 'Sulfur', '#375E7C'),
    AtomModel(17, 'Cl', 'Chlorine', '#6D1D7B'),
    AtomModel(18, 'Ar', 'Argon', '#9A3DA5'),
    AtomModel(19, 'K', 'Potassium', '#4D8946'),
    AtomModel(20, 'Ca', 'Calcium', '#F0F0F0'),
    AtomModel(21, 'Sc', 'Scandium', '#5FBB77'),
    AtomModel(22, 'Ti', 'Titanium', '#5A5A5A'),
    AtomModel(23, 'V', 'Vanadium', '#5F9EBB'),
    AtomModel(24, 'Cr', 'Chromium', '#A488B5'),
    AtomModel(25, 'Mn', 'Manganese', '#DC4A4A'),
    AtomModel(26, 'Fe', 'Iron', '#AB967D'),
    AtomModel(27, 'Co', 'Cobalt', '#4371E6'),
    AtomModel(28, 'Ni', 'Nickel', '#BAC395'),
    AtomModel(29, 'Cu', 'Copper', '#B95739'),
    AtomModel(30, 'Zn', 'Zinc', '#B4B4B4'),
    AtomModel(31, 'Ga', 'Gallium', '#39B975'),
    AtomModel(32, 'Ge', 'Germanium', '#979273'),
    AtomModel(33, 'As', 'Arsenic', '#738498'),
    AtomModel(34, 'Se', 'Selenium', '#424242'),
    AtomModel(35, 'Br', 'Bromine', '#D4753C'),
    AtomModel(36, 'Kr', 'Krypton', '#3CA0D4'),
    AtomModel(37, 'Rb', 'Rubidium', '#D22C1F'),
    AtomModel(38, 'Sr', 'Strontium', '#FF9D29'),
    AtomModel(39, 'Y', 'Yttrium', '#B129FF'),
    AtomModel(40, 'Zr', 'Zirconium', '#D6E43E'),
    AtomModel(41, 'Nb', 'Niobium', '#75DCEB'),
    AtomModel(42, 'Mo', 'Molybdenum', '#8BA38C'),
    AtomModel(43, 'Tc', 'Technetium', '#EEA1E2'),
    AtomModel(44, 'Ru', 'Ruthenium', '#563E32'),
    AtomModel(45, 'Rh', 'Rhodium', '#88D17A'),
    AtomModel(46, 'Pd', 'Palladium', '#9EABBE'),
    AtomModel(47, 'Ag', 'Silver', '#DCDCDC'),
    AtomModel(48, 'Cd', 'Cadmium', '#5560C8'),
    AtomModel(49, 'In', 'Indium', '#408D3C'),
    AtomModel(50, 'Sn', 'Tin', '#B5A47C'),
    AtomModel(51, 'Sb', 'Antimony', '#C6598C'),
    AtomModel(52, 'Te', 'Tellurium', '#827498'),
    AtomModel(53, 'I', 'Iodine', '#FF00FC'),
    AtomModel(54, 'Xe', 'Xenon', '#7888FF'),
    AtomModel(55, 'Cs', 'Caesium', '#FFD478'),
    AtomModel(56, 'Ba', 'Barium', '#E99C9C'),
    AtomModel(57, 'La', 'Lanthanum', '#8BDBBE'),
    AtomModel(58, 'Ce', 'Cerium', '#FF9329'),
    AtomModel(59, 'Pr', 'Praseodymium', '#56E019'),
    AtomModel(60, 'Nd', 'Neodymium', '#65898D'),
    AtomModel(61, 'Pm', 'Promethium', '#2EE99B'),
    AtomModel(62, 'Sm', 'Samarium', '#BD6475'),
    AtomModel(63, 'Eu', 'Europium', '#6C64BD'),
    AtomModel(64, 'Gd', 'Gadolinium', '#6E1289'),
    AtomModel(65, 'Tb', 'Terbium', '#359C50'),
    AtomModel(66, 'Dy', 'Dysprosium', '#447EE7'),
    AtomModel(67, 'Ho', 'Holmium', '#E77D46'),
    AtomModel(68, 'Er', 'Erbium', '#BF4987'),
    AtomModel(69, 'Tm', 'Thulium', '#21426B'),
    AtomModel(70, 'Yb', 'Ytterbium', '#878750'),
    AtomModel(71, 'Lu', 'Lutetium', '#D12C2C'),
    AtomModel(72, 'Hf', 'Hafnium', '#91D12C'),
    AtomModel(73, 'Ta', 'Tantalum', '#7F87AF'),
    AtomModel(74, 'W', 'Tungsten', '#2B6AA5'),
    AtomModel(75, 'Re', 'Rhenium', '#512F2F'),
    AtomModel(76, 'Os', 'Osmium', '#307060'),
    AtomModel(77, 'Ir', 'Iridium', '#C9876A'),
    AtomModel(78, 'Pt', 'Platinum', '#505008'),
    AtomModel(79, 'Au', 'Gold', '#EDC474'),
    AtomModel(80, 'Hg', 'Mercury', '#80A5AC'),
    AtomModel(81, 'Tl', 'Thallium', '#AC8089'),
    AtomModel(82, 'Pb', 'Lead', '#3C7C66'),
    AtomModel(83, 'Bi', 'Bismuth', '#FF0506'),
    AtomModel(84, 'Po', 'Polonium', '#FFFF00'),
    AtomModel(85, 'At', 'Astatine', '#00FF00'),
    AtomModel(86, 'Rn', 'Radon', '#DAE83A'),
    AtomModel(87, 'Fr', 'Francium', '#FF6C00'),
    AtomModel(88, 'Ra', 'Radium', '#00FFFF'),
    AtomModel(89, 'Ac', 'Actinium', '#424918'),
    AtomModel(90, 'Th', 'Thorium', '#AA3D82'),
    AtomModel(91, 'Pr', 'Protactinium', '#3DAA82'),
    AtomModel(92, 'U', 'Uranium', '#9CFF00'),
    AtomModel(93, 'Np', 'Neptunium', '#00AEFF'),
    AtomModel(94, 'Pu', 'Plutonium', '#FF9000'),
    AtomModel(95, 'Am', 'Americium', '#813349'),
    AtomModel(96, 'Cm', 'Curium', '#FF79D0'),
    AtomModel(97, 'Bk', 'Berkelium', '#AE877E'),
    AtomModel(98, 'Cf', 'Californium', '#8F3CB4'),
    AtomModel(99, 'Es', 'Einsteinium', '#86C4DC'),
    AtomModel(100, 'Fm', 'Fermium', '#BFDC86'),
    AtomModel(101, 'Md', 'Mendelevium', '#DC8686'),
    AtomModel(102, 'Nb', 'Nobelium', '#FFD965'),
    AtomModel(103, 'Lr', 'Lawrencium', '#5C24A0'),
    AtomModel(104, 'Rf', 'Rutherfordium', '#6B6675'),
    AtomModel(105, 'Db', 'Dubnium', '#B05032'),
    AtomModel(106, 'Sg', 'Seaborgium', '#254987'),
    AtomModel(107, 'Bh', 'Bohrium', '#9BAFA0'),
    AtomModel(108, 'Hs', 'Hassium', '#FF562D'),
    AtomModel(109, 'Mt', 'Meitnerium', '#CDCD2C'),
    AtomModel(110, 'Ds', 'Darmstadtium', '#3A7E48'),
    AtomModel(111, 'Rg', 'Roentgenium', '#FFFFFF'),
    AtomModel(112, 'Cn', 'Copernicium', '#AA4594'),
    AtomModel(113, 'Nh', 'Nihonium', '#8F8F8F'),
    AtomModel(114, 'Fl', 'Flerovium', '#2EEDE6'),
    AtomModel(115, 'Mc', 'Moscovium', '#BEAF64'),
    AtomModel(116, 'Lv', 'Livermorium', '#F22E6A'),
    AtomModel(117, 'Ts', 'Tennessine', '#70EA78'),
    AtomModel(118, 'Og', 'Oganesson', '#FF00B9'),
    AtomModel(119, 'Bn', 'Bananium', '#EDE674'),
    AtomModel(120, 'Gb', 'Gravityblockium', '#3DE6C3'),
    AtomModel(121, 'Bb', 'Breakingbadium', '#309141'),
    AtomModel(122, 'Tr', 'Timerunnerium', '#4DC8E6'),
    AtomModel(123, 'Sir', 'Sirnicanium', '#FF0000'),
    AtomModel(124, 'Ea', 'Earthium', '#1177F5'))


class AtomBase(Widget):
    board = ObjectProperty(None)
    angle = NumericProperty()
    waiting = BooleanProperty(True)
    acenter_x = NumericProperty()
    acenter_y = NumericProperty()
    color  = ObjectProperty(None)

    def __init__(self, board, **kwargs):
        super(AtomBase, self).__init__(**kwargs)
        self.board = board


class AtomText(AtomBase):
    text = StringProperty("")
    font_size = NumericProperty(20)
    text_color = ObjectProperty((0,0,0,1))

    def __init__(self, board, **kwargs):
        super(AtomText, self).__init__(board, **kwargs)


class Atom(AtomText):
    model  = ObjectProperty(None)
    symbol = StringProperty("")
    name   = StringProperty("")
    n      = NumericProperty()

    def __init__(self, n, board, **kwargs):
        model = ATOMS[n-1]
        super(Atom, self).__init__(board, **kwargs)
        self.model  = ATOMS[n-1]
        self.n      = self.model.n
        self.color  = get_color_from_hex(self.model.color)
        self.symbol = self.model.symbol
        self.name   = self.model.name


class AtomPlus(AtomText):
    pass

class AtomMinus(AtomPlus):
    pass


class Neutrino(AtomBase):
    pass


class AtomDarkPlus(AtomPlus):
    pass
