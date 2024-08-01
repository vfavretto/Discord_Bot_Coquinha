import discord
from discord.ext import commands

permissions = discord.Intents.default()
permissions.message_content = True
permissions.members = True
bot = commands.Bot(command_prefix=".", intents=permissions)


@bot.command()
async def ola(ctx: commands.Context):
    usuario = ctx.author
    await ctx.reply(f"Ola! {usuario.display_name}")


@bot.event
async def on_member_join(membro: discord.Member):
    canal = bot.get_channel(1268609670260719727)
    meu_embed = discord.Embed(title=f'Bem vindo, {membro.name}')
    meu_embed.description('Aproveite a coquinha gelada! tss aaaah')
    meu_embed.set_thumbnail(url=membro.avatar)

    await canal.send(embed=meu_embed)


@bot.command()
async def saudar(ctx: commands.Context):
    meu_embed = discord.Embed(title="Ola Mundo", description="Bom dia!")

    img_arquivo = discord.File('Discord_Bot_Coquinha/img/ckucas.jpg', 'ckucas.jpg')
    meu_embed.set_image(url="attachment://ckucas.jpg")

    thumb_arquivo = discord.File('Discord_Bot_Coquinha/img/gura.png', 'gura.png')
    meu_embed.set_thumbnail(url='attachment://gura.png')

    meu_embed.set_footer(text='Diga olá para o Ckucas!')

    meu_embed.color = discord.Color.pink()

    meu_embed.add_field(name='Filme Favorito', value='É o Fim!')
    meu_embed.add_field(name='Poder de Luta', value='?????')
    meu_embed.add_field(name='Rank', value='SSS+')
    # usar inline = false para quebrar linha nos campos

    await ctx.reply(files=[img_arquivo, thumb_arquivo], embed=meu_embed)

@bot.command()
async def botao(ctx: commands.Context):
    async def resposta(interact: discord.Interaction):
        await interact.response.send_message('Você apertou meu botão', ephemeral=True)

    view = discord.ui.View()
    botao = discord.ui.Button(label='Botão', style=discord.ButtonStyle.blurple)
    botao.callback = resposta()

    botao_url = discord.ui.Button(label='Meu Github', url='')

    view.add_item(botao)
    await ctx.reply(view=view)

@bot.event
async def on_ready():
    print("Estou pronto!")



bot.run("MTIyNjMxNjQ0MDQ5NjM3Mzc4MA.GPPsmk.mFrCNRubsTWrpQbupAsG9m-KUjig-C52VSh_qw")
