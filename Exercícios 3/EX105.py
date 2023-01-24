def notas(* nota, sit=False):
    """
    -> Cria um dicionário com informações sobre a turma
    :param nota: Notas dos alunos
    :param sit: True para incluir no dicionário a situação da turma
    :return: Dicionário com informações sobre a turma
    """

    turma = dict()

    turma['total'] = len(nota)
    turma['maior'] = max(nota)
    turma['menor'] = min(nota)
    turma['media'] = round(sum(nota) / len(nota), 1)

    if sit:
        if turma['media'] >= 9:
            turma['situacao'] = "Excelente"
        elif 9 > turma['media'] >= 8:
            turma['situacao'] = "Ótima"
        elif 8 > turma['media'] >= 6:
            turma['situacao'] = "Ok"
        elif 6 > turma['media'] >= 4:
            turma['situacao'] = "Ruim"
        else:
            turma['situacao'] = "Péssima"

    return turma


# Programa principal

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
