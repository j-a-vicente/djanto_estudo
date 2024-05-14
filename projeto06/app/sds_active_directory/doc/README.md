# MODULO SENTINEL ACTIVE DIRECTORY


## Ideias para o dashboard de apresentação do painel do AD.

+ Direcionadas ao cliente __Infraero__
    + criar três bannes um de usuários internos, tercerizados e sedidos, dentro do banner as informações:
        - Total de usuários:
            - Ativos.
            - Desativados.
            - Com a senha vencida mas ativos.
            - Com a senha vencida e bloqueado.
            - Conta bloqueada.
    + Total de contas __ativas__ que estão replicando para nuvem
    + Total de contas __ativas__ que __não__ estão replicando para nuvem.

    + Alerta para os estatus das contas:
        - 2163200: Este código geralmente indica uma conta de usuário desativada. A conta não está habilitada para acesso.
        - 512: Este código indica uma conta de usuário normal sem restrições especiais.
        - 66050: Este código indica uma conta de usuário que possui a opção "Password never expires" (A senha nunca expira) ativada, o que significa que a senha do usuário nunca expirará.
        - 66178: Este código indica uma conta de usuário que está desativada e com a opção "Password never expires" (A senha nunca expira) ativada.
        - 16843264: Este código indica uma conta de usuário que está desativada e com a opção "Password never expires" (A senha nunca expira) ativada. Também pode indicar que a conta requer pré-autenticação Kerberos.
        - 66080: Este código indica uma conta de usuário que está desativada e com a opção "Password never expires" (A senha nunca expira) ativada, e que também requer pré-autenticação Kerberos.
        - 66082: Este código indica uma conta de usuário que está desativada e com a opção "Password never expires" (A senha nunca expira) ativada, e que também requer pré-autenticação Kerberos. Além disso, a conta não é permitida para delegação.
        - 546: Este código indica uma conta de usuário desativada e com a opção "Smartcard required for interactive logon" (Cartão inteligente necessário para logon interativo) ativada.
        - 514: Este código indica uma conta de usuário desativada e com a opção "Not Delegated" (Não Delegado) ativada.
        - 544: Este código indica uma conta de usuário desativada e com a opção "Not Delegated" (Não Delegado) e "Smartcard required for interactive logon" (Cartão inteligente necessário para logon interativo) ativadas.    

    + Panéis de controle:
        + Dashboard para controle de contas que a senha vão expirar nos próximos 60 dias.
            - contas que expiram nos últimos 60 dias e tiveram a sua senha renovada.
            - contas que expiram nos últimos 60 dias e __não__ tiveram a sua senha renovada.
        + Contas desativadas e estão fora da OU __desativada__

    + Alerta para conta do usuário:
        + Total por dia.
            - badPasswordTime: Este atributo registra a data e hora da última tentativa de autenticação mal sucedida (com uma senha incorreta) para a conta de usuário.
 
        + Total de contas que tiveram a senha alterada.
            - pwdLastSet: Este atributo indica a data e hora em que a senha da conta de usuário foi alterada pela última vez. É útil para verificar a idade da senha e determinar se ela está dentro das políticas de segurança.

        + Determinar total de tentativas mal sucedidas de efetuar login na rede. __IMPORTANTE__
            - badPwdCount: Este atributo registra o número de tentativas de autenticação mal sucedidas (com senha incorreta) para a conta de usuário desde a última vez que a senha foi definida ou redefinida.

        + Total de contas bloqueadas no dia:
            - lockoutTime: Este atributo indica a data e hora em que a conta de usuário foi bloqueada devido a várias tentativas de autenticação mal sucedidas. Quando uma conta é bloqueada, ela fica inacessível até que um administrador a desbloqueie.

        + Usuários que não acessam a rede a mais de 60 dias.
            - lastLogonTimestamp: Este atributo armazena o timestamp da última vez que o usuário fez logon em qualquer controlador de domínio do Active Directory na rede. É útil para determinar a última vez que um usuário acessou o sistema.
            - lastLogon: Este atributo armazena o timestamp da última vez que o usuário fez logon em um controlador de domínio específico.

            - accountExpires: Este atributo indica a data e hora em que a conta de usuário no Active Directory expira. Depois desse momento, a conta não poderá mais ser usada para autenticação.       

        + Total de contas criadas por dia:
            - whenCreated: Este atributo armazena a data e hora em que a conta de usuário foi criada no Active Directory. É um timestamp que indica quando a conta foi inicialmente configurada.

        + Total de contas alteradas por dia:
            - whenChanged: Este atributo armazena a data e hora da última vez que a conta de usuário foi modificada no Active Directory. Ele registra a última alteração feita na conta, como alterações de senha, atualizações de informações de contato, etc.