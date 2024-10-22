from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.your-email-provider.com'  # Exemplo: smtp.gmail.com
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Seu e-mail
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Sua senha
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')  # E-mail do remetente
mail = Mail(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Aqui você pode processar os dados recebidos da Kirvano
    email_comprador = data.get('email')  # Supondo que o e-mail do comprador esteja aqui
    nome_comprador = data.get('nome')  # Supondo que o nome do comprador esteja aqui

    # Enviar e-mail
    if email_comprador:
        msg = Message('Obrigado pela sua compra!',
                      recipients=[email_comprador])
        msg.body = f'Olá {nome_comprador},\n\nObrigado pela sua compra! Seus detalhes foram processados com sucesso.'
        mail.send(msg)

    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
