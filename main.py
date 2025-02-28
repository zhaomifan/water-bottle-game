from typing import List


class Bottle:
    no: int
    volume: int
    water: int

    def __init__(self, no: int, volume: int, water: int = 0):
        self.no = no
        self.volume = volume
        self.water = water

    def beauty_print(self):
        print(f"{self.no}号瓶({self.volume}升):{self.water}升")


def transfer_water(from_bottle: Bottle, to_bottle: Bottle) -> bool:
    # 参数校验
    if (to_bottle.volume - to_bottle.water) == 0 or from_bottle.water == 0:
        return False

    if (to_bottle.volume - to_bottle.water) >= from_bottle.water:
        to_bottle.water += from_bottle.water
        from_bottle.water = 0
    else:
        from_bottle.water -= (to_bottle.volume - to_bottle.water)
        to_bottle.water = to_bottle.volume

    return True


def is_game_over(bottles: List[Bottle], target_water: int):
    for bottle in bottles:
        if bottle.water == target_water:
            return True
    return False


def show_bottles(bottles: List[Bottle]):
    for bottle in bottles:
        bottle.beauty_print()


def validate_input(value: int, valid_values):
    if value not in valid_values:
        print(f"警告:非法的输入值{value}")
        return False
    return True


def validate_inputs(values: List[int], valid_values):
    for value in values:
        if not validate_input(value, valid_values):
            return False
    return True


if __name__ == "__main__":
    # 定义三个瓶子
    bottles = [Bottle(1, 8, 8), Bottle(2, 5), Bottle(3, 3)]
    target_water = 4
    bottle_nos = [bottle.no for bottle in bottles]
    while True:
        print("-------游戏目标:获得四升水-------")
        show_bottles(bottles)
        if is_game_over(bottles, target_water):
            break
        inputs = [int(input_str) for input_str in input("输入倒出水的瓶号,倒入水的瓶号,用逗号隔开:").split(",")]
        if not validate_inputs(inputs, bottle_nos):
            continue
        from_no = inputs[0]
        to_no = inputs[1]
        if not validate_input(to_no, bottle_nos):
            continue
        if not transfer_water(bottles[from_no - 1], bottles[to_no - 1]):
            print("提示:无效的操作")
    print("游戏胜利\n游戏结束")
