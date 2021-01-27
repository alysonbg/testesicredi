class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        """
        Returns the top_n opened contracts.
        """
        top_debt_clients = [contract for contract in open_contracts if contract.id not in renegotiated_contracts]
        top_debt_clients.sort(reverse=True, key=lambda contract: contract.debt)
        top_debt_client_ids = [contract.id for contract in top_debt_clients]
        return top_debt_client_ids[:top_n]
