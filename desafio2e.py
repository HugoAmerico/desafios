
def contar_letra_a(string):
    
    string_lower = string.lower()
    
   
    quantidade_a = string_lower.count('a')
    
    
    if quantidade_a > 0:
        return f"A letra 'a' aparece {quantidade_a} vez(es) na string."
    else:
        return "A letra 'a' não está presente na string."


string_exemplo = input("Informe uma string: ")
resultado_letra_a = contar_letra_a(string_exemplo)
print(resultado_letra_a)

