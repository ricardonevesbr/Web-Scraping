from scrapy import Selector
from urllib.request import urlopen

html = """
<html>
	<head>
		<title>Aula Python Web Scraping</title>
	</head>
	<body>
		<h1>Curso Python Web Scraping</h1>

		<form action="formulario_pythonwebscraping1.php" method="POST">
			Informe os dados abaixo:<br><br>
			<table>
				<tr>
					<td>Nome:</td>
					<td><input type="text" name="nome" size="50" maxlength="100"></input></td>
				</tr>
				<tr>
					<td>E-mail:</td>
					<td><input id="email" type="text" name="email" size="50" maxlength="100"></input></td>
				</tr>
				<tr>
					<td>Celular:</td>
					<td><input type="text" name="celular" size="20" maxlength="14"></input></td>
				</tr>
				<tr>
					<td><input type="submit" name="enviar" value="Enviar dados"></td>
				</tr>
			</table>
		</form>
	</body>
</html>
"""

sel = Selector(text=html)
lista = sel.css('input::attr(id)')
for x in lista:
    print(x)
