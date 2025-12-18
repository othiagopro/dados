filme = {
    "Titulo":"GOT",
    "Ano": 1977,
    "diretor":"Sei la"
}
del filme["diretor"]

print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
    print(f"O {k} é {v}.")