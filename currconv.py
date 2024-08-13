from forex_python.converter import CurrencyRates, RatesNotAvailableError

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        return converted_amount
    except RatesNotAvailableError:
        return f"Exchange rate not available for {from_currency} to {to_currency}."
    except ValueError:
        return "Invalid currency code. Please check the currency codes and try again."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to the Currency Converter!")
    
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency code you are converting from (e.g., USD, EUR): ").upper()
        to_currency = input("Enter the currency code you are converting to: ").upper()

        result = currency_converter(amount, from_currency, to_currency)
        
        if isinstance(result, float):
            print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
        else:
            print(result)
    
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

if __name__ == "__main__":
    main()
