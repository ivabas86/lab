# TODO Найдите количество книг, которое можно разместить на дискете
ob_diskety = int(1.44*1024*1024)
str_v_knige = 100
ch_strok = 50
kol_simvol = 25
ob_koda_simvola = 4
knigi = ob_diskety//(str_v_knige*ch_strok*kol_simvol*ob_koda_simvola)
print("Количество книг, помещающихся на дискету:", knigi)