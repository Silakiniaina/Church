SELECT MAX(id) AS id ,
	   MAX(numero_dimanche) AS numero_dimanche,
	   MAX(annee) AS annee, 
	   id_eglise 
	   FROM offrande 
	   GROUP BY id_eglise,annee
	   ORDER BY annee
;