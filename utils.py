from collections import Counter

# 牌是否为“分”
def has_score(card):
    '''card: str'''
    return (('5' in card)  or ('0' in card) or ('K' in card))

# 判断是否为常规牌型
def is_normal(cards, level):
    '''cards: List[str], level: str'''

    mappings = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    if (len(cards)) < 1:
        return False
    # 单牌的情况
    if len(cards) == 1:
        return True
    # 对子的情况
    if len(cards) == 2:
        return cards[0] == cards[1]
    # 连对的情况
    if len(cards) > 2:
        if len(cards) % 2 != 0:
            return False
        # 级牌和大小王不参与构成拖拉机
        for card in cards:
            if (level in card) or ('jo' in card) or ('Jo' in card):
                return False
        # 拖拉机花色相等
        for card in cards:
            if card[0] != cards[0][0]:
                return False
        # 连对判断
        # 统计各个牌的数量
        card_numbers = [0 for i in range(15)]
        for card in cards:
            if card[1] not in mappings.keys():
                return False
            card_numbers[mappings[card[1]]] += 1
        if level not in mappings.keys():
            return False
        card_numbers.pop(mappings[level])
        
        # 判断连对
        is_start = 0
        while len(card_numbers) > 0:
            cur_num = card_numbers.pop(0)
            if cur_num not in [0, 2]:
                return False
            if (cur_num == 2) and (is_start == 0):
                is_start = 1
                continue
            if (cur_num == 0) and (is_start == 1):
                is_start = 2
                continue
            if (cur_num != 0) and (is_start > 1):
                return False
        if (is_start):
            return True
    return False
        
# 判断单张牌是大小王
def is_joker(card):
    return (card in ['jo', 'Jo'])

# 获取主花色
def get_major_suit(major):
    if isinstance(major, str):
        return major if major in 'dhcs' else None
    if (len(major) <= 2):
        return None
    suits = [s[0] for s in major]
    suits = Counter(suits)
    return max(suits.items(), key=lambda x: x[1])[0]

# 判断单张牌是主级牌
def is_major_level(card, major, level):
    major_suit = get_major_suit(major)
    if major_suit is None:
        return False
    
    return (major_suit + level == card)

# 判断单张牌是否级牌
def is_level(card, level):
    return (level in card)

# 判断单张牌是否主花色牌
def is_major_suit(card, major):
    major_suit = get_major_suit(major)
    return (major_suit in card)

# 判断单张牌card1是否比card2要大
def is_larger_single(card1, card2, major, level):

    mappings = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    if (card1 == card2):
        return False
    # 如果card2是大小王
    elif is_joker(card2):
        return False
    # 如果card2是主级牌
    elif is_major_level(card2, major, level):
        return is_joker(card1)
    # 如果card2是非主花色级牌
    elif (
        is_level(card2, level) and \
        not is_major_suit(card2, major)
    ):
        return (is_major_level(card1, major, level) or is_joker(card1))
    # 如果card2是非级牌主花色牌
    elif (
        is_major_suit(card2, major) and \
        not is_level(card2, level)
    ):
        # card1 是级牌/大小王
        if (
            is_level(card1, level) or \
            is_joker(card1)
        ):
            return True
        # card1是其他牌
        else:
            return (mappings[card1[1]] > mappings[card2[1]])
    # 如果card2是其他牌
    else:
        # card1 是级牌/大小王
        if (
            is_level(card1, level) or \
            is_joker(card1)
        ):
            return True
         # card1是非级牌主花色牌
        elif (
            is_major_suit(card1, major) and \
            not is_level(card1, level)
        ):
            return (mappings[card1[1]] >= mappings[card2[1]])
        # card1是其他牌
        else:
            return (mappings[card1[1]] > mappings[card2[1]])   

