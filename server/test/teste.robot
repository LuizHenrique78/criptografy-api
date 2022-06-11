***Settings***

Library     ../libs/Encript.py
***Variables***

${o_que_vou_encriptar}=         Testando 
***Test Cases***    

Criar key e encriptar
    ${key}=     gerar_key

    #---> encriptar <---#

    ${encripted}=       encrypt     ${key}      ${o_que_vou_encriptar}

    Log to console        ${encripted}
    Log to console      ${key}



    #---> encriptar <---#

    ${desencript}       decrypts            ${key}      ${encripted}

    Log to console              ${desencript} 

    #---> Validacão <---#

    Should be Equal               ${desencript}         ${o_que_vou_encriptar}

