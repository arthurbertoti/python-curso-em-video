times = ('São Paulo', 'Atlético MG', 'Internacional', 'Flamengo', 'Palmeiras', 'Grêmio',
         'Fluminesne', 'Santos', 'Corinthians', 'Athletico PR', 'Ceará SC', 'Atlético GO',
         'Bragantino', 'Sport Recife', 'Bahia', 'Vasco da Gama', 'Fortaleza', 'Coritiba', 'Goiás', 'Botafogo')
print(f'Os 5 primeiros colocados no Brasileirão são: {times[0:6]}', end=f'\n{20*"-="}\n')
print(f'Os últimos 4 colocados da tabela são: {times[16:]}', end= f'\n{20*"-="}\n')
print(f'Todos os times, em ordem alfabética, que estão disputando o campeonato são: {sorted(times)}', end=f'\n{20*"-="}\n')
print(f'O time Internacional está na {times.index("Internacional")+1}ª posição.')