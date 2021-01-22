from behave import *
from sample.fizzbuzz import FizzBuzz

use_step_matcher("re")


@given("we have an instance of FizzBuzz")
def step_impl(context):
    context.fizzbuzz = FizzBuzz()


@when("the number is (?P<number>.+)")
def step_impl(context, number):
    context.result = context.fizzbuzz.game(int(number))


@then("returned string will be (?P<result>.+)")
def step_impl(context, result):
    assert context.result == result

