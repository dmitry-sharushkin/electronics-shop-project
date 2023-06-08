from src.phone import Phone


def test_phone_number_of_sim():
    phone = Phone('iPhone', 1000, 10, 1)
    assert phone.number_of_sim == 1

    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

    try:
        phone.number_of_sim = 0
    except ValueError as e:
        assert str(e) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'

    try:
        phone.number_of_sim = 1.5
    except ValueError as e:
        assert str(e) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'

    try:
        phone.number_of_sim = -1
    except ValueError as e:
        assert str(e) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
