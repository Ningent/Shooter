from cProfile import label
import pygame
from PIL import Image, ImageTk
from customtkinter import *
import game

print("grafic.py")
fenetre_width = 1080
fenetre_height = 720

class Grafic:
    def __init__(self, game=None):
        self.game = game

    def oki(self, tuntun):
        tuntun.destroy()
        self.menu()

    def aaa(self, tkt):
        tkt.configure(text="press 'r' to regenerate your life")

    def fofo(self, surface):
        surface.destroy()

        with open("conection.txt", "r") as ci:
            cii = ci.readline().strip()
            cii = int(cii)
        with open("conection.txt", "w") as co:
            co.write(str(cii + 1))
        with open("bonbon.txt", "w") as bob_w:
            bob_w.write("False")

        cheh = CTk()

        cheh_width = 1500
        cheh_height = 800
        cheh.title("advice")
        cheh.geometry(f"{cheh_width}x{cheh_height}")
        cheh.maxsize(cheh_width, cheh_height)
        cheh.minsize(cheh_width, cheh_height)

        bbb = CTkFrame(master=cheh, bg_color="transparent")

        # Définir ccc avant de l'utiliser
        ccc = CTkLabel(master=bbb, text="", text_color='white')
        ccc.pack()

        consel = CTkButton(master=bbb, text="Transforms the candy into advice",
                           text_color="white", fg_color="#e12fd1",
                           hover_color="#d01489", command=lambda: self.aaa(ccc))
        consel.pack()

        ok = CTkButton(master=bbb, text="ok",
                       text_color="white", fg_color="transparent",
                       hover_color="#d01489", command=lambda: self.oki(cheh))
        ok.pack()

        bbb.pack(expand=YES)

        cheh.mainloop()

    def intro(self):
        with open("bonbon.txt", "r") as bob_r:
            line = bob_r.readline().strip()

        if line == "True":
            chef = CTk()

            chef_width = 1500
            chef_height = 800
            chef.title("bobon")
            chef.geometry(f"{chef_width}x{chef_height}")
            chef.maxsize(chef_width, chef_height)
            chef.minsize(chef_width, chef_height)

            bg = Image.open("image/bg_bonbon.png")
            bg = bg.resize((chef_width + 200, chef_height + 300))
            bg = ImageTk.PhotoImage(bg)
            bg_lb = CTkLabel(master=chef, image=bg, text="")
            bg_lb.place(x=0, y=0)

            frame = CTkFrame(master=chef, bg_color="transparent")

            bt = CTkButton(master=frame, text="Do you want a candy?",
                           text_color="white", fg_color="#e12fd1",
                           hover_color="#d01489", command=lambda: self.fofo(chef))
            bt.pack()

            frame.pack(expand=YES)

            chef.mainloop()

    def mort(self):
        pygame.quit()
        fenetre = CTk()
        fenetre.geometry(f"{fenetre_width}x{fenetre_height}")
        fenetre.maxsize(fenetre_width, fenetre_height)
        fenetre.minsize(fenetre_width, fenetre_height)

        bg_image = Image.open("image/sky.png")
        bg_image = bg_image.resize((1500, 1000))
        bg_image = ImageTk.PhotoImage(bg_image)

        bg_label = CTkLabel(master=fenetre, image=bg_image, text="")
        bg_label.place(relx=0.5, rely=0.5, anchor="center")

        mort_lb = CTkButton(master=fenetre, text="Game over", corner_radius=45, hover_color="#000000",
                            fg_color="#000000", text_color="#ab1e1e", border_color="#ab1e1e",
                            border_width=5, font=("Arial", 50))
        mort_lb.place(x=400, y=120)

        restart = CTkButton(master=fenetre, text="Restart",
                            fg_color="#999999", text_color="#ab1e1e",
                            hover_color="#c1c0c0", command=lambda: self.restart_game(fenetre))
        restart.place(x=50, y=350)

        loby = CTkButton(master=fenetre, text="Loby",
                         fg_color="#999999", text_color="#ab1e1e",
                         hover_color="#c1c0c0", command=lambda: self.loby_menu(fenetre))
        loby.place(x=500, y=350)

        mort_quit = CTkButton(master=fenetre, text="Exit",
                              fg_color="#999999", text_color="#ab1e1e",
                              hover_color="#c1c0c0", command=fenetre.destroy)
        mort_quit.place(x=800, y=350)

        fenetre.mainloop()

    def restart_game(self, fenetre):
        fenetre.destroy()
        pygame.quit()
        new_game = game.Game()  # Crée une nouvelle instance de Game
        new_game.reinstall(new_game.player)
        import main
        main.main()

    def loby_menu(self, fenetre):
        fenetre.destroy()
        self.menu()

    def pygame_start(self, mono):
        print("Starting game...")
        mono.destroy()
        pygame.quit()
        pygame.init()
        import main
        main.main()

    def menu(self):
        mono = CTk()

        mono.geometry(f"{fenetre_width}x{fenetre_height}")
        mono.maxsize(fenetre_width, fenetre_height)
        mono.minsize(fenetre_width, fenetre_height)

        bg_menu = Image.open("image/bg_menu.png")
        bg_menu = bg_menu.resize((1500, 1000))
        bg_menu = ImageTk.PhotoImage(bg_menu)
        bg_menu_lb = CTkLabel(master=mono, text="", image=bg_menu)
        bg_menu_lb.place(relx=0.5, rely=0.5, anchor="center")

        logo_menu = Image.open("image/logo.png")
        logo_menu = logo_menu.resize((250, 250))
        logo_menu = ImageTk.PhotoImage(logo_menu)
        logo_menu_lb = CTkLabel(master=mono, text="", image=logo_menu)
        logo_menu_lb.place(x=440, y=100)

        quit_menu = CTkButton(
            master=mono, text="Play", text_color="white",
            corner_radius=32, hover_color="black", fg_color="#8e8537",
            font=("Arial", 45), border_width=5, border_color="#c8bd58",
            image=CTkImage(dark_image=Image.open("image/sword.png")),
            command=lambda: self.pygame_start(mono)
        )
        quit_menu.place(x=fenetre_width / 2 - 80, y=420)

        off_menu = CTkButton(
            master=mono, text="Exit", text_color="white",
            corner_radius=32, hover_color="black", fg_color="#8e8537",
            font=("Arial", 45), border_width=5, border_color="#c8bd58",
            command=lambda: mono.destroy()
        )
        off_menu.place(x=fenetre_width / 2 - 80, y=550)

        mono.mainloop()
