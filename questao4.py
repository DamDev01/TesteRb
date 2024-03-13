import random

# Simulando a situação das lâmpadas e interruptores
lampadas = [False, False, False]  # False representa lâmpada desligada
interruptores = [0, 1, 2]

# Escolhendo aleatoriamente uma lâmpada para ligar
lampada_acesa = random.choice(interruptores)
lampadas[lampada_acesa] = True

# Escolhendo outro interruptor aleatoriamente para ligar
outro_interruptor = random.choice([interruptor for interruptor in interruptores if interruptor != lampada_acesa])
lampadas[outro_interruptor] = not lampadas[outro_interruptor]  # Invertendo o estado da lâmpada

# Verificando o estado das lâmpadas
print("Estado das lâmpadas:")
for i, lampada in enumerate(lampadas):
    print(f"Lâmpada {i+1}: {'ligada' if lampada else 'desligada'}")


#Para resolver esse problema, você pode seguir este procedimento:

#Primeiro, ligue um dos interruptores e espere alguns minutos para a lâmpada aquecer.
#Em seguida, desligue este interruptor e ligue outro interruptor.
#Agora, vá até a sala com as lâmpadas.
#A lâmpada que estiver acesa está conectada ao último interruptor que você ligou.
#Toque na lâmpada que está desligada. Se estiver quente, está conectada ao primeiro 
#interruptor que você ligou anteriormente. Se estiver fria, está conectada ao interruptor que você não tocou.