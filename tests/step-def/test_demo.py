from pytest_bdd import scenarios, given, when, then

scenarios('../features')

@given('A demo step')
def demo_step():
    print('Running a demo step...')
    assert 1 ==1
