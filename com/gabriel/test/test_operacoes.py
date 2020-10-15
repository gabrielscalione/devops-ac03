import pytest
from com.gabriel.operacoes import operacoes

def test_soma():
  operacoes = operacoes()
  assert operacoes.soma([1,5]) == 6, "Should be 6"
