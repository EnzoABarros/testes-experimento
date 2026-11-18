"""
Suíte de Testes (PyTest) — P8 (Médio): Sistema de Gerenciamento de Pedidos de Restaurante
Total: 10 testes focados em máquina de estados, invariantes e acoplamento de estrutura.
"""

import pytest

try:
    from p8 import EstadoPedido, ItemPedido, Pedido, ProdutoCardapio, RestauranteSystem
except ImportError:
    from restaurante import EstadoPedido, ItemPedido, Pedido, ProdutoCardapio, RestauranteSystem


class TestRestauranteP8:
    @pytest.fixture
    def sistema(self):
        sys = RestauranteSystem()
        sys.cadastrar_produto_cardapio(ProdutoCardapio(1, "Pizza Margherita", 45.00))
        sys.cadastrar_produto_cardapio(ProdutoCardapio(2, "Refrigerante 600ml", 8.00))
        return sys

    def test_01_cadastro_cardapio_e_bloqueio_duplicidade(self, sistema):
        with pytest.raises(ValueError):
            sistema.cadastrar_produto_cardapio(ProdutoCardapio(1, "Pizza Calabresa", 50.00))

    def test_02_criacao_pedido_estado_inicial_pendente(self, sistema):
        pedido = sistema.registrar_pedido(id_pedido=10)
        assert pedido.estado == EstadoPedido.PENDENTE
        assert pedido.calcular_total() == 0.0

    def test_03_bloqueio_produto_inexistente_cardapio(self, sistema):
        sistema.registrar_pedido(1)
        with pytest.raises((KeyError, ValueError)):
            sistema.adicionar_item_ao_pedido(id_pedido=1, id_produto=99, quantidade=1)

    def test_04_validacao_quantidade_estritamente_positiva(self, sistema):
        sistema.registrar_pedido(1)
        with pytest.raises(ValueError):
            sistema.adicionar_item_ao_pedido(id_pedido=1, id_produto=1, quantidade=0)

        with pytest.raises(ValueError):
            sistema.adicionar_item_ao_pedido(id_pedido=1, id_produto=1, quantidade=-2)

    def test_05_agregacao_itens_repetidos_e_calculo_total(self, sistema):
        pedido = sistema.registrar_pedido(1)
        sistema.adicionar_item_ao_pedido(1, id_produto=1, quantidade=2)  # 90.00
        sistema.adicionar_item_ao_pedido(1, id_produto=1, quantidade=1)  # +45.00
        sistema.adicionar_item_ao_pedido(1, id_produto=2, quantidade=3)  # +24.00
        assert pedido.calcular_total() == 159.00

    def test_06_remocao_item_pedido_e_bloqueio_inexistente(self, sistema):
        pedido = sistema.registrar_pedido(1)
        sistema.adicionar_item_ao_pedido(1, id_produto=1, quantidade=1)
        sistema.adicionar_item_ao_pedido(1, id_produto=2, quantidade=2)

        sistema.remover_item_do_pedido(1, id_produto=1)
        assert 1 not in pedido.itens
        assert pedido.calcular_total() == 16.00

        with pytest.raises((KeyError, ValueError)):
            sistema.remover_item_do_pedido(1, id_produto=1)

    def test_07_bloqueio_edicao_itens_apos_sair_de_pendente(self, sistema):
        sistema.registrar_pedido(1)
        sistema.adicionar_item_ao_pedido(1, id_produto=1, quantidade=1)
        sistema.atualizar_estado_pedido(1, EstadoPedido.EM_PREPARACAO)

        with pytest.raises(ValueError):
            sistema.adicionar_item_ao_pedido(1, id_produto=2, quantidade=1)

        with pytest.raises(ValueError):
            sistema.remover_item_do_pedido(1, id_produto=1)

    def test_08_sequencia_valida_maquina_estados(self, sistema):
        pedido = sistema.registrar_pedido(1)

        sistema.atualizar_estado_pedido(1, EstadoPedido.EM_PREPARACAO)
        assert pedido.estado == EstadoPedido.EM_PREPARACAO

        sistema.atualizar_estado_pedido(1, EstadoPedido.PRONTO)
        assert pedido.estado == EstadoPedido.PRONTO

        sistema.atualizar_estado_pedido(1, EstadoPedido.FINALIZADO)
        assert pedido.estado == EstadoPedido.FINALIZADO

    def test_09_bloqueio_saltos_retrocessos_e_pos_finalizado(self, sistema):
        sistema.registrar_pedido(1)

        # Salto: PENDENTE -> PRONTO
        with pytest.raises(ValueError):
            sistema.atualizar_estado_pedido(1, EstadoPedido.PRONTO)

        sistema.atualizar_estado_pedido(1, EstadoPedido.EM_PREPARACAO)

        # Retrocesso: EM_PREPARACAO -> PENDENTE
        with pytest.raises(ValueError):
            sistema.atualizar_estado_pedido(1, EstadoPedido.PENDENTE)

        sistema.atualizar_estado_pedido(1, EstadoPedido.PRONTO)
        sistema.atualizar_estado_pedido(1, EstadoPedido.FINALIZADO)

        # Alteração após FINALIZADO
        with pytest.raises(ValueError):
            sistema.atualizar_estado_pedido(1, EstadoPedido.EM_PREPARACAO)

    def test_10_filtragem_pedidos_por_cada_estado(self, sistema):
        p1 = sistema.registrar_pedido(1)
        p2 = sistema.registrar_pedido(2)
        p3 = sistema.registrar_pedido(3)
        p4 = sistema.registrar_pedido(4)

        sistema.atualizar_estado_pedido(2, EstadoPedido.EM_PREPARACAO)

        sistema.atualizar_estado_pedido(3, EstadoPedido.EM_PREPARACAO)
        sistema.atualizar_estado_pedido(3, EstadoPedido.PRONTO)

        sistema.atualizar_estado_pedido(4, EstadoPedido.EM_PREPARACAO)
        sistema.atualizar_estado_pedido(4, EstadoPedido.PRONTO)
        sistema.atualizar_estado_pedido(4, EstadoPedido.FINALIZADO)

        assert sistema.listar_pedidos_por_estado(EstadoPedido.PENDENTE) == [p1]
        assert sistema.listar_pedidos_por_estado(EstadoPedido.EM_PREPARACAO) == [p2]
        assert sistema.listar_pedidos_por_estado(EstadoPedido.PRONTO) == [p3]
        assert sistema.listar_pedidos_por_estado(EstadoPedido.FINALIZADO) == [p4]
