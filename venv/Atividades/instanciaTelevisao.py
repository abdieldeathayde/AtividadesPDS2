class instanciaTelevisao:
    
        
    from Televisao import Televisao
    tvBid = Televisao()
    tvLho = Televisao()
    tv3 = Televisao()
    tv4 = Televisao()
    
    
    tvBid.marca = "Dell"
    tvBid.tamanho="24'"
    tvLho.marca = "Philco"
    tvLho.tamanho="42'"
    tv3.tamanho = "23'"
    tv3.marca = "Samsung"
    tv4.marca = "Acer"
    tv4.tamanho = "30'"
    
    print(tvBid.marca + " " + tvBid.tamanho)