from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/telefone', methods=['GET'])
def telefone():
    lista_ddd={'11':'São Paulo', '12':'São Paulo', '13':'São Paulo', '14':'São Paulo', '15':'São Paulo', '16':'São Paulo', '17':'São Paulo', '18':'São Paulo', '19':'São Paulo', '21':'Rio de Janeiro', '22':'Rio de Janeiro', '24':'Rio de Janeiro', '27':'Espírito Santo', '28':'Espírito Santo', '31':'Minas Gerais', '32':'Minas Gerais', '33':'Minas Gerais', '34':'Minas Gerais', '35':'Minas Gerais', '37':'Minas Gerais', '38':'Minas Gerais', '41':'Paraná', '42':'Paraná', '43':'Paraná', '44':'Paraná', '45':'Paraná', '46':'Paraná', '47':'Santa Catarina', '48':'Santa Catarina', '49':'Santa Catarina', '51':'Rio Grande do Sul', '53':'Rio Grande do Sul', '54':'Rio Grande do Sul', '55':'Rio Grande do Sul', '61':'Distrito Federal/Goiás', '62':'Goiás', '63':'Tocantins', '64':'Goiás', '65':'Mato Grosso', '66':'Mato Grosso', '67':'Mato Grosso do Sul', '68':'Acre', '69':'Rondônia', '71':'Bahia', '73':'Bahia', '74':'Bahia', '75':'Bahia', '77':'Bahia', '79':'Sergipe', '81':'Pernambuco', '82':'Alagoas', '83':'Paraíba', '84':'Rio Grande do Norte', '85':'Ceará', '86':'Piauí', '87':'Pernambuco', '88':'Ceará', '89':'Piauí', '91':'Pará', '92':'Amazonas', '93':'Pará', '94':'Pará', '95':'Roraima', '96':'Amapá', '97':'Amazonas', '98':'Maranhão', '99':'Maranhão'}
    if len(request.args.keys())==2:
        ddd=request.args['ddd']
        telefone=request.args['telefone']
        lista_erros=[]
        if not len(ddd)==2 or ddd not in lista_ddd.keys() or len(telefone) < 8 or len(telefone) > 9 or (len(telefone) == 9 and not telefone[0] == '9'):
            if not len(ddd)==2:
                lista_erros.append('DDD precisa ter exatamente 2 dígitos')
            elif ddd not in lista_ddd.keys():
                lista_erros.append('DDD não pertence a nenhum Estado')
            if len(telefone) < 8:
                lista_erros.append('Telefone precisa ter pelo menos 8 dígitos')
            if len(telefone) > 9:
                lista_erros.append('Telefone precisa ter no máximo 9 dígitos')
            if len(telefone) == 9 and not telefone[0] == '9':
                lista_erros.append('Telefones com 9 digitos devem começar com o número 9')
            return render_template('index.html',lista_erros=lista_erros,ddd=ddd,telefone=telefone)
        if len(telefone)==8:
            telefone=telefone[:4]+'-'+telefone[4:]
        elif len(telefone)==9:
            telefone=telefone[:5]+'-'+telefone[5:]
        return render_template('telefone.html', 
                               telefone='('+ddd+') '+telefone,estado=lista_ddd[ddd])
    return render_template('index.html')

@app.route('/regressiva', methods=['GET'])
def regressiva():
    if len(request.args.keys())==1:
        erro=''
        inicial=request.args['inicial']
        if inicial=='':
            erro='Número não pode ser vazio'
            return render_template('form_regressiva.html',erro=erro,inicial=inicial)
        else:
            try:
                inicial=int(inicial)
            except:
                erro='Número não pode ser vazio'
                return render_template('form_regressiva.html',erro=erro,inicial=inicial)
            if inicial<0:
                erro='Número não pode ser menor que 0'
                return render_template('form_regressiva.html',erro=erro,inicial=inicial)
        contagem_regressiva=[]
        for i in range(inicial, -1, -1):
            contagem_regressiva.append(i)
        return render_template('regressiva.html',contagem_regressiva=contagem_regressiva,inicial=inicial)


    return render_template('form_regressiva.html',erro='')
    
@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
