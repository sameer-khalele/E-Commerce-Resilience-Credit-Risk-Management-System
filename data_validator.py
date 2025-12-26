def validate_customer_data(data):
    """
    Validates incoming customer data before it reaches the Credit Model.
    This acts as a mitigation control against data corruption.
    """
    # Check if 'income' field exists (Prevents the 'field name change' risk)
    if 'income' not in data:
        return False, "Error: Missing 'income' field. Potential schema mismatch."

    # Check if income value is logical (Prevents the 'zero income' bug)
    if data['income'] <= 0:
        return False, "Error: Income must be greater than zero. Data integrity issue detected."

    return True, "Data is valid."

# Example of a failed test case (Simulating the risk we discussed)
sample_data = {"customer_id": 101, "salary": 5000} # Developer changed 'income' to 'salary'
is_valid, message = validate_customer_data(sample_data)

print(f"Validation Result: {is_valid} | Message: {message}")
