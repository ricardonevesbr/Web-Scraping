import builtwith
import whois

builtwith.parse('https://www.aprendapowerbi.com.br/')

builtwith.parse('https://www.facebook.com', headers=None, html=None, user_agent='builtwith')

print(whois.whois('aprendapowerbi.com.br'))