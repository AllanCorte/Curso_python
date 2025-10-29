profissionais = []  # type: ignore
email_existente = False
while True:
    email = str(input('digite seu email ou ["sair"]: '))
    if email == 'sair':
        break

    elif '@gmail.com' not in email:
        print('o email deve conter @gmail.com')
        continue

    for p in (profissionais):
        if p.get('Email') == email:
            print('email ja cadastrado!, por favor coloque outro')
            email_existente = True

    if email_existente:
        continue

    profissional = {'email': email}
    profissionais.append(profissional)

for i in profissionais:
    print(i)
