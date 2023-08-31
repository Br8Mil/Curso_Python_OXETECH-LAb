import pyautogui as pg, time

time.sleep(5)

#cadastrar novos usuários

pg.click(967,594, duration=1.0)
pg.click(998,544, duration=1.0)
pg.write("Rodrigo")
pg.click(996,566, duration=1.0)
pg.write("123")
pg.click(917,594, duration=1.0)

#logar no usuário criado

pg.click(1006,543, duration=1.0)
pg.write("Rodrigo")
pg.click(989,569, duration=1.0)
pg.write("123")
pg.click(871,597, duration=1.0)

#ler a lista de produtos e ordenar para o cadastro

with open("produtos.txt", "r") as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        pg.click(712,528, duration=0.5)
        pg.write(produto)
        pg.click(711,557, duration=0.5)
        pg.write(quantidade)
        pg.click(711,581, duration=0.5)
        pg.write(preco)
        pg.click(584,736, duration=0.5)

