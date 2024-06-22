import pytest

def prime(y):
    prime_list = []
    for i in range(0, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


def test_prime():
    assert len(prime(0))== 0

@pytest.mark.parametrize("num, res", [(3,2), (3,4)])
def test_prime2(num, res):
    assert prime(num)[0]==res

@pytest.mark.important
def test_prime3():
    assert prime(5)[0]==2