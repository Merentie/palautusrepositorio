from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def has_at_least(self, value, attribute):
        return QueryBuilder(And(self.query, HasAtLeast(value, attribute)))

    def plays_in(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def has_fewer_than(self, value, attribute):
        return QueryBuilder(And(self.query, HasFewerThan(value, attribute)))

    def one_of(self, q1, q2):
        return QueryBuilder(Or(q1,q2))

    def build(self):
        return self.query