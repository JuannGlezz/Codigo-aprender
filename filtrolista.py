geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    array=[]
    for bird  in birds:
        if bird not in geese:
            array.append(bird)
    return array
  #Devuelve los pájaros que no figuran en la lista
