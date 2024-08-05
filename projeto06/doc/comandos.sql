SELECT M.id_modulo
	 , M.modulo
	 , E.etl_name
	 , F.tipo_font
	 , S.filename, S.codigofont, S.exec_paralelo
	 , F.servername
	 , F.serverip
	 , F.port
	 , F.stringconection
	 , F.sgbp
	 , F.databasename
	 , F.username
	 , F.psw	 
FROM public.modulo M
INNER JOIN public.modulo_etl E ON E.id_modulo = M.id_modulo
INNER JOIN public.modulo_datafont F ON F.id_modulo = M.id_modulo
INNER JOIN modulo_etl_script S ON S.id_modulo_etl = E.id_modulo_etl




