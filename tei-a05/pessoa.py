class pessoa:
    #construtor
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def setNome(self,nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome

    def setIdade(self,idade):
        self.idade = idade
    
    def getIdade(self):
        return self.idade

    def __str__(self):
        return "%s %s"%(self.nome,self.idade)

class pessoaFisica(pessoa):
    #construtor
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def setCpf(self,cpf):
        self.nome = nome
    
    def getCpf(self):
        return self.cpf

    def __str__(self):
        return "%s \n%s"%(super().__str__(), self.cpf)