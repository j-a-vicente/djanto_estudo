-- PROCEDURE: public.sp_all_tables_update_outros()

-- DROP PROCEDURE IF EXISTS public.sp_all_tables_update_outros();

CREATE OR REPLACE PROCEDURE public.sp_all_tables_update_outros(
	)
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
    num_update_outros_applications INTEGER;
	num_update_outros_disk INTEGER;
	num_update_outros_network_adapter INTEGER;
	num_update_outros_server_host INTEGER;
	num_update_outros_software INTEGER;

	
BEGIN
/************************** Insert de novos registros **************************/

--- applications 
    UPDATE public.master_tb_sccm_applications_up AS master
    SET 
      name0         =  st.name0,
      ad_site_name0 =  st.ad_site_name0,
      user_name0    =  st.user_name0,
      publisher0    =  st.publisher0,
      displayname0  =  st.displayname0,
      version0      =  st.version0
    FROM public.applications AS st
    WHERE master.resourceid = st.resourceid
      AND(master.name0         <> st.name0
       OR master.ad_site_name0 <> st.ad_site_name0
       OR master.user_name0    <> st.user_name0
       OR master.publisher0    <> st.publisher0
       OR master.displayname0  <> st.displayname0
       OR master.version0      <> st.version0);

    GET DIAGNOSTICS num_update_outros_applications = ROW_COUNT;
	
--- disk 
    UPDATE public.master_tb_sccm_vmdisk_up AS master
    SET 
     groupid          =  st.groupid,
     agentid          =  st.agentid,
     tmstamp          =  st.tmstamp,
     caption0         =  st.caption0,
     description0     =  st.description0,
     deviceid0        =  st.deviceid0,
     index0           =  st.index0,
     interfacetype0   =  st.interfacetype0,
     manufacturer0    =  st.manufacturer0,
     mediatype0       =  st.mediatype0,
     model0           =  st.model0,
     name0            =  st.name0,
     partitions0      =  st.partitions0,
     pnpdeviceid0     =  st.pnpdeviceid0,
     scsibus0         =  st.scsibus0,
     scsilogicalunit0 =  st.scsilogicalunit0,
     scsiport0        =  st.scsiport0,
     scsitargetid0    =  st.scsitargetid0,
     size0            =  st.size0,
     systemname0	  =  st.systemname0
    FROM public.disk AS st
    WHERE master.resourceid = st.resourceid
      AND(master.groupid          <> st.groupid
       OR master.agentid          <> st.agentid
       OR master.tmstamp          <> st.tmstamp
       OR master.caption0         <> st.caption0
       OR master.description0     <> st.description0
       OR master.deviceid0        <> st.deviceid0
       OR master.index0           <> st.index0
       OR master.interfacetype0   <> st.interfacetype0
       OR master.manufacturer0    <> st.manufacturer0
       OR master.mediatype0       <> st.mediatype0
       OR master.model0           <> st.model0
       OR master.name0            <> st.name0
       OR master.partitions0      <> st.partitions0
       OR master.pnpdeviceid0     <> st.pnpdeviceid0
       OR master.scsibus0         <> st.scsibus0
       OR master.scsilogicalunit0 <> st.scsilogicalunit0
       OR master.scsiport0        <> st.scsiport0
       OR master.scsitargetid0    <> st.scsitargetid0
       OR master.size0            <> st.size0
       OR master.systemname0	  <> st.systemname0);	
	
    GET DIAGNOSTICS num_update_outros_disk = ROW_COUNT;	

--- network_adapter 
    UPDATE public.master_tb_sccm_network_adapter_up AS master
    SET 
      dhcpenabled0 =  st.dhcpenabled0,
      dhcpserver0  =  st.dhcpserver0,
      dnsdomain0   =  st.dnsdomain0,
      dnshostname0 =  st.dnshostname0,
      ipaddress0   =  st.ipaddress0,
      deviceid0    =  st.deviceid0,
      ipenabled0   =  st.ipenabled0,
      ipsubnet0    =  st.ipsubnet0,
      servicename0 =  st.servicename0
    FROM public.network_adapter AS st
    WHERE master.resourceid = st.resourceid
	  AND master.adaptertype0 = st.adaptertype0
	  AND master.productname0 = st.productname0
	  AND master.macaddress0 = st.macaddress0
      AND(master.dhcpenabled0 <> st.dhcpenabled0
       OR master.dhcpserver0  <> st.dhcpserver0
       OR master.dnsdomain0   <> st.dnsdomain0
       OR master.dnshostname0 <> st.dnshostname0
       OR master.ipaddress0   <> st.ipaddress0
       OR master.deviceid0    <> st.deviceid0
       OR master.ipenabled0   <> st.ipenabled0
       OR master.ipsubnet0    <> st.ipsubnet0
       OR master.servicename0 <> st.servicename0);	
	
    GET DIAGNOSTICS num_update_outros_network_adapter = ROW_COUNT;
	
