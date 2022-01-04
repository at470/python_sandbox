# Write code that asks a user to input a monetary value (USD). You can assume the user will input an integer or float with no special characters.
# Return a print statement using string formatting that states the value converted to Euros (EUR), Japanese Yen (JPY), and Mexican Pesos (MXN). Your new values should be rounded to the nearest hundredth.
#
#
# Hint: To match the exact values from the example, you can use currency conversion ratios from the time of publication. As of July 6, 2021, $1 USD is equivalent to 0.85 EUR, 110.63 JPY, and 20.02 MXN.


def usd_converter(usd):
    eur = usd * 0.85
    jpy = usd * 110.63
    mxn = usd * 20.02
    txt = "{} USD = {:.2f} EUR = {:.2f} JPY = {:.2f} MXN."
    print(txt.format(usd, eur, jpy, mxn))



usd_converter(189)

usd_converter(17.82)
