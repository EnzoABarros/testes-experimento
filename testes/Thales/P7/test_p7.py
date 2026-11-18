"""
Suíte de Testes (PyTest) — P7 (Médio): Sistema de Gerenciamento de Estacionamento
Total: 10 testes focados em controle temporal, arredondamento de horas e acoplamento.
"""

from datetime import datetime, timedelta
import pytest

try:
    from p7 import EstacionamentoSystem, RegistroMovimentacao, Veiculo
except ImportError:
    from estacionamento import EstacionamentoSystem, RegistroMovimentacao, Veiculo


class TestEstacionamentoP7:
    @pytest.fixture
    def estacionamento(self):
        return EstacionamentoSystem(capacidade_vagas=2, valor_hora=10.0)

    def test_01_entrada_e_ocupacao_vagas(self, estacionamento):
        entrada = datetime(2026, 3, 30, 10, 0, 0)
        estacionamento.registrar_entrada("ABC-1234", entrada)

        assert estacionamento.vagas_disponiveis() == 1
        estacionados = estacionamento.listar_estacionados()
        assert len(estacionados) == 1
        assert estacionados[0].placa == "ABC-1234"

    def test_02_normalizacao_placa_e_bloqueio_duplicidade(self, estacionamento):
        entrada = datetime(2026, 3, 30, 10, 0, 0)
        estacionamento.registrar_entrada("abc-1234", entrada)

        with pytest.raises(ValueError):
            estacionamento.registrar_entrada("ABC-1234", entrada)

    def test_03_bloqueio_estacionamento_lotado(self, estacionamento):
        entrada = datetime(2026, 3, 30, 10, 0, 0)
        estacionamento.registrar_entrada("CAR-0001", entrada)
        estacionamento.registrar_entrada("CAR-0002", entrada)

        assert estacionamento.vagas_disponiveis() == 0
        with pytest.raises(ValueError):
            estacionamento.registrar_entrada("CAR-0003", entrada)

    def test_04_bloqueio_saida_veiculo_nao_estacionado(self, estacionamento):
        with pytest.raises((ValueError, KeyError)):
            estacionamento.registrar_saida("XYZ-9999", datetime(2026, 3, 30, 11, 0, 0))

    def test_05_validacao_temporal_saida_anterior_entrada(self, estacionamento):
        entrada = datetime(2026, 3, 30, 10, 0, 0)
        estacionamento.registrar_entrada("ABC-1234", entrada)

        with pytest.raises(ValueError):
            estacionamento.registrar_saida("ABC-1234", entrada - timedelta(seconds=1))

    def test_06_cobranca_permanencia_zero_segundos(self, estacionamento):
        entrada = datetime(2026, 3, 30, 10, 0, 0)
        estacionamento.registrar_entrada("ZERO-001", entrada)
        valor = estacionamento.registrar_saida("ZERO-001", entrada)
        assert valor == 0.0

    def test_07_cobranca_fracao_adicional_arredonda_para_cima(self, estacionamento):
        entrada = datetime(2026, 3, 30, 10, 0, 0)
        estacionamento.registrar_entrada("FRAC-001", entrada)
        # 1 hora e 1 segundo deve cobrar 2 horas cheias
        valor = estacionamento.registrar_saida("FRAC-001", entrada + timedelta(hours=1, seconds=1))
        assert valor == 20.0

    def test_08_cobranca_hora_exata_sem_hora_extra(self, estacionamento):
        entrada = datetime(2026, 3, 30, 10, 0, 0)
        estacionamento.registrar_entrada("EXAT-001", entrada)
        # 2 horas exatas não podem gerar cobrança de 3 horas
        valor = estacionamento.registrar_saida("EXAT-001", entrada + timedelta(hours=2))
        assert valor == 20.0

    def test_09_reconfiguracao_valor_hora_dinamica(self, estacionamento):
        entrada = datetime(2026, 3, 30, 10, 0, 0)
        estacionamento.registrar_entrada("TAR-0001", entrada)
        estacionamento.set_valor_hora(15.0)

        valor = estacionamento.registrar_saida("TAR-0001", entrada + timedelta(minutes=30))
        assert valor == 15.0

    def test_10_historico_movimentacoes_integro(self, estacionamento):
        entrada = datetime(2026, 3, 30, 8, 0, 0)
        saida = datetime(2026, 3, 30, 9, 15, 0)  # 2h * 10.0 = 20.0

        estacionamento.registrar_entrada("HIST-01", entrada)
        estacionamento.registrar_saida("HIST-01", saida)

        historico = estacionamento.consultar_historico()
        assert len(historico) == 1
        assert historico[0].placa == "HIST-01"
        assert historico[0].valor_cobrado == 20.0
        assert estacionamento.vagas_disponiveis() == 2
