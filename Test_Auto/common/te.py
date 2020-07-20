from common.new_res import API


a = API().api_method(method='post',url='http://game.test/game/staff/credits-game/game/list',parma="{'abc':'123'}")
print(a)
