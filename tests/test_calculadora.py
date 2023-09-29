from src.calculadora import Calculadora


class Test_calculadora:

    def teste_adicao(self):
        reusultado = Calculadora.adicao(2,3)
        assert reusultado == 5
    
    def teste_adicao2(self):
        resultado = Calculadora.adicao(2,5)
        assert resultado == 7

    def teste_divisao(self):
        resultado = Calculadora.divisao(2,2)
        assert resultado == 1

    def teste_divisao_por_zero(self):
        resultado = Calculadora.divisao(2,0)
        assert resultado == 'Erro'
    
    def teste_multiplicacao(self):
        resultado = Calculadora.multiplicacao(2,5)
        assert resultado == 10
