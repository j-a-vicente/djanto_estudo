https://learn.microsoft.com/pt-br/troubleshoot/windows-server/active-directory/useraccountcontrol-manipulate-account-properties
https://learn.microsoft.com/pt-br/troubleshoot/windows-server/active-directory/useraccountcontrol-manipulate-account-properties#property-flag-descriptions
https://woshub.com/decoding-ad-useraccountcontrol-value/
https://4sysops.com/archives/useraccountcontrol-attribute-checking-and-configuring-security-settings-for-active-directory-accounts/

select to_hex(66050);
select 512::bit(32),514::bit(32),66050::bit(32);




SELECT samaccountname,
    cast(userAccountControl as integer),
    public.decimal_to_binary(cast(userAccountControl as integer)) AS binary_representation,
	CASE WHEN (userAccountControl ) = 512 THEN 'Habilitada para logon' ELSE 'Desabilitada para logon' END AS logon_status,
    CASE WHEN (userAccountControl & 2) = 2 THEN 'Senha não requerida' ELSE 'Senha requerida' END AS password_required,
    CASE WHEN (userAccountControl & 8) = 8 THEN 'Permite redefinição de senha pelo administrador' ELSE 'Não permite redefinição de senha pelo administrador' END AS allow_admin_password_reset,
    CASE WHEN (userAccountControl & 16) = 16 THEN 'Usa criptografia de senha forte' ELSE 'Não usa criptografia de senha forte' END AS strong_password,
    CASE WHEN (userAccountControl & 32) = 32 THEN 'Senha nunca expira' ELSE 'Senha expira conforme política do domínio' END AS password_expires,
    CASE WHEN (userAccountControl & 64) = 64 THEN 'Requer criptografia Kerberos para autenticação' ELSE 'Não requer criptografia Kerberos para autenticação' END AS kerberos_authentication_required,
    CASE WHEN (userAccountControl & 128) = 128 THEN 'Permite delegação de credenciais' ELSE 'Não permite delegação de credenciais' END AS delegation_permission,
    CASE WHEN (userAccountControl & 256) = 256 THEN 'Conta bloqueada' ELSE 'Conta não bloqueada' END AS account_lockout,
    CASE WHEN (userAccountControl & 512) = 512 THEN 'Conta de usuário' ELSE 'Conta de computador' END AS account_type,
    CASE WHEN (userAccountControl & 1024) = 1024 THEN 'Conta não expira' ELSE 'Conta expira' END AS account_never_expires,
    CASE WHEN (userAccountControl & 2048) = 2048 THEN 'Conta confiável para delegação' ELSE 'Conta não confiável para delegação' END AS trusted_for_delegation
FROM public.ad_user;


select 512::bit(32),514::bit(32),66048::bit(32);


SELECT useraccountcontrol
	 , count(useraccountcontrol)
	 , CASE
	     WHEN useraccountcontrol IN(512,66050,66048) THEN 'Ativa'
		 WHEN useraccountcontrol IN(2163200,66178,16843264,66080,66082,546,514,544) THEN 'Desativada'
	  END
FROM public.ad_user
GROUP BY useraccountcontrol



-- 

CREATE SEQUENCE IF NOT EXISTS public.st_alert_user_id_st_alert_user_seg
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.st_alert_user_id_st_alert_user_seg
    OWNER TO "Sentinel";


CREATE TABLE IF NOT EXISTS public.st_alert_user
(
    id_st_alert_user integer NOT NULL,
    useraccountcontrol bigint,
    whencreated integer,
    whenchanged integer,
    accountexpires integer,
    badpasswordtime integer,
    pwdlastset integer,
    lastlogontimestamp integer,
    lastlogon integer,
    badpwdcount integer,
    lockouttime integer,
    dhcriacao timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT st_alert_user_id_st_alert_user PRIMARY KEY (id_st_alert_user)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.st_alert_user
    OWNER to "Sentinel";	


CREATE SEQUENCE IF NOT EXISTS public.st_hist_account_user_id_st_hist_account_user_seg
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.st_hist_account_user_id_st_hist_account_user_seg
    OWNER TO "Sentinel";

CREATE TABLE IF NOT EXISTS public.st_hist_account_user
(
    id_st_hist_account_user integer NOT NULL DEFAULT nextval('st_hist_account_user_id_st_hist_account_user_seg'::regclass),
	samaccountname text COLLATE pg_catalog."default" NOT NULL,
    whencreated timestamp without time zone,
    whenchanged timestamp without time zone,
    accountexpires timestamp without time zone,
    badpasswordtime timestamp without time zone,
    pwdlastset timestamp without time zone,
    lastlogontimestamp timestamp without time zone,
    lastlogon timestamp without time zone,
    badpwdcount bigint,
    lockouttime bigint,
    dhcriacao timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT st_hist_account_user_id_st_hist_account_user PRIMARY KEY (id_st_hist_account_user)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.st_hist_account_user OWNER to "Sentinel";



-- Retora no numero referente ao dia.
-- Alerta para conta do usuário: (st_alert_user)
SELECT samaccountname
	 , CASE 
	     WHEN whencreated >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  whencreated <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "whencreated"	
	 , CASE 
	     WHEN whenchanged >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  whenchanged <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "whenchanged"	
	 , CASE 
	     WHEN accountexpires >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  accountexpires <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "accountexpires"	
	 , CASE 
	     WHEN badpasswordtime >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  badpasswordtime <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "badpasswordtime"	
	 , CASE 
	     WHEN pwdlastset >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  pwdlastset <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "pwdlastset"	
	 , CASE 
	     WHEN lastlogontimestamp >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  lastlogontimestamp <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "lastlogontimestamp"	
	 , CASE 
	     WHEN lastlogon >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  lastlogon <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "lastlogon"	
	, badpwdcount, lockouttime, useraccountcontrol
FROM stage.ad_user;


SELECT samaccountname
	 , CASE 
	     WHEN whencreated >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  whencreated <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "whencreated"	
	 , CASE 
	     WHEN whenchanged >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  whenchanged <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "whenchanged"	
	 , CASE 
	     WHEN accountexpires >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  accountexpires <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "accountexpires"	
	 , CASE 
	     WHEN badpasswordtime >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  badpasswordtime <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "badpasswordtime"	
	 , CASE 
	     WHEN pwdlastset >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  pwdlastset <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "pwdlastset"	
	 , CASE 
	     WHEN lastlogontimestamp >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  lastlogontimestamp <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "lastlogontimestamp"	
	 , CASE 
	     WHEN lastlogon >= DATE_TRUNC('day', CURRENT_TIMESTAMP)
	      AND
			  lastlogon <= DATE_TRUNC('day', CURRENT_TIMESTAMP) + INTERVAL '1 day - 1 second' THEN 1
		 ELSE 0
	    END as "lastlogon"	
	, badpwdcount, lockouttime, useraccountcontrol
FROM stage.ad_user
ORDER BY lockouttime DESC











