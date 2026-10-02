import subprocess
import time
import psutil
import pygetwindow as gw

class OperaFakturama:
    def __init__(self, caminho_exe=r"D:/Fakturama2/Fakturama.exe"):
        self.caminho_exe = caminho_exe

    def fakturama_execucao(self):
        # Verifica se já existe processo Fakturama
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] and "fakturama" in proc.info['name'].lower():
                print("Fakturama já está aberto!")
                windows = [w for w in gw.getWindowsWithTitle("Fakturama") if w.visible]
                if windows:
                    win = windows[0]
                    win.activate()
                    win.maximize()
                    print("Janela do Fakturama detectada e ativada!")
                    return True
                else:
                    print("Janela do Fakturama não encontrada.")
                    return False
                
        print("Abrindo Fakturama...")
        subprocess.Popen([self.caminho_exe])

        # Espera até a janela aparecer
        for _ in range(30):
            windows = [w for w in gw.getWindowsWithTitle("Fakturama") if w.visible]
            if windows:
                win = windows[0]
                win.activate()
                win.maximize()
                print("Janela do Fakturama detectada e ativada!")
                return True
            time.sleep(1)

        return False

    def fechar_fakturama(self):
        windows = [w for w in gw.getWindowsWithTitle("Fakturama") if w.visible]
        if windows:
            win = windows[0]
            win.close()
            print("Janela do Fakturama fechada com sucesso!")
            return True
        else:
            print("Janela do Fakturama não encontrada.")
            return False
