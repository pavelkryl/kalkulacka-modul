from dataclasses import dataclass


@dataclass
class StavKalkulacky:
    op1: float
    op2: float
    operace: str
    vysledek: float


def plus(stav: StavKalkulacky, a: float, b: float) -> None:
    stav.operace = "+"
    stav.op1 = a
    stav.op2 = b
    stav.vysledek = stav.op1 + stav.op2


def multi(stav: StavKalkulacky, a: float, b: float) -> None:
    stav.operace = "x"
    stav.op1 = a
    stav.op2 = b
    stav.vysledek = stav.op1 * stav.op2


def minus(stav: StavKalkulacky, a: float, b: float) -> None:
    stav.operace = "-"
    stav.op1 = a
    stav.op2 = b
    stav.vysledek = stav.op1 - stav.op2


def divide(stav: StavKalkulacky, a: float, b: float) -> None:
    stav.operace = "/"
    stav.op1 = a
    stav.op2 = b
    stav.vysledek = stav.op1 / stav.op2


def result(stav: StavKalkulacky) -> float:
    return stav.vysledek


def historie(stav: StavKalkulacky) -> str:
    return f"Poslední operace byla: {stav.op1} {stav.operace} {stav.op2} = {stav.vysledek}"
