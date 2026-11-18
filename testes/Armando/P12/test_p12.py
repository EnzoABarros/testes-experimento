"""P12: 10 testes objetivos, equivalentes para os tratamentos A e B."""
from p12 import calcular_rota


def test_01_rota_direta():
    assert calcular_rota([('A','B',7)], 'A', 'B') == {'custo':7, 'rota':['A','B']}


def test_02_caminho_indireto_mais_barato():
    trechos=[('A','B',4),('A','C',2),('C','B',1),('B','D',3),('C','D',7)]
    assert calcular_rota(trechos,'A','D') == {'custo':6, 'rota':['A','C','B','D']}


def test_03_direcao_nao_invertida():
    assert calcular_rota([('A','B',1),('B','C',1)],'C','A') is None


def test_04_origem_igual_destino_sem_trechos():
    assert calcular_rota([], 'X', 'X') == {'custo':0, 'rota':['X']}


def test_05_destino_inalcancavel():
    assert calcular_rota([('A','B',2),('C','D',1)], 'A', 'D') is None


def test_06_desempate_caminho_completo():
    # Em custo igual, ['A','B','Z'] precede ['A','C','Z'].
    t=[('A','C',1),('C','Z',2),('A','B',2),('B','Z',1)]
    assert calcular_rota(t,'A','Z') == {'custo':3,'rota':['A','B','Z']}


def test_07_desempate_com_mais_arestas():
    # Não priorizar caminhos com menos saltos: vale o desempate lexicográfico.
    t=[('A','D',4),('A','B',1),('B','C',1),('C','D',2)]
    assert calcular_rota(t,'A','D') == {'custo':4, 'rota':['A','B','C','D']}


def test_08_multiarestas_e_ciclo():
    t=[('A','B',9),('A','B',2),('B','A',1),('B','C',3),('A','C',10)]
    assert calcular_rota(t,'A','C') == {'custo':5,'rota':['A','B','C']}


def test_09_custo_nao_equivale_numero_saltos():
    t=[('A','D',50),('A','B',8),('B','C',6),('C','D',4),('A','C',20)]
    assert calcular_rota(t,'A','D') == {'custo':18,'rota':['A','B','C','D']}


def test_10_rede_extensa_linear():
    # 400 arestas: verifica viabilidade para uma instância maior.
    t=[(f'N{i:03d}', f'N{i+1:03d}', 1) for i in range(400)]
    t.append(('N000','N400',500))
    assert calcular_rota(t,'N000','N400') == {
        'custo':400, 'rota':[f'N{i:03d}' for i in range(401)]
    }