--- server_host 
    UPDATE public.master_tb_sccm_server_host_up AS master
    SET 	
      fabricante           =  st.fabricante,
      modelo               =  st.modelo,
      hostname             =  st.hostname,
      dominio              =  st.dominio,
      username             =  st.username,
      machinetype          =  st.machinetype,
      chassi               =  st.chassi,
      bioserialnumber      =  st.bioserialnumber,
      os                   =  st.os,
      ospkversao           =  st.ospkversao,
      osversao             =  st.osversao,
      nserie               =  st.nserie,
      totalphysicalmemory  =  st.totalphysicalmemory,
      cpufabricante        =  st.cpufabricante,
      cpumodelo            =  st.cpumodelo,
      cpusockets           =  st.cpusockets,
      corespersocket       =  st.corespersocket,
      status               =  st.status,
      clientsccm           =  st.clientsccm
    FROM public.server_host AS st
    WHERE master.resourceid = st.resourceid
      AND(master.fabricante           <> st.fabricante
       OR master.modelo               <> st.modelo
       OR master.hostname             <> st.hostname
       OR master.dominio              <> st.dominio
       OR master.username             <> st.username
       OR master.machinetype          <> st.machinetype
       OR master.chassi               <> st.chassi
       OR master.bioserialnumber      <> st.bioserialnumber
       OR master.os                   <> st.os
       OR master.ospkversao           <> st.ospkversao
       OR master.osversao             <> st.osversao
       OR master.nserie               <> st.nserie
       OR master.totalphysicalmemory  <> st.totalphysicalmemory
       OR master.cpufabricante        <> st.cpufabricante
       OR master.cpumodelo            <> st.cpumodelo
       OR master.cpusockets           <> st.cpusockets
       OR master.corespersocket       <> st.corespersocket
       OR master.status               <> st.status
       OR master.clientsccm           <> st.clientsccm);
	   
    GET DIAGNOSTICS num_update_outros_server_host = ROW_COUNT;	
	
	
--- software 
    UPDATE public.master_tb_sccm_software_up AS master
    SET 	
      name0       =  st.name0,
      companyname =  st.companyname,
      productname =  st.productname,
      filename    =  st.filename,
      fileversion =  st.fileversion,
      filepath	  =  st.filepath
    FROM public.software AS st
    WHERE master.resourceid = st.resourceid
      AND(master.name0       <> st.name0
       OR master.companyname <> st.companyname
       OR master.productname <> st.productname
       OR master.filename    <> st.filename
       OR master.fileversion <> st.fileversion
       OR master.filepath	 <> st.filepath);
	
    GET DIAGNOSTICS num_update_outros_software = ROW_COUNT;

	   
    /******************************* Retorno da SP. *******************************/
    RAISE NOTICE 'Updates em outros colunas na tabelas applications: %', num_update_outros_applications;
	RAISE NOTICE 'Updates em outros colunas na tabelas disk: %', num_update_outros_disk;
	RAISE NOTICE 'Updates em outros colunas na tabelas network_adapter: %', num_update_outros_network_adapter;
	RAISE NOTICE 'Updates em outros colunas na tabelas server_host: %', num_update_outros_server_host;
	RAISE NOTICE 'Updates em outros colunas na tabelas software: %', num_update_outros_software;	

END 
$BODY$;
ALTER PROCEDURE public.sp_all_tables_update_outros()
    OWNER TO "Sentinel";

-- PROCEDURE: public.sp_all_tables_update_desativar()

-- DROP PROCEDURE IF EXISTS public.sp_all_tables_update_desativar();

CREATE OR REPLACE PROCEDURE public.sp_all_tables_update_desativar(
	)
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
    num_update_desativar_applications INTEGER;
	num_update_desativar_disk INTEGER;
	num_update_desativar_network_adapter INTEGER;
	num_update_desativar_server_host INTEGER;
	num_update_desativar_software INTEGER;

	
BEGIN
    /******************************* Update Desativar registros *******************************/
	
-- 	applications
    CREATE TEMP TABLE temp_key (key_0 integer);

    INSERT INTO temp_key (key_0)
    SELECT st.id_applications
    FROM public.replica_02_tb_sccm_applications AS st
    WHERE NOT EXISTS (
        SELECT 1
        FROM public.applications AS it
        WHERE it.resourceid = st.resourceid
    );

    UPDATE public.master_tb_sccm_applications_up AS master
    SET 
        ativo = false
    WHERE master.id_applications IN (SELECT key_0 FROM temp_key);
	
    GET DIAGNOSTICS num_update_desativar_applications = ROW_COUNT;
    
    DROP TABLE temp_key;

------------------------------------------------------------------------------------------------------	
	
-- disk	
    CREATE TEMP TABLE temp_key (key_0 integer);

    INSERT INTO temp_key (key_0)
    SELECT st.id_vmdisk
    FROM public.replica_02_tb_sccm_vmdisk AS st
    WHERE NOT EXISTS (
        SELECT 1
        FROM public.disk AS it
        WHERE it.resourceid = st.resourceid
    );

    UPDATE public.master_tb_sccm_vmdisk_up AS master
    SET 
        ativo = false
    WHERE master.id_vmdisk IN (SELECT key_0 FROM temp_key);
	
    GET DIAGNOSTICS num_update_desativar_disk = ROW_COUNT;
    
    DROP TABLE temp_key;

------------------------------------------------------------------------------------------------------	
	
