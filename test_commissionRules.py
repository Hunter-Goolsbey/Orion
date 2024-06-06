from .commissionRules import commissionRules
#import unittest

def test_getAddCommissionRules():
    flint = commissionRules()
    flint.add("q")
    assert flint.getCommissionRules() == ["q"]