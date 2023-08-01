import asyncio
from time import sleep
from iol_client import IOLClient
from iol_client.constants import Mercado, Plazo
from iol_sheets import SheetClient
from iol_sheets.constants import Scope
import os


async def run_app():
    print("Hello World!")

    iol_client = IOLClient(
        username=os.getenv("IOL_USER") or "", password=os.getenv("IOL_PASS") or ""
    )
    iol_sheet = SheetClient(
        spreadsheet_id=os.getenv("SPREADSHEET_ID") or "",
        credentials_file=os.getenv("CREDENTIALS_FILE_JSON") or "",
        scopes=[Scope.WRITEABLE],
        iol_api=iol_client,
    )

    print("Starting...")
    for _ in range(4):
        await iol_sheet.append_cotizacion_titulo(
            simbolo="GGAL", mercado=Mercado.BCBA, plazo=Plazo.T0
        )
        await iol_sheet.append_cotizacion_titulo(
            simbolo="GGAL", mercado=Mercado.BCBA, plazo=Plazo.T1
        )
        await iol_sheet.append_cotizacion_titulo(
            simbolo="GGAL", mercado=Mercado.BCBA, plazo=Plazo.T2
        )
        sleep(900)
    print("Done!")


def main():
    asyncio.run(run_app())


if __name__ == "__main__":
    main()
