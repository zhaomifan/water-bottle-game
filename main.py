from typing import List


class Bottle:
    name: int
    volume: int
    water: int

    def __init__(self, volume: int, water: int = 0):
        # self.no = no
        self.volume = volume
        self.water = water

    def beauty_print(self):
        print(f"{self.volume}升({self.water}升)")

        b_str = ""
        for i in range(self.volume):
            b_str += "水" if i < self.water else "空"
        print(f"|{b_str}|\n")


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


def is_game_over(bottles: List[Bottle], targetWater: int):
    for bottle in bottles:
        if bottle.water == targetWater:
            return True
    return False


def show_bottles(bottles: List[Bottle]):
    for bottle in bottles:
        bottle.beauty_print()


if __name__ == "__main__":
    # 定义三个瓶子
    bottles = [Bottle(12, 12), Bottle(8), Bottle(5)]
    target_water = 6
    print("游戏开始")
    while True:
        print("》》》》》》XXXXXXX《《《《《《《")
        show_bottles(bottles)
        if is_game_over(bottles, target_water):
            print("胜利")
            break
        print("请输入要倒出水的瓶号")
        from_no = int(input()) - 1
        print("请输入要倒入水的瓶号")
        to_no = int(input()) - 1
        if not transfer_water(bottles[from_no], bottles[to_no]):
            print("提示:无效的操作")
    print("游戏结束")
