Feature: FizzBuzz game Functionality
  Scenario Outline: Numbers divisible only by 5
    Given we have an instance of FizzBuzz
    When the number is <number>
    Then returned string will be <result>
    Examples:
      | number | result |
      |      5 |   Buzz |
      |     10 |   Buzz |
      |     25 |   Buzz |

  Scenario Outline: Numbers divisible only by 3
    Given we have an instance of FizzBuzz
    When the number is <number>
    Then returned string will be <result>
    Examples:
      | number | result |
      |      3 |   Fizz |
      |      9 |   Fizz |
      |     27 |   Fizz |

  Scenario Outline: Numbers divisible by 15
    Given we have an instance of FizzBuzz
    When the number is <number>
    Then returned string will be <result>
    Examples:
      | number | result   |
      |     15 | FizzBuzz |
      |     30 | FizzBuzz |
      |     45 | FizzBuzz |

  Scenario Outline: Numbers divisible by 15 or only 3
    Given we have an instance of FizzBuzz
    When the number is <number>
    Then returned string will be <result>
    Examples:
      | number | result   |
      |     39 | Fizz     |
      |     90 | FizzBuzz |
      |     66 | Fizz     |

  Scenario Outline: Numbers not divisible by 3 and 5
    Given we have an instance of FizzBuzz
    When the number is <number>
    Then returned string will be <result>
    Examples:
      | number | result |
      |      4 | 4      |
      |     13 | 13     |
      |     77 | 77     |