# 判断cards1是否比cards2要大
def is_larger(cards1, cards2, major, level):
    '''input should be list[str], list[str], list[str], level'''

    # 首先判断是否为常规牌型
    if not (is_normal(cards1, level) and is_normal(cards2, level)):
        return False
    
    # 判断长度是否相等
    if (len(cards1) != len(cards2)):
        return False
    # 单张或两张的情况
    if (len(cards1) <= 2):
        return is_larger_single(cards1[0], cards2[0], major, level)
    # 拖拉机的情况，寻找最小牌并比较
    min_cards1 = cards1[0]
    for card in cards1:
        if (is_larger_single(min_cards1, card, major, level)):
            min_cards1 = card
    min_cards2 = cards1[0]
    for card in cards2:
        if (is_larger_single(min_cards2, card, major, level)):
            min_cards2 = card
    return is_larger_single(min_cards1, min_cards2, major, level)

# 测试函数
def main():
    # 测试常规牌型
    # 单牌测试
    assert is_normal(['sA'], '2')
    assert is_normal(['h5'], '2')
    assert is_normal(['Jo'], '2')
    assert is_normal(['jo'], '2')

    # 对子测试
    assert is_normal(['s3', 's3'], '5')
    assert is_normal(['h4', 'h4'], '4')
    assert is_normal(['c6', 'd6'], '6') == False  # 非同花色
    assert is_normal(['c6', 'c7'], '6') == False  # 非同点数
    assert is_normal(['Jo', 'Jo'], '3')
    assert is_normal(['jo', 'jo'], '3')

    # 连对（拖拉机）测试
    assert is_normal(['s4', 's4', 's6', 's6'], '5')  # 连对：4466
    assert is_normal(['s4', 's4', 's5', 's5'], '5') == False  # 包含级牌
    assert is_normal(['h3', 'h3', 'h4', 'h4', 'h6', 'h6'], '5')  # 连对：334466
    assert is_normal(['c3', 'c3', 'c4', 'c4', 'c5', 'c5'], '5') == False  # 包含级牌
    assert is_normal(['d7', 'd7', 'd8', 'd8', 'd9', 'd9'], '5')
    assert is_normal(['s8', 's8', 's9', 's9', 's0', 's0'], 'J')  # 连对：889900
    assert is_normal(['hJ', 'hJ', 'hQ', 'hQ', 'hK', 'hK'], 'J') == False  # 包含级牌
    assert is_normal(['s2', 's2', 's3', 's3', 'Jo'], '4') == False  # 包含大王
    assert is_normal(['h4', 'h4', 'h5', 'h5', 'h6', 'h6'], '5') == False  # 包含级牌
    assert is_normal(['c2', 'c2', 'c3', 'c3', 'c4', 'c5'], '2') == False  # 不构成对子


    # 测试主花色
    assert get_major_suit(['jo', 'Jo']) is None
    assert get_major_suit(['d3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd0', 'dJ', 'dQ', 'dK', 'dA', 's2', 'h2', 'c2', 'd2', 'jo', 'Jo']) == 'd'

    # 测试主级牌
    assert is_major_level('c4', 
                          ['d3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd0', 'dJ', 'dQ', 'dK', 'dA', 's2', 'h2', 'c2', 'd2', 'jo', 'Jo'],
                          '4') == False
    assert is_major_level('d4', 
                          ['d3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd0', 'dJ', 'dQ', 'dK', 'dA', 's2', 'h2', 'c2', 'd2', 'jo', 'Jo'],
                          '4')
    assert is_major_level('d4', 
                          ['d3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd0', 'dJ', 'dQ', 'dK', 'dA', 's2', 'h2', 'c2', 'd2', 'jo', 'Jo'],
                          '5') == False
    assert is_major_level('Jo', 
                          ['d3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd0', 'dJ', 'dQ', 'dK', 'dA', 's2', 'h2', 'c2', 'd2', 'jo', 'Jo'],
                          '4') == False
    assert is_major_level('d4', ['jo', 'Jo'], '4') == False
if __name__ == '__main__':
    main()