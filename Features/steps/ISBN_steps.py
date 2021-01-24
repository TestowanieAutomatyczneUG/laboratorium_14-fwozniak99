from behave import *
from src.sample.ISBN import ISBN

use_step_matcher("re")


@given("we have an instance of ISBN and a ISBN number")
def step_impl(context):
    context.isbn = ISBN()


@when("isbn number equal to (?P<isbn>.+)")
def step_impl(context, isbn):
    context.result = context.isbn.validate(isbn)


@then("validation result should be equal to (?P<result>.+)")
def step_impl(context, result):
    assert context.result == eval(result)
