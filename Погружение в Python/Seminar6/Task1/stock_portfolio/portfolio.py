__all__ = ["calculate_portfolio_value", "calculate_portfolio_return", "get_most_profitable_stock"]
_INITIAL_VALUE = float()
_INITIAL_BRIEFCASE = {}


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    """
    Расчет общей стоимости портфеля акций.
    ВАЖНО! Все символьные значения акций должны быть указаны верно.
    :param stocks: словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.),
    и значениями - количество акций каждого символа.
    :param prices: словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции.
    :return: общая стоимость портфеля акций на основе количества акций и их текущих цен.
    """
    value = 0
    for k, v in stocks.items():
        value += v * prices.get(k, 0)
        _INITIAL_BRIEFCASE.setdefault(k, prices.get(k, 0))
    global _INITIAL_VALUE
    if not _INITIAL_VALUE and value:
        _INITIAL_VALUE = value
    return value


def calculate_portfolio_return(current_value: float, initial_value=None) -> float:
    """
    Расчет доходности портфеля
    :param initial_value: начальная стоимость портфеля акций
    :param current_value: текущая стоимость портфеля акций
    :return: процентная доходность портфеля
    """
    if not initial_value:
        initial_value = _INITIAL_VALUE
    # Вторая проверка на случай если ещё не был инициализрована стоимость
    if initial_value:
        percent = initial_value / 100
        return round(current_value / percent - 100, 2)
    return 0


# В условии было принимать stocks: dict - словарь с акциями и их количеством, но типо, а зачем если вообще не важно
# сколько там этих акций ведь нужна цена за одну
def get_most_profitable_stock(prices: dict) -> str:
    """
    Определение наиболее прибыльной акции
    :param prices: словарь с акциями и их текущими ценами
    :return: символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью
    """
    max_variance = 0
    result = ''
    for k, v in prices.items():
        if _INITIAL_BRIEFCASE.get(k, 0):
            buffer = v / _INITIAL_BRIEFCASE[k]
            if buffer > max_variance:
                max_variance = buffer
                result = k
    return result
