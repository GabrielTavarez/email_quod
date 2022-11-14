def get_texto_CIP(nome, cnpj, member_id):
    texto = f"""
Olá,
Solicito a criação dos dados da fonte no MBS, Orbit e R3, tanto em Dev quanto em Prod.
        
Razão social: {nome}
CNPJ: {cnpj}
Tipo:  Fonte CIP
                
        
Orbit (Datasets):
        
    • ACPO107 - Name: {nome} - Part ACPO107 | {nome} - Full ACPO107
        Member Id:{member_id}P |{member_id}F
            File Source Id: G
        
        
    • ACPO109 - Name: {nome} - Part ACPO109 | {nome} - Full ACPO109
        Member Id:{member_id}P |{member_id}F
            File Source Id: I
        
               
                        
    • ACPO111 - Name: {nome} - Part ACPO111 | {nome} - Full ACPO111
        Member id:{member_id}P |{member_id}F
            File Source Id: K
        
                        
                        
    • ACPO112 - Name: {nome} - Part ACPO112 | {nome} - Full ACPO112
        Member Id:{member_id}P |{member_id}F
            File Source Id: L
        
                        
                        
    • ACPO129 - Name: {nome} - Part ACPO129 | {nome} - Full ACPO129
        Member Id:{member_id}P |{member_id}F
            File Source Id: Z
        
                            
                        
Orbit (Builds):
        
    • {member_id}FG000000000001 - Description: {nome} - Scrub Build of ACPO107
        Components: {member_id}FG
            Build Type Name: No Sequence
            
    • {member_id}FG-Linker - Description: {nome} - Linker of ACPO107 Full and Part files
        Components: {member_id}PG, {member_id}FG
            Build Type Name: Linker
                        
    • {member_id}FI-Linker - Description: {nome} - Linker of ACPO109 Full and Part files
        Components: {member_id}PI, {member_id}FI
            Build Type Name: Linker
                        
    • {member_id}FK-Linker - Description: {nome} - Linker of ACPO111 Full and Part files
        Components: {member_id}PK, {member_id}FK
            Build Type Name: Linker
                        
    • {member_id}FK000000000001 - Description: {nome} - Scrub Build of ACPO111
        Components: {member_id}FK
            Build Type Name: No Sequence
                        
    • {member_id}FL-Linker - Description: {nome} - Linker of ACPO112 Full and Part files
        Components: {member_id}PL, {member_id}FL
            Build Type Name: Linker
                        
    • {member_id}FZ-Linker - Description: {nome} - Linker of ACPO129 Full and Part files
        Components: {member_id}PZ, {member_id}FZ
            Build Type Name: Linker
                        
    • {member_id}FZ000000000001 - Description: {nome} - Scrub Build of ACPO129
        Components: {member_id}FZ
            Build Type Name: No Sequence
                        
LZs necessárias no R3 PROD:
                        
    • ACPO107 - Member Id: {member_id}PG
        Pickup: /data/Sterling/cd_cip_prod
            Output: /data/banks/acpo/incoming
                        
    • ACPO109 - Member Id: {member_id}PI
        (Mesmos subdiretórios)
                        
    • ACPO111 - Member Id: {member_id}PK
        (Mesmos subdiretórios)
                        
    • ACPO129 - Member Id: {member_id}PZ
        (Mesmos subdiretórios)

Att,        
"""
    return texto

def get_texto_Utilities(nome, cnpj, member_id):
    texto = """
Olá,
Solicito a criação dos dados da fonte no MBS, Orbit e R3, tanto em Dev quanto em Prod.

Razão social: {nome}
CNPJ: {cnpj}
Tipo:  Fonte Direta
                
        
Orbit (Datasets):
        
    • ACPO107 - Name: {nome} – Part ACPO107 | {nome} – Full ACPO107
        Member Id:{member_id}P |{member_id}F
            File Source Id: G
        
        
    • ACPO108 - Name: {nome} – Part ACPO108 | {nome} – Full ACPO108
        Member Id:{member_id}P |{member_id}F
            File Source Id: H
        
        
    • ACPO109 - Name: {nome} – Part ACPO109 | {nome} – Full ACPO109
        Member Id:{member_id}P |{member_id}F
            File Source Id: I
        
        
    • ACPO110 - Name: {nome} – Part ACPO110 | {nome} – Full ACPO110
        Member Id:{member_id}P |{member_id}F
            File Source Id: J
        
                        
                        
    • ACPO111 - Name: {nome} – Part ACPO111 | {nome} – Full ACPO111
        Member id:{member_id}P |{member_id}F
            File Source Id: K
        
                        
                        
    • ACPO112 - Name: {nome} – Part ACPO112 | {nome} – Full ACPO112
        Member Id:{member_id}P |{member_id}F
            File Source Id: L
        
                            
                        
Orbit (Builds):
        
    •{member_id}FG000000000001 – Description: {nome} – Scrub Build of ACPO107
        Components:{member_id}FG
            Build Type Name: No Sequence
                        
                        
                        
    •{member_id}FG-Linker – Description: {nome} – Linker of ACPO107 and ACPO108 Full and Part files
        Components:{member_id}PG,{member_id}FG,{member_id}PH,{member_id}FH
            Build Type Name: Linker
        
                        
                        
    •{member_id}FI-Linker – Description: {nome} – Linker of ACPO109 and ACPO110 Full and Part files
        Components:{member_id}PI,{member_id}FI,{member_id}PJ,{member_id}FJ
            Build Type Name: Linker
        
                        
                        
    •{member_id}FK-Linker – Description: {nome} – Linker of ACPO111 and ACPO112 Full and Part files
        Components:{member_id}PK,{member_id}FK,{member_id}PL,{member_id}FL
            Build Type Name: Linker
        
                        
                        
    •{member_id}FK000000000001 – Description: {nome} – Scrub Build of ACPO111
        Components:{member_id}FK
            Build Type Name: No Sequence
                        
                        
                   
                    
LZs necessárias no R3 PROD:
        
    • ACPO107 – Member Id:{member_id}PG
        Pickup: /data/files/nubank/cpp/upload
            Output: /data/banks/acpo/incoming
        
        
    • ACPO108 – Member Id:{member_id}PH
        Pickup: /data/banks/acpo/outgoing
            Output: /data/files/to_rename
                  
              
    • ACPO109 – Member Id:{member_id}PI
        (Mesmos subdiretórios)
        
        
    • ACPO110 – Member Id:{member_id}PJ
        Pickup: /data/banks/acpo/outgoing
            Output: /data/files/to_rename
                
                
    • ACPO111 – Member Id:{member_id}PK
        (Mesmos subdiretórios)
        
                
    • ACPO112 – Member Id:{member_id}PL
        Pickup: /data/banks/acpo/outgoing
            Output: /data/files/to_rename

Att,
"""
    return texto

