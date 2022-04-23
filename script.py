#Author: Felipe Lira
#Date: 23/04/2022
#Gostou? Me paga um cafe? rs


def indexPON():
    print('\n\n\n')
    print('SISTEMA PARA VERIFICAR INDEX PORTA PON')
    print('\n')
    slot = input('Informe o SLOT: ')
    pon = input('Informe a PON: ')

 
    if slot == '1':
        slot_binario = '00010'
    
    elif slot == '2':
        slot_binario = '00011'
    
    elif slot == '3':
        slot_binario = '00100'
    
    elif slot == '4':
        slot_binario = '00101'
    
    elif slot == '5':
        slot_binario = '00110'
    
    elif slot == '6':
        slot_binario = '00111'
    
    elif slot == '7':
        slot_binario = '01000'
    
    elif slot == '8':
        slot_binario = '01001'
    
    elif slot == '9':
        slot_binario = '01010'
    
    elif slot == '10':
        slot_binario = '01011'
    
    elif slot == '11':
        slot_binario = '01100'
    
    elif slot == '12':
        slot_binario = '01101'
    
    elif slot == '13':
        slot_binario = '01110'
    
    elif slot == '14':
        slot_binario = '01111'
    
    elif slot == '15':
        slot_binario = '10000'
    
    elif slot == '16':
        slot_binario = '10001'

    
    if pon == '1':
        pon_binario = '00000'
        
    elif pon == '2':
        pon_binario = '00001'
    
    elif pon == '3':
        pon_binario = '00010'
    
    elif pon == '4':
        pon_binario = '00011'
    
    elif pon == '5':
        pon_binario = '00100'
    
    elif pon == '6':
        pon_binario = '00101'
    
    elif pon == '7':
        pon_binario = '00110'
    
    elif pon == '8':
        pon_binario = '00111'
    
    elif pon == '9':
        pon_binario = '01000'
    
    elif pon == '10':
        pon_binario = '01001'
    
    elif pon == '11':
        pon_binario = '01010'
    
    elif pon == '12':
        pon_binario = '01011'
    
    elif pon == '13':
        pon_binario = '01100'
    
    elif pon == '14':
        pon_binario = '01101'
    
    elif pon == '15':
        pon_binario = '01110'

    elif pon == '16':
        pon_binario = '01111'


    resultado_binario = str('00' + slot_binario + '1101' + pon_binario + '0000000000000000')
    resultado_decimal = int ( resultado_binario , 2)

    print('\n')
    print('Resultado')
    print(f'Index Binario:', resultado_binario)
    print(f'Index Decimal:', resultado_decimal)



def indexONU():
    print('\n\n\n')
    print('SISTEMA PARA VERIFICAR INDEX PORTA PON')
    print('\n')

    slot = int (input('Informe o SLOT: '))
    pon = int (input('Informe a PON: '))
    onu = int (input('Informe a posicao da ONU: '))
 
    index_onu = slot*33554432+33554432+pon*65536-65536+onu*512-512+29360128

    print('\n')
    print('Resultado')
    print(index_onu)


def menuprinc():


    opcao=int(input('''

SISTEMA PARA VERIFICAR INDEX SNMP OLT NOKIA
   
Felipe Lira | 2022
=========================================
||    	  Escolha um programa          ||
|| 1 - Index PON                       ||
|| 2 - Index ONU                       ||
|| 0 - Fechar Menu                     ||
=========================================
Escolha: '''))


   
    if opcao == 1:
        indexPON()
    elif opcao == 2:
        indexONU()
    elif opcao == 0:
        exit()
    else:
        print("Este número não está nas alternativas, tente novamente :D.\n")
        menuprinc()
while True:
    try:
        menuprinc()    
    except ValueError:
        print("Isso não é um número, tente novamente :D.\n")
