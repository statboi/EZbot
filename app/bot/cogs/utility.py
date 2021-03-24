import discord
from discord.ext import commands
import json

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def user(self, ctx, member : discord.Member):
        with open(r"cogs\features.json", "r") as fe:
            if json.load(fe)["user"]=="1":
                with open("config.json") as f:
                    data = json.load(f)
                    for p in data["config"]:
                        bot_author = p["authorName"]
                        if isinstance(ctx.channel, discord.channel.DMChannel):
                            await ctx.send('This command is only available on guilds')
                        else:
                            embed=discord.Embed(title=f"Info about {member.name}", color=0x2efcff)
                            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                            embed.set_thumbnail(url=member.avatar_url)
                            embed.add_field(name=f"Roles on {ctx.guild.name}:", value=len(member.roles)-1, inline=False)
                            embed.add_field(name="Created at:", value=round(member.created_at), inline=False)
                            embed.add_field(name=f"Joined at {ctx.guild.name} on:", value=round(member.joined_at), inline=False)
                            embed.set_footer(text=f"Bot made by {bot_author}\nPowered by EZbot - https://github.com/statboi/EZbot")
                            await ctx.send(embed=embed)
            else: return

def setup(bot):
    bot.add_cog(Utility(bot))