-- network_adapter
    CREATE TEMP TABLE temp_key (key_0 integer);

    INSERT INTO temp_key (key_0)
    SELECT st.id_network_adapter
    FROM public.replica_02_tb_sccm_network_adapter AS st
    WHERE NOT EXISTS (
        SELECT 1
        FROM public.network_adapter AS it
        WHERE it.resourceid = st.resourceid
		  AND it.adaptertype0 = st.adaptertype0
		  AND it.productname0 = st.productname0
		  AND it.macaddress0 = st.macaddress0		
    );

    UPDATE public.master_tb_sccm_network_adapter_up AS master
    SET 
        ativo = false
    WHERE master.id_network_adapter IN (SELECT key_0 FROM temp_key);
	
    GET DIAGNOSTICS num_update_desativar_network_adapter = ROW_COUNT;
    
    DROP TABLE temp_key;

------------------------------------------------------------------------------------------------------		
	
-- server_host
    CREATE TEMP TABLE temp_key (key_0 integer);

    INSERT INTO temp_key (key_0)
    SELECT st.id_server_host
    FROM public.replica_02_tb_sccm_server_host AS st
    WHERE NOT EXISTS (
        SELECT 1
        FROM public.server_host AS it
        WHERE it.resourceid = st.resourceid
    );

    UPDATE public.master_tb_sccm_server_host_up AS master
    SET 
        ativo = false
    WHERE master.id_server_host IN (SELECT key_0 FROM temp_key);
	
    GET DIAGNOSTICS num_update_desativar_server_host = ROW_COUNT;
    
    DROP TABLE temp_key;

------------------------------------------------------------------------------------------------------		
	
-- software
    CREATE TEMP TABLE temp_key (key_0 integer);

    INSERT INTO temp_key (key_0)
    SELECT st.id_software
    FROM public.replica_02_tb_sccm_software AS st
    WHERE NOT EXISTS (
        SELECT 1
        FROM public.software AS it
        WHERE it.resourceid = st.resourceid
    );

    UPDATE public.master_tb_sccm_software_up AS master
    SET 
        ativo = false
    WHERE master.id_software IN (SELECT key_0 FROM temp_key);
	
    GET DIAGNOSTICS num_update_desativar_software = ROW_COUNT;
    
    DROP TABLE temp_key;


------------------------------------------------------------------------------------------------------		


    /******************************* Retorno da SP. *******************************/
    RAISE NOTICE 'Registros desativados na tabela applications: %', num_update_desativar_applications;
	RAISE NOTICE 'Registros desativados na tabela disk: %', num_update_desativar_disk;
	RAISE NOTICE 'Registros desativados na tabela network_adapter: %', num_update_desativar_network_adapter;
	RAISE NOTICE 'Registros desativados na tabela server_host: %', num_update_desativar_server_host;
	RAISE NOTICE 'Registros desativados na tabela software: %', num_update_desativar_software;	
		
END 
$BODY$;
ALTER PROCEDURE public.sp_all_tables_update_desativar()
    OWNER TO "Sentinel";



-- PROCEDURE: public.sp_all_tables_update_reativar()

-- DROP PROCEDURE IF EXISTS public.sp_all_tables_update_reativar();

CREATE OR REPLACE PROCEDURE public.sp_all_tables_update_reativar(
	)
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE

    num_update_reativar_applications INTEGER;
	num_update_reativar_disk INTEGER;
	num_update_reativar_network_adapter INTEGER;
	num_update_reativar_server_host INTEGER;
	num_update_reativar_software INTEGER;
	
BEGIN
/************************** Update Reativar registros **************************/	

-- applications
    UPDATE public.master_tb_sccm_applications_up AS master
    SET 
        ativo = true
    FROM public.applications AS st
    WHERE master.resourceid   = st.resourceid
	  AND master.ativo = false;
	  
	GET DIAGNOSTICS num_update_reativar_applications = ROW_COUNT;


-----------------------------------------------------------------------------------	
	
-- disk	
    UPDATE public.master_tb_sccm_vmdisk_up AS master
    SET 
        ativo = true
    FROM public.disk AS st
    WHERE master.resourceid   = st.resourceid
	  AND master.ativo = false;

	GET DIAGNOSTICS num_update_reativar_disk = ROW_COUNT;
	
-----------------------------------------------------------------------------------

-- network_adapter
    UPDATE public.master_tb_sccm_network_adapter_up AS master
    SET 
        ativo = true
    FROM public.network_adapter AS st
    WHERE master.resourceid   = st.resourceid
	  AND it.adaptertype0 = st.adaptertype0
	  AND it.productname0 = st.productname0
	  AND it.macaddress0 = st.macaddress0		
	  AND master.ativo = false;
	  
	GET DIAGNOSTICS num_update_reativar_network_adapter = ROW_COUNT;	
	
	
-----------------------------------------------------------------------------------

-- server_host
    UPDATE public.master_tb_sccm_server_host_up AS master
    SET 
        ativo = true
    FROM public.server_host AS st
    WHERE master.resourceid = st.resourceid
	  AND master.ativo = false;
	  
	GET DIAGNOSTICS num_update_reativar_server_host = ROW_COUNT;		
	
	
-----------------------------------------------------------------------------------

-- software
    UPDATE public.master_tb_sccm_software_up AS master
    SET 
        ativo = true
    FROM public.software AS st
    WHERE master.resourceid = st.resourceid
	  AND master.ativo = false;
	GET DIAGNOSTICS num_update_reativar_software = ROW_COUNT;		
	

    /******************************* Retorno da SP. *******************************/
    RAISE NOTICE 'Registros reativados na tabela applications: %', num_update_reativar_applications;
	RAISE NOTICE 'Registros reativados na tabela disk: %', num_update_reativar_disk;
	RAISE NOTICE 'Registros reativados na tabela network_adapter: %', num_update_reativar_network_adapter;
	RAISE NOTICE 'Registros reativados na tabela server_host: %', num_update_reativar_server_host;
	RAISE NOTICE 'Registros reativados na tabela software: %', num_update_reativar_software;
	