def get_texto_direta(nome, cnpj, member_id):
    texto = """
Razão social: {nome}
CNPJ: {cnpj}
Tipo:  Fonte Direta
                
        
Orbit (Datasets):
        
    • ACPO107 - Name: {nome} – Part ACPO107 | {nome} – Full ACPO107
        Member Id:{member_id}P |{member_id}F
            File Source Id: G
        
        
    • ACPO108 - Name: {nome} – Part ACPO108 | {nome} – Full ACPO108
        Member Id:{member_id}P |{member_id}F
            File Source Id: H
        
        
    • ACPO109 - Name: {nome} – Part ACPO109 | {nome} – Full ACPO109
        Member Id:{member_id}P |{member_id}F
            File Source Id: I
        
        
    • ACPO110 - Name: {nome} – Part ACPO110 | {nome} – Full ACPO110
        Member Id:{member_id}P |{member_id}F
            File Source Id: J
        
                        
                        
    • ACPO111 - Name: {nome} – Part ACPO111 | {nome} – Full ACPO111
        Member id:{member_id}P |{member_id}F
            File Source Id: K
        
                        
                        
    • ACPO112 - Name: {nome} – Part ACPO112 | {nome} – Full ACPO112
        Member Id:{member_id}P |{member_id}F
            File Source Id: L
        
                            
                        
Orbit (Builds):
        
    •{member_id}FG000000000001 – Description: {nome} – Scrub Build of ACPO107
        Components:{member_id}FG
            Build Type Name: No Sequence
                        
                        
                        
    •{member_id}FG-Linker – Description: {nome} – Linker of ACPO107 and ACPO108 Full and Part files
        Components:{member_id}PG,{member_id}FG,{member_id}PH,{member_id}FH
            Build Type Name: Linker
        
                        
                        
    •{member_id}FI-Linker – Description: {nome} – Linker of ACPO109 and ACPO110 Full and Part files
        Components:{member_id}PI,{member_id}FI,{member_id}PJ,{member_id}FJ
            Build Type Name: Linker
        
                        
                        
    •{member_id}FK-Linker – Description: {nome} – Linker of ACPO111 and ACPO112 Full and Part files
        Components:{member_id}PK,{member_id}FK,{member_id}PL,{member_id}FL
            Build Type Name: Linker
        
                        
                        
    •{member_id}FK000000000001 – Description: {nome} – Scrub Build of ACPO111
        Components:{member_id}FK
            Build Type Name: No Sequence
                        
                        
                   
                    
LZs necessárias no R3 PROD:
        
    • ACPO107 – Member Id:{member_id}PG
        Pickup: /data/files/nubank/cpp/upload
            Output: /data/banks/acpo/incoming
        
        
    • ACPO108 – Member Id:{member_id}PH
        Pickup: /data/banks/acpo/outgoing
            Output: /data/files/to_rename
                  
              
    • ACPO109 – Member Id:{member_id}PI
        (Mesmos subdiretórios)
        
        
    • ACPO110 – Member Id:{member_id}PJ
        Pickup: /data/banks/acpo/outgoing
            Output: /data/files/to_rename
                
                
    • ACPO111 – Member Id:{member_id}PK
        (Mesmos subdiretórios)
        
                
    • ACPO112 – Member Id:{member_id}PL
        Pickup: /data/banks/acpo/outgoing
            Output: /data/files/to_rename
"""
    return texto



def get_body(nome, cnpj, member_id, tipo):
    if tipo == 'Fonte CIP':
        return get_texto_CIP(nome, cnpj, member_id)
    if tipo == 'Fonte Direta':
        return get_texto_CIP(nome, cnpj, member_id)
    if tipo == 'Fonte Utilities':
        return get_texto_CIP(nome, cnpj, member_id)
    