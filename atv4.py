consoantes = []
vogais = ["a", "e", "i", "o", "u"]

texto = input("Digite um nome ou palavra com 10 caracteres: ").lower()

if len(texto) == 10:

    for letra in texto:
        if letra.isalpha() and letra not in vogais:
            consoantes.append(letra)

    
    print(f"\nTotal de consoantes: {len(consoantes)}")
    print(f"Consoantes encontradas: {consoantes}")
else:
    print(f"\nErro: Você digitou {len(texto)} caracteres. Precisa ter exatamente 10!")
