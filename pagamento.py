from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os
import logging
from random import choice
import string

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Exemplo: smtp.gmail.com
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Seu e-mail
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Sua senha de aplicativo
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')  # E-mail do remetente
mail = Mail(app)

# Configuração de logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return "Webhook is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    logging.info(f'Recebido dados: {data}')  # Log dos dados recebidos
    
    # Aqui você pode processar os dados recebidos da Kirvano
    email_comprador = data.get('customer', {}).get('email')  # Acessando o e-mail do comprador
    nome_comprador = data.get('customer', {}).get('name')  # Acessando o nome do comprador

    senha = ''
    for i in range(14):
        senha += choice(string.ascii_letters + string.digits + string.punctuation)
        
    # Validação básica
    if not email_comprador or not nome_comprador:
        logging.warning('Dados incompletos recebidos.')  # Log de aviso
        return jsonify({'status': 'error', 'message': 'Dados incompletos'}), 400

    # Enviar e-mail
    try:
        msg = Message('Obrigado pela sua compra!',
                      recipients=[email_comprador])
        msg.html = f"""
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
        <head>
          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <meta name="x-apple-disable-message-reformatting">
          <meta http-equiv="X-UA-Compatible" content="IE=edge">
          <title></title>
          <style type="text/css">
            @media only screen and (min-width: 520px) {{
              .u-row {{
                width: 500px !important;
              }}
              .u-row .u-col {{
                vertical-align: top;
              }}
              .u-row .u-col-33p33 {{
                width: 166.65px !important;
              }}
              .u-row .u-col-50 {{
                width: 250px !important;
              }}
              .u-row .u-col-100 {{
                width: 500px !important;
              }}
            }}
            @media only screen and (max-width: 520px) {{
              .u-row-container {{
                max-width: 100% !important;
                padding-left: 0px !important;
                padding-right: 0px !important;
              }}
              .u-row {{
                width: 100% !important;
              }}
              .u-row .u-col {{
                display: block !important;
                width: 100% !important;
                min-width: 320px !important;
                max-width: 100% !important;
              }}
              .u-row .u-col > div {{
                margin: 0 auto;
              }}
              .u-row .u-col img {{
                max-width: 100% !important;
              }}
            }}
            body{{margin:0;padding:0}}
            table,td,tr{{border-collapse:collapse;vertical-align:top}}
            p{{margin:0}}
            .ie-container table,.mso-container table{{table-layout:fixed}}
            *{{line-height:inherit}}
            a[x-apple-data-detectors=true]{{color:inherit!important;text-decoration:none!important}}
            table, td {{ color: #000000; }} #u_body a {{ color: #0000ee; text-decoration: underline; }}
          </style>
        </head>
        <body class="clean-body u_body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #F7F8F9;color: #000000">
          <table id="u_body" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #F7F8F9;width:100%" cellpadding="0" cellspacing="0">
            <tbody>
              <tr style="vertical-align: top">
                <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
                  <div class="u-row-container" style="padding: 0px;background-color: transparent">
                    <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                      <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                        <div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
                          <div style="height: 100%;width: 100% !important;border-radius: 0px;">
                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                              <tbody>
                                <tr>
                                  <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
                                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                      <tr>
                                        <td style="padding-right: 0px;padding-left: 0px;" align="center">

<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
 width="200.000000pt" height="200.000000pt" viewBox="0 0 200.000000 200.000000"
 preserveAspectRatio="xMidYMid meet">

<g transform="translate(0.000000,200.000000) scale(0.100000,-0.100000)"
fill="#1D5796" stroke="none">
<path d="M0 1000 l0 -1000 1000 0 1000 0 0 1000 0 1000 -1000 0 -1000 0 0
-1000z m1220 545 l57 -57 -96 -93 -96 -94 96 -98 c103 -105 119 -127 119 -168
0 -40 -15 -63 -103 -152 l-81 -83 37 -38 37 -38 -88 -87 c-97 -97 -133 -113
-190 -84 -30 14 -30 14 -84 -40 -29 -30 -65 -61 -80 -69 -35 -18 -82 -18 -116
0 -29 16 -429 415 -456 456 -9 13 -16 42 -16 64 0 39 7 47 268 309 154 155
281 275 301 284 47 20 86 8 143 -45 l49 -46 67 66 c77 75 83 79 136 73 31 -3
50 -15 96 -60z m417 -297 c192 -193 203 -206 203 -241 0 -21 -6 -50 -14 -65
-25 -47 -528 -540 -559 -547 -51 -13 -89 3 -149 62 l-57 56 37 27 c51 37 335
336 345 363 19 51 1 78 -148 227 l-145 145 73 73 c95 98 122 114 172 108 35
-4 58 -23 242 -208z"/>
<path d="M712 1257 l-202 -204 0 -53 0 -53 185 -186 184 -186 113 112 112 112
-101 104 c-146 150 -147 176 -13 308 44 44 80 83 80 87 0 4 -35 42 -78 85
l-78 77 -202 -203z"/>
</g>
</svg>
                                        </td>
                                      </tr>
                                    </table>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                              <tbody>
                                <tr>
                                  <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
                                    <h1 style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-size: 25px; font-weight: 700;">
                                      <span>Obrigado pela compra!</span>
                                    </h1>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                              <tbody>
                                <tr>
                                  <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
                                    <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
                                      <p style="line-height: 140%; text-align: center;">🚀 Um pequeno clique para você mas um grande passo para seu negócio!</p>
                                    </div>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                              <tbody>
                                <tr>
                                  <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
                                    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                      <tbody>
                                        <tr style="vertical-align: top">
                                          <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                            <span>&#160;</span>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="u-row-container" style="padding: 0px;background-color: transparent">
                      <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                        <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                          <div class="u-col u-col-50" style="max-width: 320px;min-width: 250px;display: table-cell;vertical-align: top;">
                            <div style="height: 100%;width: 100% !important;border-radius: 0px;">
                              <div style="box-sizing: border-box; height: 100%; padding: 0px;">
                                <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                  <tbody>
                                    <tr>
                                      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
                                        <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
                                          <p style="line-height: 140%;">Suas credenciais de acesso ao <strong>Sistema Forteplus</strong>:</p>
                                          <ul>
                                            <li style="line-height: 19.6px;">Email:{email_comprador}</li>
                                            <li style="line-height: 19.6px;">Senha:{senha}</li>
                                          </ul>
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                                <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                  <tbody>
                                    <tr>
                                      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
                                        <div align="left">
                                          <a href="app.forteplus.com.br" target="_blank" class="v-button" style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #0068a5; border-radius: 4px;width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 14px;">
                                            <span style="display:block;padding:10px 20px;line-height:120%;"><span style="font-size: 14px; line-height: 16.8px;">Acessar Forteplus</span></span>
                                          </a>
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </div>
                            </div>
                          </div>
                          <div class="u-col u-col-50" style="max-width: 320px;min-width: 250px;display: table-cell;vertical-align: top;">
                            <div style="height: 100%;width: 100% !important;border-radius: 0px;">
                              <div style="box-sizing: border-box; height: 100%; padding: 0px;">
                                <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                  <tbody>
                                    <tr>
                                      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
                                        <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
                                          <p style="line-height: 140%;">Suas credenciais para acesso ao mini curso na <strong>Kirvano:</strong></p>
                                          <ul>
                                            <li style="line-height: 19.6px;">Email:{email_comprador}</li>
                                            <li style="line-height: 19.6px;">Senha: Crie sua senha pelo email recebido</li>
                                          </ul>
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                                <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                  <tbody>
                                    <tr>
                                      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
                                        <div align="left">
                                          <a href="https://app.kirvano.com/" target="_blank" class="v-button" style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #161616; border-radius: 4px;width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 14px;">
                                            <span style="display:block;padding:10px 20px;line-height:120%;"><span style="font-size: 14px; line-height: 16.8px;">Acessar Kirvano</span></span>
                                          </a>
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="u-row-container" style="padding: 0px;background-color: transparent">
                      <div class="u-row" style="margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                        <div style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">
                          <div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
                            <div style="height: 100%;width: 100% !important;border-radius: 0px;">
                              <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                <tbody>
                                  <tr>
                                    <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">
                                      <div style="font-size: 14px; line-height: 140%; text-align: left; word-wrap: break-word;">
                                        <p style="line-height: 140%;"><span style="font-size: 12px; line-height: 16.8px;">Dúvidas entre em contato através do suporte por telefone:<strong> (31) 3582-1410</strong></span></p>
                                        <p style="line-height: 140%;"><span style="font-size: 12px; line-height: 16.8px;">© 2024 Forteplus Sistemas - Todos os direitos reservados.</span></p>
                                      </div>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </body>
        </html>
        """
        mail.send(msg)
        logging.info(f'E-mail enviado para: {email_comprador}')  # Log de sucesso
    except Exception as e:
        logging.error(f'Erro ao enviar e-mail: {str(e)}')  # Log de erro
        return jsonify({'status': 'error', 'message': str(e)}), 500

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
