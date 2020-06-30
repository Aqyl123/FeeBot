import discord
import asyncio

token = 'YOUR BOT TOKEN'
client = discord.Client()

@client.event
async def on_ready():
	print('----------------------')
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('----------------------')

@client.event
async def on_message(message):
	if message.author.bot:
		return

	if message.content.startswith('!help'):
		embed = discord.Embed(title="Help", description="Use `!fees PRICE` to get started!", color=0x00FF00)
		embed.set_author(name="Fee Calculator", url="https://www.aqyl.xyz/", icon_url="https://i.dlpng.com/static/png/268736_preview.png")
		embed.set_thumbnail(url="https://catawba.edu/files/3715/3789/4354/calculator.png")
		await message.channel.send(embed=embed)

	if message.content.startswith('!'):
		cmd = message.content.split()[0].lower()[1:]
		args = message.content.split()[1:]
		price = float(' '.join(args))

		paypal = round((price * 0.029 + 0.30), 2)
		stockx = round((price * 0.095), 2)
		stockx2 = round((price * 0.09), 2)
		stockx3 = round((price * 0.085), 2)
		stockx4 = round((price * 0.08), 2)
		goatUS = round((price * 0.095 + 5), 2)
		goatCA = round((price * 0.095 + 20), 2)
		goatOT = round((price * 0.095 + 30), 2)
		ebay = round((price * 0.129 + 0.30), 2)
		mercari = round((price * 0.1), 2)
		bump = round((price * 0.089 + 0.30), 2)
		bumpI = round((price * 0.104 + 0.30), 2)
		grailed = round((price * 0.089 + 0.30), 2)
		grailedI = round((price * 0.104 + 0.30), 2)

		if cmd == "fees":
			embed = discord.Embed(title="Fee Calculator", color=0x00FF00)
			embed.set_author(name="Fee Calculator", url="https://www.aqyl.xyz/", icon_url="https://i.dlpng.com/static/png/268736_preview.png")
			embed.set_thumbnail(url="https://i.dlpng.com/static/png/268736_preview.png")
			embed.add_field(name="PayPal:", value="${}".format(paypal), inline=False)
			embed.add_field(name="StockX Level 1:", value="${}".format(stockx), inline=False)
			embed.add_field(name="StockX Level 2:", value="${}".format(stockx2), inline=False)
			embed.add_field(name="StockX Level 3:", value="${}".format(stockx3), inline=False)
			embed.add_field(name="StockX Level 4:", value="${}".format(stockx4), inline=False)
			embed.add_field(name="GOAT (US):", value="${}".format(goatUS), inline=False)
			embed.add_field(name="GOAT (CA):", value="${}".format(goatCA), inline=False)
			embed.add_field(name="GOAT (Other):", value="${}".format(goatOT), inline=False)
			embed.add_field(name="eBay:", value="${}".format(ebay), inline=False)
			embed.add_field(name="Mercari:", value="${}".format(mercari), inline=False)
			embed.add_field(name="BUMP:", value="${}".format(bump), inline=False)
			embed.add_field(name="BUMP (International):", value="${}".format(bumpI), inline=False)
			embed.add_field(name="Grailed:", value="${}".format(grailed), inline=False)
			embed.add_field(name="Grailed (International):", value="${}".format(grailedI), inline=False)
			await message.channel.send(embed=embed)

client.run(token)

