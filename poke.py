
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence 
import os
import sys

def obter_diretorio_executavel():
    """Retorna o caminho da pasta onde o .exe (ou o .py) está localizado"""
    if getattr(sys, 'frozen', False):
        # Se for um executável compilado pelo PyInstaller
        return os.path.dirname(sys.executable)
    else:
        # Se estiver a rodar como script .py normal
        return os.path.dirname(os.path.abspath(__file__))

class MascoteDinamico:
    def __init__(self, root, nome_imagem):
        self.root = root
        
        # Configurações de Janela
        self.root.overrideredirect(True) 
        self.root.wm_attributes('-topmost', False) 
        
        self.transparent_color = '#00FF00' 
        self.root.wm_attributes('-transparentcolor', self.transparent_color)
        self.root.configure(bg=self.transparent_color)

        # Localiza o ficheiro na pasta do executável
        diretorio = obter_diretorio_executavel()
        caminho_gif = os.path.join(diretorio, nome_imagem)

        if not os.path.exists(caminho_gif):
            # Se não encontrar o mascote.gif, mostra um aviso na tela
            self.label = tk.Label(root, text=f"Ficheiro '{nome_imagem}'\nnão encontrado na pasta!", 
                                 fg='black', bg='white', padx=10, pady=10)
            self.label.pack()
            self.label.bind("<Button-3>", lambda e: self.root.destroy()) # Botão direito para fechar
            return

        # Carregar e Redimensionar
        pil_image = Image.open(caminho_gif)
        tamanho_maximo = (300, 300) 
        
        self.frames = []
        for frame in ImageSequence.Iterator(pil_image):
            temp_frame = frame.copy()
            temp_frame.thumbnail(tamanho_maximo, Image.Resampling.LANCZOS)
            self.frames.append(ImageTk.PhotoImage(temp_frame))

        self.frame_atual = 0
        self.label = tk.Label(root, bg=self.transparent_color, bd=0)
        self.label.pack()

        # Inicia a posição e as animações
        self.x = self.root.winfo_screenwidth() 
        self.y = self.root.winfo_screenheight() - 350
        self.is_dragging = False

        self.animar_gif()
        self.voar_pela_tela() 

        # Eventos de Mouse
        self.label.bind("<ButtonPress-1>", self.iniciar_arraste)
        self.label.bind("<B1-Motion>", self.mover_janela)
        self.label.bind("<ButtonRelease-1>", self.parar_arraste)
        self.label.bind("<Button-3>", lambda e: self.root.destroy()) 

    def animar_gif(self):
        self.frame_atual = (self.frame_atual + 1) % len(self.frames)
        self.label.configure(image=self.frames[self.frame_atual])
        self.root.after(80, self.animar_gif) 

    def voar_pela_tela(self):
        if not self.is_dragging:
            self.x -= 2 
            if self.x < -300:
                self.x = self.root.winfo_screenwidth() 
            self.root.geometry(f"+{self.x}+{self.y}")
        self.root.after(30, self.voar_pela_tela)

    def iniciar_arraste(self, event):
        self.is_dragging = True 
        self.x_offset = event.x
        self.y_offset = event.y

    def mover_janela(self, event):
        self.x = event.x_root - self.x_offset
        self.y = event.y_root - self.y_offset
        self.root.geometry(f"+{self.x}+{self.y}")
        
    def parar_arraste(self, event):
        self.is_dragging = False 

if __name__ == '__main__':
    root = tk.Tk()
    # O programa agora procura sempre por este nome fixo na pasta
    app = MascoteDinamico(root, 'mascote.gif')
    root.mainloop()
