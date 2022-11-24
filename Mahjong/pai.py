from mahjong.constants import HAKU, HATSU, CHUN

from constants import Wind, Dragon


class Pai:
    def __init__(
        self,
        type:str,
        kind:int,
        is_red:bool=False
    ):
        assert type in ['m', 'p', 's', 'w', 'd']
        if is_red:
            assert type in ['m', 'p', 's'] and 5 == kind
        
        self.is_su     = False
        self.is_wind   = False
        self.is_dragon = False
        if type in ['m', 'p', 's']:
            assert 1 <= kind <= 9
            self.is_su = True
        elif 'w' == type:
            assert kind in Wind.winds
            self.is_wind = True
        elif 'd' == type:
            assert kind in Dragon.dragons
            self.is_dragon = True
                
        self.type   = type
        self.kind   = kind
        self.is_red = is_red
        
    def __str__(self):
        bg_color = '\033[47m'
        text_color = '\033[31m' if self.is_red or CHUN is self.kind else '\033[32m' if HATSU is self.kind else '\033[37m' if HAKU is self.kind else '\033[30m'
        if self.is_su:
            sub_color = '\033[31m' if 'm' == self.type else '\033[34m' if 'p' == self.type else '\033[32m'
            return f'{bg_color}{text_color}{self.kind}{sub_color}{self.type}\033[0m'
        elif self.is_wind:
            return f'{bg_color}{text_color}{Wind.winds_jp[self.kind]}\033[0m'
        elif self.is_dragon:
            return f'{bg_color}{text_color}{Dragon.dragons_jp[self.kind]}\033[0m'
     
    def __int__(self):
        return ['m', 'p', 's', 'w', 'd'].index(self.type) * 100 + self.is_red * 10 + self.kind
    
    def __lt__(self, other):
        return int(self) < int(other)
    
        
class Paiset:
    def __init__(self, pais:list[Pai]):
        self.pais:list[Pai] = pais
        
    def __str__(self):
        return ' '.join(list(map(str, self.pais)))
    
    def __len__(self):
        return len(self.pais)
    
    def __getitem__(self, i):
        if type(i) == int:
            return self.pais[i]
        else:
            return Paiset(self.pais[i])
        
    def __add__(self, other):
        if type(other) == Pai:
            self.pais.append(other)
        else:
            self.pais += other.pais
            
        return self
        
    @property
    def sorted(self):
        return Paiset(sorted(self.pais))
    
    def pop(self, i):
        return self.pais.pop(i)
    
    def append(self, item):
        self.pais.append(item)
        
        
def all_pais(
    number_of_players:int,
    has_red:bool=True
) -> list[Pai]:
    assert number_of_players in [3, 4]
    pais = []
    
    pais += [Pai(type='m', kind=1) for _ in range(4)]
    if 4 == number_of_players:
        pais += [Pai(type='m', kind=kind) for kind in range(2, 5) for _ in range(4)]
        pais += [Pai(type='m', kind=5) for _ in range(3)]
        pais += [Pai(type='m', kind=5, is_red=has_red)]
        pais += [Pai(type='m', kind=kind) for kind in range(6, 9) for _ in range(4)]
    pais += [Pai(type='m', kind=9) for _ in range(4)]
    
    pais += [Pai(type='p', kind=kind) for kind in range(1, 5) for _ in range(4)]
    pais += [Pai(type='p', kind=5) for _ in range(3)]
    pais += [Pai(type='p', kind=5, is_red=has_red)]
    pais += [Pai(type='p', kind=kind) for kind in range(6, 10) for _ in range(4)]
    
    pais += [Pai(type='s', kind=kind) for kind in range(1, 5) for _ in range(4)]
    pais += [Pai(type='s', kind=5) for _ in range(3)]
    pais += [Pai(type='s', kind=5, is_red=has_red)]
    pais += [Pai(type='s', kind=kind) for kind in range(6, 10) for _ in range(4)]
    
    pais += [Pai(type='w', kind=wind) for wind in Wind.winds for _ in range(4)]
    pais += [Pai(type='d', kind=dragon) for dragon in Dragon.dragons for _ in range(4)]
        
    return pais
