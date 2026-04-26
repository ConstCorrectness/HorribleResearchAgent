import asyncio
import argparse






async def main():
    print(f'hello from main()')

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

def run():
    asyncio.run(main())

if __name__ == '__main__':
    run()