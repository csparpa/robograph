from datamodel.nodes import apply


class Not(apply.ApplyStatic):
    def __init__(self, name=None):
        apply.ApplyStatic.__init__(
            self,
            lambda predicate: not predicate,
            name=name)


class And(apply.ApplyStatic):
    def __init__(self, name=None):
        apply.ApplyStatic.__init__(
            self,
            lambda predicates: reduce(lambda p1, p2: p1 and p2, predicates),
            name=name)


class Or(apply.ApplyStatic):
    def __init__(self, name=None):
        apply.ApplyStatic.__init__(
            self,
            lambda predicates: reduce(lambda p1, p2: p1 or p2, predicates),
            name=name)


class All(apply.ApplyStatic):
    def __init__(self, name=None):
        apply.ApplyStatic.__init__(self, all, name=name)


class Nil(apply.ApplyStatic):
    def __init__(self, name=None):
        apply.ApplyStatic.__init__(self, lambda predicates: not any(predicates),
                                   name=name)


class Any(apply.ApplyStatic):
    def __init__(self, name=None):
        apply.ApplyStatic.__init__(self, any, name=name)
