import pytest
from com.gabriel.operacoes import operacoes

def test_soma():
  operacoes = Operacoes()
  assert operacoes.soma([1,5]) == 6, "Should be 6"
