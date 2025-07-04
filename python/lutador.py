class Lutador:
    def __init__(self, identificador, cor, socos=0, irregular=0, coordenadas=None, box=None, roi_cabeca=None,
                 roi_tronco=None,
                 roi_linha_cintura=None, roi_mao_esquerda=None, roi_mao_direita=None, nose=None, left_eye=None,
                 right_eye=None, left_ear=None, right_ear=None, left_shoulder=None, right_shoulder=None,
                 left_elbow=None, right_elbow=None, left_wrist=None, right_wrist=None, left_hip=None,
                 right_hip=None, left_knee=None, right_knee=None, left_ankle=None, right_ankle=None, distancia=None):
        # 'identificador' diferencia os lutadores.
        self.identificador = identificador
        self.cor = cor

        self.primeira_execucao = 0

        # 'socos' guarda o número de socos de cada lutador.
        self.socos = socos

        self.irregular = irregular

        self.coordenadas = coordenadas

        self.box = box

        # COORDENADAS DE ROIS DO LUTADOR

        self.roi_cabeca = roi_cabeca
        self.roi_tronco = roi_tronco
        self.roi_linha_cintura = roi_linha_cintura
        self.roi_mao_esquerda = roi_mao_esquerda
        self.roi_mao_direita = roi_mao_direita

        # VALORES BOOLEANOS DE VERIFICACAO DE GOLPE

        self.roi_mao_direitaCabeca = False
        self.roi_mao_esquerdaCabeca = False

        self.roi_mao_direitaTronco = False
        self.roi_mao_esquerdaTronco = False

        self.golpe_irregularEsquerda = False
        self.golpe_irregularDireita = False

        self.distancia = distancia

        # COORDENADAS DE CADA KEYPOINT DO LUTADOR

        self.nose = nose  # Nariz
        self.left_eye = left_eye  # Olho esquerdo
        self.right_eye = right_eye  # Olho direito
        self.left_ear = left_ear  # Orelha esquerda
        self.right_ear = right_ear  # Orelha direita
        self.left_shoulder = left_shoulder  # Ombro esquerdo
        self.right_shoulder = right_shoulder  # Ombro direito
        self.left_elbow = left_elbow  # Cotovelo esquerdo
        self.right_elbow = right_elbow  # Cotovelo direito
        self.left_wrist = left_wrist  # Pulso esquerdo
        self.right_wrist = right_wrist  # Pulso direito
        self.left_hip = left_hip  # Quadril esquerdo
        self.right_hip = right_hip  # Quadril direito
        self.left_knee = left_knee  # Joelho esquerdo
        self.right_knee = right_knee  # Joelho direito
        self.left_ankle = left_ankle  # Tornozelo esquerdo
        self.right_ankle = right_ankle  # Tornozelo direito

    def soco(self, parte: str):
        self.socos += 1

    def falta(self):
        self.irregular += 1

    def __str__(self):
        return f"Lutador {self.identificador}: {self.socos} socos, {self.coordenadas}, {self.box}"
