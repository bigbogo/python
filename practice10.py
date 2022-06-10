# 모듈
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_mornings(4) # 4명이서 조조 할인 영화 보러갔을때
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price_soldier(3)
# mv.price_mornings(5)
# mv.price(3)

# from theater_module import *
# # from random import *
# price(3)
# price_mornings(4)
# price_soldier(5)

# from theater_module import price, price_mornings
# price(5)
# price_mornings(4)
# price_soldier(3)

from theater_module import price_soldier as price
price(3)