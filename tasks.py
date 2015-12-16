from invoke import task
import pytest

@task()
def clean():
    '''Clean build directory.'''
    print 'Cleaning build directory...'

@task
def build(clean=False):
    if clean:
        print("Cleaning!")
    print("Building!")

@task(clean, help={'name': "Name of the person to say hi to."})
def hi(name):
    print("Hi %s!" % name)

@task
def all():
    pytest.main()


@task
def unit():
    pytest.main('test/unit')
