"""
Testes automatizados de regressão - Página de Certificação
Apenas o que faz sentido automatizar: verificações consistentes e repetitivas
"""
import pytest
from pages.certificacao_page import CertificacaoPage

class TestCertificacaoRegressao:
    
    def test_pagina_carrega_sem_erros(self, browser):
        """Página deve carregar sem erros 500"""
        pagina = CertificacaoPage(browser).navegar()
        status_code = pagina.obter_status_code()
        assert status_code == 200, f"Erro {status_code} ao carregar página"
    
    def test_elementos_principais_presentes(self, browser):
        """Verifica se elementos estruturais existem (não se funcionam)"""
        pagina = CertificacaoPage(browser).navegar()
        
        assert pagina.botao_inscrever_existe(), "Botão 'Inscreva-se' não encontrado no DOM"
        assert pagina.indicador_etapa_existe(), "Indicador de etapa não encontrado"
    
    @pytest.mark.slow
    def test_tempo_carregamento_aceitavel(self, browser):
        """Verifica performance básica de carregamento"""
        import time
        
        start = time.time()
        CertificacaoPage(browser).navegar()
        load_time = time.time() - start
        
        assert load_time < 5, f"Página lenta: {load_time:.2f}s (limite: 5s)"
        print(f"Tempo de carregamento: {load_time:.2f}s")