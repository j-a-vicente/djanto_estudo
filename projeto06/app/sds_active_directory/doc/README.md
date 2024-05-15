# Modulo Senteinel Active Directory


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
        Preciso do nome do grupo que é responsavel por replicar os usuários para nuvem.

    + Total de contas __ativas__ que __não__ estão replicando para nuvem.
        quem estiver fora do grupo não replica.

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
        - 66048: a conta é uma conta de computador habilitada para logon, com uma senha que expira e que permite delegação de credenciais.

    + Panéis de controle: (st_hist_account_user)
        + Dashboard para controle de contas que a senha vão expirar nos próximos 60 dias.
            
            - Contas que expiram nos últimos 60 dias e tiveram a sua senha renovada __antes__ da conta ficar bloqueada. 
                * __accountExpires__ usado como variável do 60 dias, ou seja hoje menos 60 dias.
                * __pwdLastSet__ a troca da senha tem que ser __menor__ que a data de bloqueio __accountExpires__, Este valor é depois da alteração.                    
                * __useraccountcontrol__ a conta __DEVER__ está ativa.

            - Contas que expiram nos últimos 60 dias e tiveram a sua senha renovada __depois__ da conta ficar bloqueada.
                * __accountExpires__ usado como variável do 60 dias, ou seja hoje menos 60 dias.
                * __pwdLastSet__ a troca da senha tem que ser __maior__ que a data de bloqueio __accountExpires__, 
                * __useraccountcontrol__ a conta __DEVER__ está ativa.

            - Contas que expiram nos últimos 60 dias e __não__ tiveram a sua senha renovada ou seja aconta está bloqueada para login.
                * __accountExpires__ usado como variável do 60 dias, ou seja hoje menos 60 dias.
                * __pwdLastSet__ a troca da senha tem que ser __maior__ que a data de bloqueio __accountExpires__
                * __useraccountcontrol__ a conta __DEVER__ está Desativada.        


        + Contas desativadas e estão fora da OU __desativada__

    + Alerta para conta do usuário: (st_alert_user)
        
        + Total por dia.
            - __badPasswordTime__: Este atributo registra a data e hora da última tentativa de autenticação __mal__ sucedida (com uma senha incorreta) para a conta de usuário.
 
        + Total de contas que tiveram a senha alterada.
            - __pwdLastSet__: Este atributo indica a data e hora em que a senha da conta de usuário foi alterada pela última vez. É útil para verificar a idade da senha e determinar se ela está dentro das políticas de segurança.

        + Determinar total de tentativas mal sucedidas de efetuar login na rede. __IMPORTANTE__
            - __badPwdCount__: Este atributo registra o número de tentativas de autenticação mal sucedidas (com senha incorreta) para a conta de usuário desde a última vez que a senha foi definida ou redefinida.

        + Total de contas bloqueadas no dia:
            - __lockoutTime__: Este atributo indica a data e hora em que a conta de usuário foi bloqueada devido a várias tentativas de autenticação mal sucedidas. Quando uma conta é bloqueada, ela fica inacessível até que um administrador a desbloqueie.

        + Usuários que não acessam a rede a mais de 60 dias.
            - __lastLogonTimestamp__: Este atributo armazena o timestamp da última vez que o usuário fez logon em qualquer controlador de domínio do Active Directory na rede. É útil para determinar a última vez que um usuário acessou o sistema.
            - __lastLogon__: Este atributo armazena o timestamp da última vez que o usuário fez logon em um controlador de domínio específico.

            - __accountExpires__: Este atributo indica a data e hora em que a conta de usuário no Active Directory expira. Depois desse momento, a conta não poderá mais ser usada para autenticação.       

        + Total de contas criadas por dia:
            - __whenCreated__: Este atributo armazena a data e hora em que a conta de usuário foi criada no Active Directory. É um timestamp que indica quando a conta foi inicialmente configurada.

        + Total de contas alteradas por dia:
            - __whenChanged__: Este atributo armazena a data e hora da última vez que a conta de usuário foi modificada no Active Directory. Ele registra a última alteração feita na conta, como alterações de senha, atualizações de informações de contato, etc.