END 
$BODY$;
ALTER PROCEDURE public.sp_all_tables_update_reativar()
    OWNER TO "Sentinel";


-- PROCEDURE: public.sp_all_tables_insert_new()

-- DROP PROCEDURE IF EXISTS public.sp_all_tables_insert_new();

CREATE OR REPLACE PROCEDURE public.sp_all_tables_insert_new(
	)
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
    num_insert_applications INTEGER;
	num_insert_disk INTEGER;
	num_insert_network_adapter INTEGER;
	num_insert_server_host INTEGER;
	num_insert_software INTEGER;
	
BEGIN
/************************** Insert de novos registros **************************/

--- applications
	INSERT INTO public.master_tb_sccm_applications_in(resourceid, name0, ad_site_name0, user_name0, publisher0, displayname0, version0)
	SELECT resourceid, name0, ad_site_name0, user_name0, publisher0, displayname0, version0
	FROM public.applications AS st
	WHERE 
	NOT EXISTS(SELECT * 
	            FROM public.replica_02_tb_sccm_applications AS it
				 WHERE it.resourceid = st.resourceid);
				 
	GET DIAGNOSTICS num_insert_applications = ROW_COUNT;
	
	
--- disk
	INSERT INTO public.master_tb_sccm_vmdisk_in(resourceid, groupid, agentid, tmstamp, caption0, description0, deviceid0, index0, interfacetype0, manufacturer0, mediatype0, model0, name0, partitions0, pnpdeviceid0, scsibus0, scsilogicalunit0, scsiport0, scsitargetid0, size0, systemname0)
	SELECT resourceid, groupid, agentid, tmstamp, caption0, description0, deviceid0, index0, interfacetype0, manufacturer0, mediatype0, model0, name0, partitions0, pnpdeviceid0, scsibus0, scsilogicalunit0, scsiport0, scsitargetid0, size0, systemname0
	FROM public.disk AS st
	WHERE 
	NOT EXISTS(SELECT * 
	            FROM public.replica_02_tb_sccm_vmdisk AS it
				 WHERE it.resourceid = st.resourceid);
				 
	GET DIAGNOSTICS num_insert_disk = ROW_COUNT;	


--- network_adapter
	INSERT INTO public.master_tb_sccm_network_adapter_in(resourceid, adaptertype0, productname0, macaddress0, dhcpenabled0, dhcpserver0, dnsdomain0, dnshostname0, ipaddress0, deviceid0, ipenabled0, ipsubnet0, servicename0)
	SELECT resourceid, adaptertype0, productname0, macaddress0, dhcpenabled0, dhcpserver0, dnsdomain0, dnshostname0, ipaddress0, deviceid0, ipenabled0, ipsubnet0, servicename0
	FROM public.network_adapter AS st
	WHERE 
	NOT EXISTS(SELECT * 
	            FROM public.replica_02_tb_sccm_network_adapter AS it
				 WHERE it.resourceid   = st.resourceid
				   AND it.adaptertype0 = st.adaptertype0
				   AND it.productname0 = st.productname0
				   AND it.macaddress0  = st.macaddress0);
				 
	GET DIAGNOSTICS num_insert_network_adapter = ROW_COUNT;


--- server_host	
	INSERT INTO public.master_tb_sccm_server_host_in(resourceid, fabricante, modelo, hostname, dominio, username, machinetype, chassi, bioserialnumber, os, ospkversao, osversao, nserie, totalphysicalmemory, cpufabricante, cpumodelo, cpusockets, corespersocket, status, clientsccm)
	SELECT resourceid, fabricante, modelo, hostname, dominio, username, machinetype, chassi, bioserialnumber, os, ospkversao, osversao, nserie, totalphysicalmemory, cpufabricante, cpumodelo, cpusockets, corespersocket, status, clientsccm
	FROM public.server_host AS st
	WHERE 
	NOT EXISTS(SELECT * 
	            FROM public.replica_02_tb_sccm_server_host AS it
				 WHERE it.resourceid = st.resourceid);
				 
	GET DIAGNOSTICS num_insert_server_host = ROW_COUNT;	

--- software		
	INSERT INTO public.master_tb_sccm_software_in(resourceid, name0, companyname, productname, filename, fileversion, filepath)
	SELECT resourceid, name0, companyname, productname, filename, fileversion, filepath
	FROM public.software AS st
	WHERE 
	NOT EXISTS(SELECT * 
	            FROM public.replica_02_tb_sccm_software AS it
				 WHERE it.resourceid = st.resourceid);
				 
	GET DIAGNOSTICS num_insert_software = ROW_COUNT;


    /******************************* Retorno da SP. *******************************/
    RAISE NOTICE 'Novos registros inseridos na tabela applications: %', num_insert_applications;
	RAISE NOTICE 'Novos registros inseridos na tabela disk: %', num_insert_disk;
	RAISE NOTICE 'Novos registros inseridos na tabela network_adapter: %', num_insert_network_adapter;
	RAISE NOTICE 'Novos registros inseridos na tabela server_host: %', num_insert_server_host;
	RAISE NOTICE 'Novos registros inseridos na tabela software: %', num_insert_software;

