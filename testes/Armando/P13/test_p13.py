"""P13: 10 testes objetivos, equivalentes para os tratamentos A e B."""
from p13 import selecionar_projetos


def proj(ident, custo, beneficio, deps=None):
    return {'id':ident,'custo':custo,'beneficio':beneficio,'dependencias':[] if deps is None else deps}


def test_01_sem_projetos():
    assert selecionar_projetos([], 10) == {'projetos':[], 'beneficio_total':0, 'custo_total':0}


def test_02_orcamento_zero():
    assert selecionar_projetos([proj('A',1,10)],0) == {'projetos':[], 'beneficio_total':0, 'custo_total':0}


def test_03_escolha_simples():
    assert selecionar_projetos([proj('A',2,5),proj('B',4,8)],4) == {
        'projetos':['B'],'beneficio_total':8,'custo_total':4
    }


def test_04_escolha_global_supera_guloso():
    itens=[proj('A',10,10),proj('B',6,9),proj('C',4,8)]
    assert selecionar_projetos(itens,10)=={'projetos':['B','C'],'beneficio_total':17,'custo_total':10}


def test_05_dependencia_direta_obrigatoria():
    itens=[proj('A',4,10,['B']),proj('B',3,2),proj('C',3,6)]
    assert selecionar_projetos(itens,7)=={'projetos':['A','B'],'beneficio_total':12,'custo_total':7}


def test_06_dependencias_transitivas():
    itens=[proj('A',4,15,['B']),proj('B',3,4,['C']),proj('C',2,1),proj('D',5,10)]
    assert selecionar_projetos(itens,9)=={'projetos':['A','B','C'],'beneficio_total':20,'custo_total':9}


def test_07_dependencia_compartilhada_contada_uma_vez():
    itens=[proj('A',3,8,['C']),proj('B',3,7,['C']),proj('C',2,2),proj('D',6,12)]
    assert selecionar_projetos(itens,8)=={'projetos':['A','B','C'],'beneficio_total':17,'custo_total':8}


def test_08_desempate_menor_custo():
    itens=[proj('A',5,10),proj('B',4,10),proj('C',2,2)]
    assert selecionar_projetos(itens,5)=={'projetos':['B'],'beneficio_total':10,'custo_total':4}


def test_09_desempate_lexicografico():
    itens=[proj('B',3,5),proj('A',3,5),proj('C',5,2)]
    assert selecionar_projetos(itens,3)=={'projetos':['A'],'beneficio_total':5,'custo_total':3}


def test_10_limite_de_18_projetos():
    itens=[proj(f'P{i:02d}',1,i) for i in range(1,19)]
    assert selecionar_projetos(itens,5)=={
        'projetos':['P14','P15','P16','P17','P18'],'beneficio_total':80,'custo_total':5
    }
