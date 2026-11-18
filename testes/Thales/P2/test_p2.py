"""
Suíte de Testes (PyTest) — P2 (Fácil): Sistema de Gerenciamento de Lista de Compras
Total: 6 testes focados em ambiguidades de interpretação e regras de consistência.
"""

import pytest

try:
    from p2 import ListaDeComprasSystem, Produto
except ImportError:
    from lista_compras import ListaDeComprasSystem, Produto


class TestListaDeComprasP2:
    @pytest.fixture
    def sistema(self):
        return ListaDeComprasSystem()

    def test_01_adicionar_e_consultar_produtos(self, sistema):
        prod = Produto(id_produto=1, nome="Leite", quantidade=2, preco_unitario=4.50)
        sistema.adicionar_produto(prod)

        produtos = sistema.consultar_produtos()
        assert len(produtos) == 1
        assert produtos[0].id_produto == 1
        assert produtos[0].comprado is False

    def test_02_bloqueio_produto_duplicado(self, sistema):
        sistema.adicionar_produto(Produto(1, "Arroz", 1, 20.0))
        with pytest.raises((ValueError, KeyError)):
            sistema.adicionar_produto(Produto(1, "Arroz", 2, 22.0))

    def test_03_validacao_valores_negativos_e_limite_zero(self, sistema):
        # Limite zero deve ser aceito ("quantidades negativas ou preços inferiores a zero")
        prod_zero = Produto(1, "Brinde", quantidade=0, preco_unitario=0.0)
        sistema.adicionar_produto(prod_zero)
        assert sistema.calcular_valor_total_estimado() == 0.0

        with pytest.raises(ValueError):
            Produto(2, "Feijão", quantidade=-1, preco_unitario=8.0)

        with pytest.raises(ValueError):
            Produto(3, "Café", quantidade=1, preco_unitario=-0.01)

    def test_04_remocao_restrita_a_itens_cadastrados(self, sistema):
        sistema.adicionar_produto(Produto(1, "Açúcar", 2, 5.0))
        sistema.remover_produto(1)
        assert sistema.consultar_produtos() == []

        with pytest.raises((KeyError, ValueError)):
            sistema.remover_produto(1)

    def test_05_atualizacao_e_separacao_pendentes_comprados(self, sistema):
        sistema.adicionar_produto(Produto(1, "Manteiga", 1, 10.0))
        sistema.adicionar_produto(Produto(2, "Queijo", 1, 20.0))

        sistema.atualizar_produto(1, quantidade=3, preco_unitario=9.50)
        sistema.marcar_como_comprado(1)

        pendentes = sistema.consultar_pendentes()
        comprados = sistema.consultar_comprados()

        assert [p.id_produto for p in pendentes] == [2]
        assert [p.id_produto for p in comprados] == [1]
        assert comprados[0].quantidade == 3
        assert comprados[0].preco_unitario == 9.50

    def test_06_calculo_valor_total_estimado(self, sistema):
        sistema.adicionar_produto(Produto(1, "Item A", 2, 10.50))  # 21.00
        sistema.adicionar_produto(Produto(2, "Item B", 3, 4.10))   # 12.30
        assert sistema.calcular_valor_total_estimado() == 33.30
