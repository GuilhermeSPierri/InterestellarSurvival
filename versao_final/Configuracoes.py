class Configuracoes:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Configuracoes, cls).__new__(cls)
            # Adicione aqui as configurações globais que deseja gerenciar
            cls._instance.__titulo = 'Interstellar Survival'
            cls._instance.__caminho_background = 'versao_final/assets/imgs/bg.png'
            cls._instance.__FPS = 80
            cls._instance.__largura_tela = 1100
            cls._instance.__altura_tela = 660
            cls._instance.__caminho_fonte1 = 'versao_final/assets/fonts/PixelGameFont.ttf'
            cls._instance.__caminho_imagem_jogador = 'versao_final/assets/imgs/jogadorbase.png'
            cls._instance.__sprites_jogador = ['versao_final/assets/imgs/jogadorbase.png',
                                            'versao_final/assets/imgs/jogadorbase2.png',
                                            'versao_final/assets/imgs/jogadorbase3.png',
                                            'versao_final/assets/imgs/jogadorbase4.png'
                                            ]
            cls._instance.__caminho_imagem_explosao1 = [
                    'versao_final/assets/imgs/Explosion3_1.png','versao_final/assets/imgs/Explosion3_2.png',
                    'versao_final/assets/imgs/Explosion3_3.png','versao_final/assets/imgs/Explosion3_4.png',
                    'versao_final/assets/imgs/Explosion3_5.png','versao_final/assets/imgs/Explosion3_6.png',
                    'versao_final/assets/imgs/Explosion3_7.png','versao_final/assets/imgs/Explosion3_8.png',
                    'versao_final/assets/imgs/Explosion3_9.png','versao_final/assets/imgs/Explosion3_10.png',
                    'versao_final/assets/imgs/Explosion3_11.png',
                ]
            cls._instance.__caminho_imagem_explosao2 = [
                    'versao_final/assets/imgs/tile000.png','versao_final/assets/imgs/tile001.png',
                    'versao_final/assets/imgs/tile002.png','versao_final/assets/imgs/tile003.png',
                    'versao_final/assets/imgs/tile004.png','versao_final/assets/imgs/tile005.png',
                    'versao_final/assets/imgs/tile006.png','versao_final/assets/imgs/tile007.png',
                    'versao_final/assets/imgs/tile008.png','versao_final/assets/imgs/tile009.png',
                    'versao_final/assets/imgs/tile010.png','versao_final/assets/imgs/tile011.png',
                    'versao_final/assets/imgs/tile012.png','versao_final/assets/imgs/tile013.png',
                    'versao_final/assets/imgs/tile014.png','versao_final/assets/imgs/tile015.png',
                    'versao_final/assets/imgs/tile016.png'
            ]
            cls._instance.__caminho_imagem_coracao_cheio = 'versao_final/assets/imgs/coracao_cheio.png'
            cls._instance.__caminho_imagem_barra_score = 'versao_final/assets/imgs/barra_score.png'
            cls._instance.__audio_gameover = 'versao_final/assets/audio/gameover.wav'
            cls._instance.__audio_tiro = 'versao_final/assets/audio/shootjogador.mp3'
            cls._instance.__audio_jogo = 'versao_final/assets/audio/MyVeryOwnDeadShip.ogg'
            cls._instance.__audio_home = 'versao_final/assets/audio/Home.wav'
        return cls._instance

    # Métodos para acessar e modificar caminhos de imagens
    @property
    def audio_home(self):
        return self.__audio_home
    
    @audio_home.setter
    def audio_home(self, audio_home):
        self.__audio_home = audio_home
    
    @property
    def audio_jogo(self):
        return self.__audio_jogo
    
    @audio_jogo.setter
    def audio_jogo(self, audio_jogo):
        self.__audio_jogo = audio_jogo
    
    @property
    def audio_tiro(self):
        return self.__audio_tiro
    
    @audio_tiro.setter
    def audio_tiro(self, audio_tiro):
        self.__audio_tiro = audio_tiro

    @property
    def audio_gameover(self):
        return self.__audio_gameover
    
    @audio_gameover.setter
    def audio_gameover(self, audio_gameover):
        self.__audio_gameover = audio_gameover

    @property
    def caminho_background(self):
        return self.__caminho_background
    
    @caminho_background.setter
    def caminho_background(self, caminho_background):
        self.__caminho_background = caminho_background

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def sprites_jogador(self):
        return self.__sprites_jogador
    
    @sprites_jogador.setter
    def sprites_jogador(self, sprites_jogador):
        self.__sprites_jogador = sprites_jogador

    @property
    def caminho_fonte1(self):
        return self.__caminho_fonte1
    
    @caminho_fonte1.setter
    def caminho_fonte1(self, caminho_fonte1):
        self.__caminho_fonte1 = caminho_fonte1

    @property
    def altura_tela(self):
        return self.__altura_tela
    
    @altura_tela.setter
    def altura_tela(self, altura_tela):
        self.__altura_tela = altura_tela

    @property
    def largura_tela(self):
        return self.__largura_tela
    
    @largura_tela.setter
    def largura_tela(self, largura_tela):
        self.__largura_tela = largura_tela
    
    @property
    def FPS(self):
        return self.__FPS
    
    @FPS.setter
    def FPS(self, FPS):
        self.__FPS = FPS

    @property
    def caminho_imagem_jogador(self):
        return self.__caminho_imagem_jogador
    
    @caminho_imagem_jogador.setter
    def caminho_imagem_jogador(self, caminho):
        self.__caminho_imagem_jogador = caminho

    @property
    def caminho_imagem_explosao1(self):
        return self.__caminho_imagem_explosao1

    @caminho_imagem_explosao1.setter
    def caminho_imagem_explosao1(self, caminho):
        self.__caminho_imagem_explosao1 = caminho

    @property
    def caminho_imagem_explosao2(self):
        return self.__caminho_imagem_explosao2

    @caminho_imagem_explosao2.setter
    def caminho_imagem_explosao2(self, caminho):
        self.__caminho_imagem_explosao2 = caminho

    @property
    def caminho_imagem_coracao_cheio(self):
        return self.__caminho_imagem_coracao_cheio

    @caminho_imagem_coracao_cheio.setter
    def caminho_imagem_coracao_cheio(self, caminho_imagem_coracao_cheio):
        self.__caminho_imagem_coracao_cheio = caminho_imagem_coracao_cheio
    
    @property
    def caminho_imagem_barra_score(self):
        return self.__caminho_imagem_barra_score

    @caminho_imagem_barra_score.setter
    def caminho_imagem_barra_score(self, caminho_imagem_barra_score):
        self.__caminho_imagem_barra_score = caminho_imagem_barra_score
