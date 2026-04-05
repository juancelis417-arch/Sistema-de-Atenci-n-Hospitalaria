def escribir_log(texto):
    with open("log.txt","a") as log:
        log.write(texto + "\n")