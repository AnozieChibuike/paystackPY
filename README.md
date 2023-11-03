[![PyPI Version](https://img.shields.io/pypi/v/paystackPY.svg)](https://pypi.org/project/paystackPY/)
[![Python Versions](https://img.shields.io/pypi/pyversions/paystackPY.svg)](https://pypi.org/project/paystackPY/)
[![License](https://img.shields.io/pypi/l/paystackPY.svg)](https://github.com/AnozieChibuike/paystackPY/blob/master/LICENSE)

A Python package that creates a typewriter effect for text output.

## Installation

You can install this package using `pip`:

```bash
pip install paystackPY 
```

Usage
-----

```python
from paystackPY import Paystack

paystack = Paystack(api_key=<Your paystack api key>)
reference = <Your custom reference>
pay = paystack.initializeTransaction(email, amount, reference=reference, callback_url=<your callback url>) 
# The above will return a dictionary which you can access
ref = paystack.verifyTransaction(reference)
# The above will return a dictionary which you can access
```
Contributing
------------

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and test them thoroughly.
4.  Create a pull request with a clear description of your changes.

License
-------

This project is licensed under the MIT License - see the [LICENSE](https://mit-license.org/) file for details.

Acknowledgments
---------------

-   Inspired by the openai package in Python.

Contact
-------

-   Anozie Joel
-   Email: chibuikeanozie0@gmail.com
-   GitHub: [Anozie Chibuike](https://github.com/AnozieChibuike)