END 
$BODY$;
ALTER PROCEDURE public.sp_all_tables_insert_new()
    OWNER TO "Sentinel";



-- View: public.vw_etl_script

-- DROP VIEW public.vw_etl_script;

CREATE OR REPLACE VIEW public.vw_etl_script
 AS
 SELECT e.id_modulo_etl,
    s.filename,
    s.id_dependencia,
    s.dependencia,
    s.exec_paralelo,
    d.id_modulo_datafont,
    d.tipo_font,
    d.servername,
    d.serverip,
    d.sgbp,
    d.databasename,
    d.username,
    d.psw,
    d.port,
    d.stringconection
   FROM modulo_etl e
     JOIN modulo_etl_script s ON s.id_modulo_etl = e.id_modulo_etl
     JOIN modulo_etl_datafont_origem o ON o.id_modulo_etl_script = s.id_modulo_etl_script
     JOIN modulo_datafont d ON d.id_modulo_datafont = o.id_modulo_datafont;

ALTER TABLE public.vw_etl_script
    OWNER TO "Sentinel";

-- View: public.vw_modulo_job_detalhe

-- DROP VIEW public.vw_modulo_job_detalhe;

CREATE OR REPLACE VIEW public.vw_modulo_job_detalhe
 AS
 SELECT s.id_modulo_jobs_schedule,
    j.id_modulo_etl,
    j.nomejobs,
    s.nomeschedule,
        CASE
            WHEN r.dt_start IS NOT NULL THEN 'Sucesso'::text
            ELSE 'FALHA'::text
        END AS statusexecucao,
    r.dt_start AS ultimaexecucao,
    l.frequencia,
    l.tiposchedule,
    l.repetir,
    l.recorreacada,
    l.datainicio,
    l.dataparada,
    l.horainicial,
    l.horafinal
   FROM modulo m
     JOIN modulo_jobs j ON j.id_modulo = m.id_modulo
     JOIN modulo_jobs_schedule s ON s.id_modulo_jobs = j.id_modulo_jobs
     JOIN LATERAL get_json_fields(s.id_modulo_jobs_schedule) l(frequencia, tiposchedule, repetir, recorreacada, datainicio, dataparada, horainicial, horafinal) ON l.frequencia IS NOT NULL
     LEFT JOIN ( SELECT modulo_logs.id_modulo_jobs_schedule,
            max(modulo_logs.dt_start) AS dt_start
           FROM modulo_logs
          GROUP BY modulo_logs.id_modulo_jobs_schedule) r ON r.id_modulo_jobs_schedule = s.id_modulo_jobs_schedule
  WHERE m.ativo = true AND j.ativo = true AND s.ativo = true;

ALTER TABLE public.vw_modulo_job_detalhe
    OWNER TO "Sentinel";

-- View: public.vw_schedule_frequencia_1

-- DROP VIEW public.vw_schedule_frequencia_1;

