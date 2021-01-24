Feature: ISBN Number validation validator

  Scenario Outline: Validating ISBN number
    Given we have an instance of ISBN and a ISBN number
    When isbn number equal to <isbn>
    Then validation result should be equal to <result>

    Examples:
      | isbn                    | result |
      | 978-3-16-148410-0       | True   |
      | 978-4-16-148410-0       | False  |
      | 978-2-1234-5680-3       | True   |
      | 113-1-4411-3333-0       | False  |
      | abcdef-ghijkf4          | False  |
      | 1234-5678               | False  |
      | test                    | False  |
