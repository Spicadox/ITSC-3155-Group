import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {
        "Pen": {"qnt": 10, "unit_price": 3.75, "discount": 5},
        "Notebook": {"qnt": 5, "unit_price": 7.5, "discount": 10},
        "Water Bottle": {"qnt": 0, "unit_price": 1.0, "discount": 7}
    }
    return products


@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


@pytest.fixture()
def item_Pen():
    item_Pen = "Pen"
    return item_Pen


@pytest.fixture()
def item_Water():
    item_Water = "Water Bottle"
    return item_Water


def test_CanCalucateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38


# TODO: Sam and Jinquan: Implement CheckInStock Test Case
def test_CanCheckInStock(invoice, products):
    invoice.checkInStock(products, 'Pen')
    assert invoice.checkInStock(products, 'Pen') == True
    assert invoice.checkInStock(products, 'Apple') == False
    assert invoice.checkInStock(products, 'Notebook') == True


# TODO: Ed and Tommy: Implement RemoveItem Test Case
def test_CanRemoveItem(invoice, products, item_Pen, item_Water):
    invoice.removeItem(products, item_Pen)
    invoice.removeItem(products, item_Water)
    assert invoice.removeItem(products, item_Pen) == {'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10},
                                                      'Water Bottle': {'qnt': 0, 'unit_price': 1.0, 'discount': 7}}
    assert invoice.removeItem(products, item_Water) == {"Pen": {"qnt": 10, "unit_price": 3.75, "discount": 5},
                                                        "Notebook": {"qnt": 5, "unit_price": 7.5, "discount": 10}}
