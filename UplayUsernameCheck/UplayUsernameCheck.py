import asyncio
import itertools as it
import r6sapi as api

async def run():
    auth = api.Auth("email", "password")

    mainstring = "abcdefghijklmnopqrstuvwxyz"
    secondstring = "abcdefghijklmnopqrstuvwxyz0123456789.-_"

    for i in mainstring:
      for j in secondstring:
        for k in secondstring:
          string = i + j + k
          checkxbox = 0
          checkpc = 0
          checkpsn = 0
          try:
            await auth.get_player(string, api.Platforms.UPLAY)
            checkpc = 1
          except:
            checkpc = 0

          try:
            await auth.get_player(string, api.Platforms.XBOX)
            checkxbox = 1
          except:
            checkxbox = 0

          try:
            await auth.get_player(string, api.Platforms.PLAYSTATION)
            checkpsn = 1
          except:
            checkpsn = 0

          finally:
            if (checkxbox == 0 and checkpsn == 0 and checkxbox == 0):
              print(string)
    
asyncio.get_event_loop().run_until_complete(run())
