def test_ERC20(w3, HAY_token):
    a0, a1 = w3.eth.accounts[:2]
    assert HAY_token.name() == 'HAY Token'
    assert HAY_token.symbol() == 'HAY'
    assert HAY_token.decimals() == 18
    assert HAY_token.totalSupply() == 100000*10**18
    assert HAY_token.balanceOf(a0) == 100000*10**18
    HAY_token.transfer(a1, 1*10**18, transact={})
    assert HAY_token.balanceOf(a0) == 100000*10**18 - 1*10**18
    assert HAY_token.balanceOf(a1) == 1*10**18