CREATE OR REPLACE VIEW public.vw_schedule_frequencia_1
 AS
 WITH RECURSIVE execution_times AS (
         SELECT s.id_modulo_jobs_schedule,
            j.id_modulo_etl,
            get_dt_start(s.id_modulo_jobs_schedule,
                CASE
                    WHEN l.frequencia = '1'::text AND l.repetir ~~ '%Hora%'::text THEN
                    CASE
                        WHEN date_trunc('minute'::text, now()) > date_trunc('minute'::text, now()::date + l.horainicial::time without time zone) THEN date_trunc('minute'::text, now()::date + l.horainicial::time without time zone) + '01:00:00'::interval
                        ELSE date_trunc('minute'::text, now()::date + l.horainicial::time without time zone)
                    END
                    WHEN l.frequencia = '1'::text AND l.repetir ~~ '%Minuto%'::text THEN
                    CASE
                        WHEN date_trunc('minute'::text, now()) > date_trunc('minute'::text, now()::date + l.horainicial::time without time zone) THEN date_trunc('minute'::text, now()::date + l.horainicial::time without time zone) + '00:30:00'::interval
                        ELSE date_trunc('minute'::text, now()::date + l.horainicial::time without time zone)
                    END
                    ELSE NULL::timestamp without time zone
                END) AS ultimaexecucao,
            l.frequencia,
            l.repetir,
            l.recorreacada,
            l.datainicio,
            l.dataparada,
            l.horainicial,
            l.horafinal,
                CASE
                    WHEN l.frequencia = '1'::text AND l.repetir ~~ '%Hora%'::text THEN
                    CASE
                        WHEN date_trunc('minute'::text, now()) > date_trunc('minute'::text, now()::date + l.horainicial::time without time zone) THEN date_trunc('minute'::text, now()::date + l.horainicial::time without time zone) + '01:00:00'::interval
                        ELSE date_trunc('minute'::text, now()::date + l.horainicial::time without time zone)
                    END
                    WHEN l.frequencia = '1'::text AND l.repetir ~~ '%Minuto%'::text THEN
                    CASE
                        WHEN date_trunc('minute'::text, now()) > date_trunc('minute'::text, now()::date + l.horainicial::time without time zone) THEN date_trunc('minute'::text, now()::date + l.horainicial::time without time zone) + '00:30:00'::interval
                        ELSE date_trunc('minute'::text, now()::date + l.horainicial::time without time zone)
                    END
                    ELSE NULL::timestamp without time zone
                END AS proximaexecucao
           FROM modulo m
             JOIN modulo_jobs j ON j.id_modulo = m.id_modulo
             JOIN modulo_jobs_schedule s ON s.id_modulo_jobs = j.id_modulo_jobs
             JOIN LATERAL get_json_fields(s.id_modulo_jobs_schedule) l(frequencia, tiposchedule, repetir, recorreacada, datainicio, dataparada, horainicial, horafinal) ON l.frequencia IS NOT NULL
          WHERE m.ativo = true AND j.ativo = true AND s.ativo = true AND l.frequencia = '1'::text
        UNION ALL
         SELECT et.id_modulo_jobs_schedule,
            et.id_modulo_etl,
            et.ultimaexecucao,
            et.frequencia,
            et.repetir,
            et.recorreacada,
            et.datainicio,
            et.dataparada,
            et.horainicial,
            et.horafinal,
                CASE
                    WHEN et.frequencia = '1'::text AND et.repetir ~~ '%Hora%'::text THEN et.proximaexecucao + '01:00:00'::interval
                    WHEN et.frequencia = '1'::text AND et.repetir ~~ '%Minuto%'::text THEN et.proximaexecucao + '00:30:00'::interval
                    ELSE NULL::timestamp without time zone
                END AS proximaexecucao
           FROM execution_times et
          WHERE et.proximaexecucao IS NOT NULL AND et.proximaexecucao <= (now() + '24:00:00'::interval) AND et.frequencia = '1'::text
        )
 SELECT id_modulo_jobs_schedule,
    id_modulo_etl,
        CASE
            WHEN ultimaexecucao IS NULL AND date_trunc('minute'::text, now()) > proximaexecucao THEN 'FALHA'::text
            WHEN ultimaexecucao IS NULL AND date_trunc('minute'::text, now()) <= proximaexecucao THEN 'NÃO INICIADO'::text
            WHEN ultimaexecucao IS NOT NULL THEN 'Sucesso'::text
            ELSE NULL::text
        END AS statusexecucao,
    ultimaexecucao,
    frequencia,
    repetir,
    recorreacada,
    datainicio,
    dataparada,
    horainicial,
    horafinal,
    proximaexecucao
   FROM execution_times
  ORDER BY id_modulo_jobs_schedule, proximaexecucao;

ALTER TABLE public.vw_schedule_frequencia_1
    OWNER TO "Sentinel";

-- View: public.vw_schedule_frequencia_2

-- DROP VIEW public.vw_schedule_frequencia_2;

CREATE OR REPLACE VIEW public.vw_schedule_frequencia_2
 AS
 WITH RECURSIVE execution_times AS (
         SELECT s.id_modulo_jobs_schedule,
            j.id_modulo_etl,
            get_dt_start(s.id_modulo_jobs_schedule,
                CASE
                    WHEN l.frequencia = '2'::text THEN
                    CASE
                        WHEN date_trunc('minute'::text, now()) > date_trunc('minute'::text, now()::date + l.recorreacada::time without time zone) THEN date_trunc('minute'::text, now()::date + l.recorreacada::time without time zone) + '00:00:00'::interval
                        ELSE date_trunc('minute'::text, now()::date + l.recorreacada::time without time zone)
                    END
                    ELSE NULL::timestamp without time zone
                END) AS ultimaexecucao,
            l.frequencia,
            'Diário'::text AS repetir,
            l.recorreacada,
            l.datainicio,
            l.dataparada,
            l.horainicial,
            l.horafinal,
                CASE
                    WHEN l.frequencia = '2'::text THEN
                    CASE
                        WHEN date_trunc('minute'::text, now()) > date_trunc('minute'::text, now()::date + l.recorreacada::time without time zone) THEN date_trunc('minute'::text, now()::date + l.recorreacada::time without time zone) + '00:00:00'::interval
                        ELSE date_trunc('minute'::text, now()::date + l.recorreacada::time without time zone)
                    END
                    ELSE NULL::timestamp without time zone
                END AS proximaexecucao
           FROM modulo m
             JOIN modulo_jobs j ON j.id_modulo = m.id_modulo
             JOIN modulo_jobs_schedule s ON s.id_modulo_jobs = j.id_modulo_jobs
             JOIN LATERAL get_json_fields(s.id_modulo_jobs_schedule) l(frequencia, tiposchedule, repetir, recorreacada, datainicio, dataparada, horainicial, horafinal) ON l.frequencia IS NOT NULL
          WHERE m.ativo = true AND j.ativo = true AND s.ativo = true
        UNION ALL
         SELECT et.id_modulo_jobs_schedule,
            et.id_modulo_etl,
            et.ultimaexecucao,
            et.frequencia,
            'Diário'::text AS repetir,
            et.recorreacada,
            et.datainicio,
            et.dataparada,
            et.horainicial,
            et.horafinal,
            et.proximaexecucao + '1 day'::interval AS proximaexecucao
           FROM execution_times et
          WHERE et.proximaexecucao IS NOT NULL AND et.proximaexecucao <= (now() + '24:00:00'::interval)
        )
 SELECT id_modulo_jobs_schedule,
    id_modulo_etl,
        CASE
            WHEN ultimaexecucao IS NULL AND date_trunc('minute'::text, now()) > proximaexecucao THEN 'FALHA'::text
            WHEN ultimaexecucao IS NULL AND date_trunc('minute'::text, now()) <= proximaexecucao THEN 'NÃO INICIADO'::text
            WHEN ultimaexecucao IS NOT NULL THEN 'Sucesso'::text
            ELSE NULL::text
        END AS statusexecucao,
    ultimaexecucao,
    frequencia,
    repetir,
    recorreacada,
    datainicio,
    dataparada,
    horainicial,
    horafinal,
    proximaexecucao
   FROM execution_times
  WHERE frequencia = '2'::text
  ORDER BY id_modulo_jobs_schedule, proximaexecucao;

