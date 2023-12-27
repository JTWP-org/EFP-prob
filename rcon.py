import asyncio
import sys
from pavlov import PavlovRCON

async def main():

    if len(sys.argv) < 2:
        print("Usage: python script.py <your_argument>")
        return
    

    ARG = sys.argv[1]

    pavlov = PavlovRCON("127.0.0.1", 9000, "HNXb7PVs4CFni2goxcDFswh1xge5cvl")
    data = await pavlov.send(ARG)
    print(data)

asyncio.run(main())
