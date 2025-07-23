import tkinter as tk
from menus import MenuSistema

COR_FUNDO = "#F4EDE3"
COR_VERDE = "#A8D5BA"

menu = MenuSistema()

def criar_tela_pedidos(root, email, mostrar_tela_callback):
    from tkinter import messagebox
    frame_pedidos = tk.Frame(root, bg=COR_FUNDO)

    tk.Label(frame_pedidos, text="Meus Pedidos", font=("Helvetica", 20, "bold"), bg=COR_FUNDO).pack(pady=20)

    pedidos = menu.pedidos.listar_pedidos_do_usuario(email)

    painel = tk.Frame(frame_pedidos, bg=COR_FUNDO)
    painel.pack(expand=True)

    if not pedidos:
        tk.Label(painel, text="Nenhum pedido realizado ainda.", font=("Arial", 12), bg=COR_FUNDO).pack(pady=40)
    else:
        for pedido in pedidos:
            id_animal = pedido["animal_id"]
            tipo = pedido["tipo"]
            animal = menu.animais.buscar_animal_por_id(id_animal, tipo)
            info = f"{animal['nome'].title()} • {animal['especie'].title()} • {animal['idade']} ({tipo})"

            card = tk.Frame(painel, bg=COR_VERDE, padx=10, pady=10)
            card.pack(pady=10, fill="x", padx=50)

            tk.Label(card, text=info, font=("Arial", 12), bg=COR_VERDE).pack(anchor="w")

            def excluir_pedido_local(email=email, aid=id_animal, tipo=tipo):
                if messagebox.askyesno("Confirmação", f"Excluir pedido de {animal['nome'].title()}?"):
                    menu.pedidos.remover_pedido(email, aid, tipo)
                    messagebox.showinfo("Removido", "Pedido excluído com sucesso.")
                    mostrar_tela_callback("pedidos")  # Recarrega a tela

            tk.Button(card, text="Excluir", font=("Arial", 10), bg="#C77D7D", command=excluir_pedido_local).pack(anchor="e", pady=5)

    tk.Button(frame_pedidos, text="Voltar", font=("Arial", 12), bg=COR_VERDE, command=lambda: mostrar_tela_callback("menu")).pack(pady=20)

    return frame_pedidos