ALTER TABLE public.vw_schedule_frequencia_2
    OWNER TO "Sentinel";


CREATE FOREIGN TABLE IF NOT EXISTS public.master_tb_host(
    hostid integer,
    name character varying(255) COLLATE pg_catalog."default",
    status integer
)
    SERVER rm_zabbix
    OPTIONS (schema_name 'public', table_name 'hosts');

ALTER FOREIGN TABLE public.master_tb_host
    OWNER TO "Sentinel";

CREATE FOREIGN TABLE IF NOT EXISTS public.replica_02_tb_host(
    hostid integer,
    name character varying(255) COLLATE pg_catalog."default",
    status integer
)
    SERVER rm_zabbix
    OPTIONS (schema_name 'public', table_name 'hosts');

ALTER FOREIGN TABLE public.replica_02_tb_host
    OWNER TO "Sentinel";



    -- MASTER
CREATE SERVER rm_master_sds_inventario
    FOREIGN DATA WRAPPER postgres_fdw
    OPTIONS (host '172.18.0.3', dbname 'sds_inventario', port '5432');

ALTER SERVER rm_master_sds_inventario
    OWNER TO "Sentinel";

CREATE USER MAPPING FOR "Sentinel" SERVER rm_master_sds_inventario
    OPTIONS ("user" 'Sentinel', password 'Sentinel');	
	
	


CREATE SEQUENCE IF NOT EXISTS public.hists_id_hist_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE SEQUENCE IF NOT EXISTS public.trends_id_trend_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE TABLE public.hosts (
    hostid INTEGER PRIMARY KEY,
	id_server_host INTEGER NULL,
    name VARCHAR(255) NOT NULL,
    status INTEGER NOT NULL);

CREATE TABLE public.items (
    itemid INTEGER PRIMARY KEY,
    hostid INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    type INTEGER NOT NULL);

CREATE TABLE public.hists (
	id_hist integer NOT NULL DEFAULT nextval('hists_id_hist_seq'::regclass),
    itemids     INTEGER,
    clock       TIMESTAMPTZ NOT NULL,
    value       REAL,
    num         INTEGER);

CREATE TABLE public.trends (
	id_trend integer NOT NULL DEFAULT nextval('trends_id_trend_seq'::regclass),
    itemids     INTEGER,
    clock       TIMESTAMPTZ NOT NULL,
    num         INTEGER,
    value_min   REAL,
    value_avg   REAL,
    value_max   REAL);
	
SELECT create_hypertable('hists', 'clock', chunk_time_interval => INTERVAL '1 month');
SELECT create_hypertable('trends', 'clock', chunk_time_interval => INTERVAL '1 month');
	
SELECT create_hypertable('hists', 'clock', chunk_time_interval => 86400);
SELECT create_hypertable('trends', 'clock', chunk_time_interval => 86400);


ALTER SEQUENCE public.hists_id_hist_seq  OWNER TO "Sentinel";
ALTER SEQUENCE public.trends_id_trend_seq  OWNER TO "Sentinel";
ALTER TABLE IF EXISTS public.hosts OWNER to "Sentinel";
ALTER TABLE IF EXISTS public.items OWNER to "Sentinel";
ALTER TABLE IF EXISTS public.hists OWNER to "Sentinel";
ALTER TABLE IF EXISTS public.trends OWNER to "Sentinel";


CREATE OR REPLACE VIEW public.vw_hists_ult_reg
 AS
 SELECT itemids,
    max(clock) AS clock
   FROM hists
  GROUP BY itemids
  ORDER BY itemids;

ALTER TABLE public.vw_hists_ult_reg
    OWNER TO "Sentinel";
	
CREATE OR REPLACE VIEW public.vw_items_host
 AS
 SELECT a.itemid,
    a.hostid,
    b.id_server_host,
    b.name AS server_host,
    a.name,
    a.type,
    a.monitor,
    d.clock
   FROM items a
     JOIN hosts b ON b.hostid = a.hostid
     LEFT JOIN vw_hists_ult_reg d ON d.itemids = a.itemid;

ALTER TABLE public.vw_items_host
    OWNER TO "Sentinel";
	
CREATE INDEX IF NOT EXISTS hists_clock_idx
    ON public.hists USING btree
    (clock DESC NULLS FIRST)
    TABLESPACE pg_default;




--STAGE

CREATE TABLE public.hosts (
    hostid INT,
    name VARCHAR(255) NOT NULL,
    status INTEGER NOT NULL);

