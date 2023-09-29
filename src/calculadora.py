class Calculadora:

    @staticmethod
    def adicao (a, b):
        return a+b
    
    @staticmethod
    def divisao (a, b):
        if b == 0:
            return 'Erro'
        return a/b
    
    @staticmethod
    def multiplicacao (a, b):
        return a*b