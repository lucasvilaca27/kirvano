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
        semja += choice(14)
        
    # Validação básica
    if not email_comprador or not nome_comprador:
        logging.warning('Dados incompletos recebidos.')  # Log de aviso
        return jsonify({'status': 'error', 'message': 'Dados incompletos'}), 400

    # Enviar e-mail
    try:
        msg = Message('Obrigado pela sua compra!',
                      recipients=[email_comprador])
        msg.body = f'Olá {nome_comprador},\n\nObrigado pela sua compra! Seus detalhes foram processados com sucesso. \nSeus dados de acesso: \nemail: {email_comprador}\nsenha: {senha}'
        mail.send(msg)
        logging.info(f'E-mail enviado para: {email_comprador}')  # Log de sucesso
    except Exception as e:
        logging.error(f'Erro ao enviar e-mail: {str(e)}')  # Log de erro
        return jsonify({'status': 'error', 'message': str(e)}), 500

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
