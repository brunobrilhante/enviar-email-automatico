import smtplib
import email.message


def enviarEmail(resumo_loja, loja):
    server = smtplib.SMTP('smtp.gmail.com:587')
    corpo_email = f'<p>Prezados, </p> \
                  <p>Segue abaixo o e-email do relatório para a {loja}</p>  \
                  {resumo_loja.to_html()} \
                  Qualquer dúvida, estou à disposição'

    msg = email.message.Message()
    msg['Subject'] = f"Relatório - {loja}"

    # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
    # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
    # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
    # Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
    msg['From'] = 'seu_email@email.com'
    msg['To'] = 'destinatario@email.com'
    password = "sua_senha"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
