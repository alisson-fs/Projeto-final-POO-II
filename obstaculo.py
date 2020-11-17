from objeto import Objeto


class Obstaculo(Objeto):
    def __init__(self,
                 posicao: list,
                 nome: str,
                 tela: object,
                 anim: list,
                 velocidade: int):
        super().__init__(posicao, nome, tela, anim, velocidade)
        self.img_atual = self.anim[0]

        self.rect = self.img_atual.get_rect()
        self.pos_inicial()

        self.spriteNum = 0
        self.spriteNumMax = len(self.anim)

        self.spriteTimer = 0
        self.spriteTimerMax = 4

    def update(self):
        self.rect.y += self.velocidade
        if (self.rect.top >= self.tela.height):
            self.kill()
