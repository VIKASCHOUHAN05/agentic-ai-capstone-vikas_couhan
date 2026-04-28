def request_approval(amount):

    print(f"Approval required for refund: ${amount}")

    decision = input("Approve? (yes/no): ")

    return decision == "yes"