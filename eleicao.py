class VotingSystem:
    def __init__(self):
        self.voters = set()
        self.votes = {}

    def vote(self, voter_id, candidate):
        if voter_id in self.voters:
            return "Erro: Eleitor já votou."

        self.voters.add(voter_id)
        if candidate in self.votes:
            self.votes[candidate] += 1
        else:
            self.votes[candidate] = 1

        return f"Voto registrado para {candidate}!"

    def show_results(self):
        if not self.votes:
            return "Nenhum voto registrado ainda."

        print("\n--- Resultado da Eleição ---")
        for candidate, count in sorted(self.votes.items(), key=lambda x: -x[1]):
            print(f"{candidate}: {count} votos")
        print("----------------------------")


if __name__ == "__main__":
    election = VotingSystem()

    print(election.vote("111", "Yasmim"))
    print(election.vote("222", "Lucas"))
    print(election.vote("111", "Yasmim"))
    print(election.vote("333", "Yasmim"))
    print(election.vote("444", "Lucas"))

    election.show_results()