CREATE TABLE public.items (
    itemid INT,
    hostid INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    type INTEGER NOT NULL);

CREATE TABLE public.hists (
    itemids     INT,
    clock       TIMESTAMPTZ NOT NULL,
    value       REAL,
    num         INT);

CREATE TABLE public.trends (
    itemids     INT,
    clock       TIMESTAMPTZ NOT NULL,
    num         INT,
    value_min   REAL,
    value_avg   REAL,
    value_max   REAL);

ALTER TABLE IF EXISTS public.hosts OWNER to "Sentinel";
ALTER TABLE IF EXISTS public.items OWNER to "Sentinel";
ALTER TABLE IF EXISTS public.hists OWNER to "Sentinel";
ALTER TABLE IF EXISTS public.trends OWNER to "Sentinel";

-- View: public.vw_st_serverhost_origemii

-- DROP VIEW public.vw_st_serverhost_origemii;

CREATE OR REPLACE VIEW public.vw_st_serverhost_origemii
 AS
 SELECT
        CASE
            WHEN ad = true THEN count(ad)
            ELSE 0::bigint
        END AS ad,
        CASE
            WHEN sccm = true THEN count(sccm)
            ELSE 0::bigint
        END AS sccm,
        CASE
            WHEN nx = true THEN count(nx)
            ELSE 0::bigint
        END AS nutanix,
        CASE
            WHEN vw = true THEN count(vw)
            ELSE 0::bigint
        END AS vmware,
        CASE
            WHEN or_ad = true THEN count(ad)
            ELSE 0::bigint
        END AS o_ad,
        CASE
            WHEN or_sccm = true THEN count(sccm)
            ELSE 0::bigint
        END AS o_sccm,
        CASE
            WHEN or_nx = true THEN count(nx)
            ELSE 0::bigint
        END AS o_nutanix,
        CASE
            WHEN or_vw = true THEN count(vw)
            ELSE 0::bigint
        END AS o_vmware
   FROM serverhost
  GROUP BY ad, or_ad, sccm, or_sccm, nx, or_nx, vw, or_vw
  ORDER BY (
        CASE
            WHEN or_ad = true THEN 'Active Directory'::text
            WHEN or_sccm = true THEN 'SCCM'::text
            WHEN or_nx = true THEN 'Nutanix'::text
            WHEN or_vw = true THEN 'VMware'::text
            ELSE NULL::text
        END);

ALTER TABLE public.vw_st_serverhost_origemii
    OWNER TO "Sentinel";

-- View: public.vw_st_serverhost_origem_total

-- DROP VIEW public.vw_st_serverhost_origem_total;

CREATE OR REPLACE VIEW public.vw_st_serverhost_origem_total
 AS
 SELECT
        CASE
            WHEN serverhost.or_ad = true THEN 'Active Directory'::text
            WHEN serverhost.or_sccm = true THEN 'SCCM'::text
            WHEN serverhost.or_nx = true THEN 'Nutanix'::text
            WHEN serverhost.or_vw = true THEN 'VMware'::text
            ELSE NULL::text
        END AS "Origem",
        CASE
            WHEN serverhost.or_ad = true THEN count(serverhost.hostname)
            WHEN serverhost.or_sccm = true THEN count(serverhost.hostname)
            WHEN serverhost.or_nx = true THEN count(serverhost.hostname)
            WHEN serverhost.or_vw = true THEN count(serverhost.hostname)
            ELSE NULL::bigint
        END AS "Total"
   FROM serverhost
  WHERE serverhost.ativo = true
  GROUP BY serverhost.or_ad, serverhost.or_sccm, serverhost.or_nx, serverhost.or_vw
UNION ALL
 SELECT 'Total'::text AS "Origem",
    count(serverhost.hostname) AS "Total"
   FROM serverhost
  WHERE serverhost.ativo = true;

ALTER TABLE public.vw_st_serverhost_origem_total
    OWNER TO "Sentinel";

-- View: public.vw_st_serverhost_origem_cruzado

-- DROP VIEW public.vw_st_serverhost_origem_cruzado;

CREATE OR REPLACE VIEW public.vw_st_serverhost_origem_cruzado
 AS
 SELECT ad,
    count(ad) AS t_ad,
    or_ad,
    count(or_ad) AS t_or_ad,
    sccm,
    count(sccm) AS t_sccm,
    or_sccm,
    count(or_sccm) AS t_or_sccm,
    nx,
    count(nx) AS t_nx,
    or_nx,
    count(or_nx) AS t_or_nx,
    vw,
    count(vw) AS t_vw,
    or_vw,
    count(or_vw) AS t_or_vw
   FROM serverhost
  GROUP BY ad, or_ad, sccm, or_sccm, nx, or_nx, vw, or_vw;

ALTER TABLE public.vw_st_serverhost_origem_cruzado
    OWNER TO "Sentinel";



SELECT fisicovm, count(fisicovm)
	FROM public.vw_serverhost
WHERE ativo = true	
GROUP BY fisicovm

SELECT "Origem", "Total"
	FROM public.vw_st_serverhost_origem_total;
	
SELECT zabbix, COUNT(zabbix)
	FROM public.vw_serverhost
WHERE fisicovm = 'Servidor'
GROUP BY zabbix		

SELECT id_serverhost, hostname, fisicovm, sistemaoperaciona, zabbix
	FROM public.vw_serverhost;




    