class Aluno: 
    nome = '' 
    ra = 0 
    sala = '' 
    ano = 0 
    notas = [] 
    media = 0 
    aluno_status = ''
    def __init__(self, nome = '', ra = 0, sala = '', ano = 0, notas =[], media = 0, aluno_status = ''): 
        self.nome = nome 
        self.ra = ra 
        self.sala = sala 
        self.ano = ano 
        self.notas = notas 
        self.media = media 
        self.aluno_status = aluno_status
    

opcao = 0
alunos = [] 
qtd_provas = []
notas = []
 
def menu(): 
    print('=' *40)
    print(''' Digite a opção do menu desejada: 
    [1] Cadastro de alunos  
    [2] Obter informações 
    [3] Cadastrar notas     
    [4] Calcular média
    [5] Fechar programa''')
    print('=' *40) 
menu()


def cadastro_aluno(): 
    print('=\n'*4)
    print('=' *40)
    print('TELA DE CADASTRO DE ALUNOS')
    print('='*40)
    ra = int(input('Digite o ra: \n')) 
    if(len(alunos) > 0): 
        for aluno in alunos: 
            if(aluno.ra == ra): 
                print('Aluno já cadastrado!') 
                return  
        estudante = input('Digite o nome do aluno: \n') 
        sala = input('Digite em que sala o aluno está matriculado: \n')
        ano = input('Digite que ano o aluno está matriculado: \n')
        print('Aluno cadastrado com sucesso!')
        alunos.append(Aluno(ra = ra, nome = estudante, sala = sala, ano = ano))

            
    else: 
        estudante = input('Digite o nome do aluno: \n')
        sala = input('Digite em que sala o aluno está matriculado: \n')
        ano = input ('Informe o ano em que o aluno está matriculado: \n')
        print('Aluno cadastrado com sucesso!')
        alunos.append(Aluno(ra = ra, nome = estudante, sala = sala, ano = ano)) 


def obter_informacoes():
    print('=\n'*4)
    ra = int(input('Por favor insira o ra do aluno que você deseja obter informações: \n'))
    if (len(alunos) > 0):
        for aluno in alunos:
            if (aluno.ra == ra):
                print(f'O aluno matriculado no RA:{aluno.ra}, é o(a) {aluno.nome} e está no {aluno.ano}{aluno.sala}.')
                print(f'A média do mesmo é {aluno.media}')
                break
            else:
                print('Esse aluno não se encontra cadastrado, por favor cadastre-o!')
                cadastro_aluno()    
    else:
        print('Ainda não há nenhum aluno cadastrado no sistema, por favor cadastre algum aluno para continuarmos.')
        cadastro_aluno()


def cadastro_notas():
    print('=\n'*4)
    print('='*40)
    print('TELA DE CADASTRO DE NOTAS') 
    print('='*40)
    ra = int(input('Por favor, insira o RA do aluno que você deseja cadastrar uma nota nova!: \n'))
    if (len(alunos) > 0):
        for aluno in alunos:
            if (aluno.ra == ra):
                aluno.notas.append(float(input(f'Digite a nota que você deseja cadastrar para o {aluno.nome}: \n')))
                break
            else:
                print('Esse aluno não se encontra cadastrado, por favor cadastre-o!')
                cadastro_aluno()
                break
    else: 
        print('Ainda não há nenhum aluno cadastrado no sistema, por favor cadastre algum aluno para continuarmos.')
        cadastro_aluno()

def calculo_media():
    print('=\n'*4)
    print('=' *40)
    print('TELA DE CÁLCULO DE MÉDIA')
    print('='*40)
    ra = int(input('Digite o ra do aluno que você deseja calcular a média: \n'))
    if (len(alunos) > 0):
        for aluno in alunos:
            if (aluno.ra == ra):
                media = 0 
                for nota in aluno.notas: 
                    media += nota 
                aluno.media = media / len(aluno.notas) 
                return                
            else:
                print('Esse aluno não se encontra cadastrado, por favor cadastre-o!')
                cadastro_aluno()
    else:
        print('Ainda não há nenhum aluno cadastrado no sistema, por favor cadastre algum aluno para continuarmos.')
        cadastro_aluno()


while opcao !=5:
    opcao = int(input('Escolha a opção que você deseja: '))
    if opcao == 1: 
        cadastro_aluno() 
    elif opcao == 2: 
        obter_informacoes()
    elif opcao == 3:
        cadastro_notas()
    elif opcao == 4:
        calculo_media()
    elif opcao ==5:
        print('Obrigador por utilizar os nossos serviços, volte sempre que precisar!')
    else:
        print('Opção inválida, por favor tente novamente!') 
 