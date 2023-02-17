class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Check for edge cases
        if divisor == 0 or (dividend == -2147483648 and divisor == -1):
            return 2147483647
        
        # Determine sign of the quotient
        is_negative = (dividend < 0) != (divisor < 0)
        
        # Take absolute values of dividend and divisor
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize quotient and remainder
        quotient = 0
        
        # Bitwise division
        for i in range(31, -1, -1):
            if dividend >= (divisor << i):
                dividend -= (divisor << i)
                quotient |= (1 << i)
        
        # Apply sign to quotient
        if is_negative:
            quotient = -quotient
        
        # Check if quotient falls within the range of a 32-bit signed integer
        if quotient < -2147483648 or quotient > 2147483647:
            return 2147483647
        
        return quotient
