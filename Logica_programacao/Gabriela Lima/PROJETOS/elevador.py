# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem
#  a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as
#  ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

# 1° - Garantir que o elevador esteja no andar solicitado;
# 2° - Garantir que todas as pessoas tenham entrado em segurança dentro do elevador;
# 3° - O elevador deve ir até o andar do botão acionado;

# print("====Elevador Python!====")

# andar_atual = 0
# while True:
#          try:
#             destino   = int(input("Para qual andar iremos? \n"))
#             if andar_atual < 0 or destino > 10:
#               print(f"Saindo {andar_atual}, indo para {destino}")
#               andar_atual = destino 
#               if input("Deseja escolher outro andar? (s/n): \n").lower() != 's':
#                    print("Obrigado por usar o ==== Elevador Python! ===== Até a próxima!")
#                    break
# for listagem in range(10):
#       print(f"Andar {listagem} - {'[X]' if listagem == andar_atual else '[ ]'} ")
#      except ValueError:
# print(f"Ocorreu um erro inesperado")
# print("Sistema desligado")



