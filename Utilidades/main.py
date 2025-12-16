def clientes_emails(): #+5565981363052

    mes, ano = str(compet()).split("/")

    recusa = ['tecnomaquinas@outlook.com.br', 'flopesdegodoy@gmail.com','administrativo@plantiomaquinas.com.br', 'tiagocardozopdo@hotmail.com', 'diretoria@mixdasaude.com.br', 'admin@gruposantosmt.com.br', 'administrativo@gpconstrutora.com.br', 'administrativo@grupoenbase.com.br']
    substituto = {
            'diretoria@mixdasaude.com.br':'financeiro@mixdasaude.com.br',
            'admin@gruposantosmt.com.br':'contabil@gruposantosmt.com.br',
            'administrativo@gpconstrutora.com.br':'administrativo@grupoenbase.com.br',
            'flopesdegodoy@gmail.com':'enairalustosav@gmail.com',
            'tecnomaquinas@outlook.com.br': 'financeiro.tecno.agro@outlook.com'
            }

    colunas = ['codi_emp', 'razao_emp', 'email_emp']
    comando = f"""
        select
            codi_emp,
            razao_emp,
            email_emp

            FROM ccontrol_web.vw_empresa

            WHERE stat_emp <> 'I'
            AND prioridade_fiscal in('4','11', '12')
            AND dcad_emp < '{ano}-{int(mes) + 1 if mes != '12' else '01'}-01'

        """
    
    with conexao_db_ccw() as cursor:
        dados = buscar_dados_ccw(cursor, comando)
        clientes = crir_dicionario(dados, colunas)

    # buscas os emails na api
    headers = {
        'content-type': "application/json",
        'authorization': f"Bearer {os.environ.get('TOKEN_ADMIN')}"
    }
    response_emails = requests.get("http://api.c-controll.corp/api/v1/dn/core/emails_empresas", headers=headers)

    if response_emails.status_code == 200:
        emails = response_emails.json()['result']
        print(emails)
    lista_final = []

    for cliente in clientes:

        codi_emp = str(cliente['codi_emp'])
        razao_emp = str(cliente['razao_emp']).title()
        email = str(cliente['email_emp']).lower()
        

        #verifica se tem email no bitrix
        try:
            email_bx = emails[codi_emp]['EMAIL_PADRAO_COBRANCA']
            if email_bx:
                if "@g.us" not in email_bx:
                    email = str(email_bx).lower()
        except Exception as e:
            pass

        try:
            email_sub = str(substituto[email]).lower()
            email = email_sub
        except KeyError:
            pass

        lista_final.append({'nome':razao_emp, 'email': email, 'codi_emp': codi_emp})

    return {'result':lista_final}