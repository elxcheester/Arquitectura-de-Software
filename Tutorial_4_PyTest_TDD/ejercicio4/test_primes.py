from primes import is_prime


def test_prime_number():
    assert is_prime(1) == False

 def test_prime_other_number():
    assert is_prime(15) == False