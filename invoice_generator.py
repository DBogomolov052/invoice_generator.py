from jinja2 import Template

def generate_invoice(invoice_template_file, company_info, client_info, items):
    # Загрузка шаблона счета
    with open(invoice_template_file) as f:
        template_str = f.read()
    template = Template(template_str)

    # Генерация счета
    invoice_data = {
        'company': company_info,
        'client': client_info,
        'items': items
    }
    invoice_str = template.render(invoice_data)

    # Сохранение счета в файл
    with open('invoice.pdf', 'wb') as f:
        f.write(pdfkit.from_string(invoice_str, False
