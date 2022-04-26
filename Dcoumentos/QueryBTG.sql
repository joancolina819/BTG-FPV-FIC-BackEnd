
-- ###############################################################################################################
-- NOMBRES DE LOS CLIENTES LOS CUALES TIENEN INSCRITO ALGUN PRODUCTO DISPONIBLE SOLO EN LAS SUCURSALES QUE VISITAN
-- ###############################################################################################################

	-- ###########################################################################################################
	-- INCIO FORMA #1: UTILIZANDO IN EN CONJUNTO CON INNER JOIN
	-- ###########################################################################################################
	SELECT 
		CLI.nombre						AS "Nombre",
		CLI.apellidos					AS "Apellido",
		CLI.nombre +' '+CLI.apellidos	AS "Nombre completo"
	FROM cliente AS CLI
	WHERE	[CLI].id IN (
				-- ID DE CLIENTES QUE TIENEN PRODUCTOS DISPONIBLES E INSCRITOS
				SELECT DISTINCT [INS].idCliente
				FROM inscripcion AS INS
					INNER JOIN [dbo].disponibilidad	AS DIS ON [DIS].idProducto = [INS].idProducto
				)
	AND		[CLI].id IN (
				-- ID DE CLIENTE QUE HAN VISITADO UNA SUCRUSAL
				SELECT DISTINCT [VIS].idCliente
				FROM visitan AS VIS
					INNER JOIN [dbo].sucursal	AS SUC ON [SUC].id = [VIS].idSucursal
				)
	-- ###########################################################################################################
	-- FIN FORMA #1: UTILIZANDO IN
	-- ###########################################################################################################

	-- ###########################################################################################################
	-- INCIO FORMA #2: UTILIZANDO INNER JOIN
	-- ###########################################################################################################
	SELECT 
		[CLI].nombre						AS "Nombre",
		[CLI].apellidos						AS "Apellido",
		[CLI].nombre +' '+[CLI].apellidos	AS "Nombre completo" 
	FROM dbo.cliente						AS [CLI]
		INNER JOIN [dbo].inscripcion		AS [INS] ON CLI.id			= [INS].idCliente
		INNER JOIN [dbo].disponibilidad		AS [DIS] ON INS.idProducto	= [INS].idProducto
		INNER JOIN [dbo].sucursal			AS [SUC] ON SUC.id			= [DIS].idSucursal
		INNER JOIN [dbo].visitan			AS [VIS] ON VIS.idSucursal	= [SUC].id AND [VIS].idCliente = [CLI].id
	GROUP BY [CLI].nombre, [CLI].apellidos
	-- ###########################################################################################################
	-- FIN FORMA #2: UTILIZANDO INNER JOIN
	-- ###########################################################################################################