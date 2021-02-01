def leap_year(year: int) -> bool:
    return True if (year%4==0 and not year%100==0) or year%400==0 else False

