from funcionarios import *

class Aplicacao:
    def __init__(self) -> None:

        self.Banco_Dados = [] # AQUI DENTRO ESTARA AS INFOMAÇÕES DOS FUNCIONARIOS
        
        while True:
            
           print('''
            ====================================================
                  CADASTRO DE FUNCIONARIOS DA EMPRESA 
            ====================================================
            
               1. > INCLUIR FUNCIONARIO
               2. > ALTERAR FUNCIONARIO
               3. > EXCLUIR FUNCIONARIO
               4. > CONSULTAR 1 FUNCIONARIO
               5. > CONSULTAR QUADRO GERAL DE FUNCIONARIOS
               6. > SAIR DO SISTEMA
        
            =====================================================
             ***************** ///////////////******************    
            =====================================================
            ''')
        
           Op = int(input('DIGITE SUA OPÇÃO:   '))
           if Op == 6:
               print('Saindo do Sistema...')
               break
           elif Op == 1:
               self.incluir_func()
           elif Op == 2: 
               self.alterar_func()
           elif Op == 3:
               self.excluir_func()
           elif Op == 4:
               self.consultar_func()
           elif Op == 5:
                self.consultar_quadro()
           else:
                print('='*50)
                print('ESTÁ OPÇÃO É INVALIDA !!!')
                print('='*50)
        
        print('===================APLICAÇÃO ENCERRADA=====================')
        
# AQUI FAZEMOS A INCLUSÃO DOS FUNCIONARIOS    
    
    def incluir_func(self):
        print('===================INCLUIR FUNCIONARIOS======================')
        print('=============================================================')
        id_fun = int(input('Digite o Identificador do Funcionario:  '))
        nome_fun = input('Digite o Nome do Funcionario:         ')
        cargo_fun = input('Digite o Cargo do Funcionario:       ')
        salario_fun = float(input('Digite o Salario do funcionario:     '))
        funcionarios = Funcionarios(id_fun,nome_fun,cargo_fun,salario_fun)
        self.Banco_Dados.append(funcionarios)
            
# AQUI FAZEMOS A ALTERAÇÃO DO FUNCIONARIO DANDO UM FOR E CRIANDO UMA VARIAVEL NOVA              
    def alterar_func(self):
        print('==================ALTERAR FUNCIONARIO=======================')
        print('============================================================')
        self.consultar_quadro()
        id_fun = int(input('Digite o Identificador do Funcionario:    '))
        
        print('===============DIGITE AS ALTERAÇÕES NECESSARIA==============')
        
        for f in self.Banco_Dados:
            if f.id_func == id_fun:
                nome_fun = input('Digite o Nome do Funcionario:         ')
                cargo_fun = input('Digite o Cargo do Funcionario:       ')
                salario_fun = float(input('Digite o Salario do funcionario:     '))
                f.nome_fun = nome_fun
                f.cargo_fun = cargo_fun
                f.salrio_fun = salario_fun
                 
        self.consultar_quadro()                         
        
        
# AQUI EXCLUIMOS O FUNCIONARIO PELO SEU ID, E DAMOS UM REMOVE EM BANCO DADOS         
    def excluir_func(self):
        print('==============EXCLUIR FUNCIONARIO======================')
        print('===========================================================')
        id_fun = int(input('Digite o Identificador do Funcionario:  '))
        print('===========================================================')
        for f in self.Banco_Dados:
            if id_fun == f.id_func:
               self.Banco_Dados.remove(f)    
    
# AQUI CONSULTA APENAS 1 FUNCIONARIO COM SEU ID, FAZ UM FOR EM BANCO DE DADOS        
    def consultar_func(self):
        print('==============CONSULTAR 1 FUNCIONARIO======================')
        print('===========================================================')
        id_fun = int(input('Digite o Identificador do Funcionario:  '))
        print('===========================================================')
        for f in self.Banco_Dados:
            if id_fun == f.id_func:
               print('====================================================') 
               print(f.id_func, f.nome_func, f.cargo_func, f.salario_func)
               print('====================================================')

# AQUI CONSULTA O QUADRO GERAL = FAZ UM FOR DENTRO DE BANCO DE DADOS E PRINTA CADA FUNCIONARIO        
    def consultar_quadro(self):
        print('===================QUADRO DE FUNCIONARIOS======================')
        print('===============================================================')
        for f in self.Banco_Dados:
            print('=====================================================')
            print(f.id_func, f.nome_func, f.cargo_func, f.salario_func)
            print('=====================================================')
            
            
# ============================================================================    
if __name__ == '__main__':
    app = Aplicacao()     
    
# a Aplicação só roda se tiver Indentificando aqui
# pq especificamos em funcionario que rodaria se 
# houvesse dentro de uma classe 