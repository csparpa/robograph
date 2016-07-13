from robograph.datamodel.nodes.lib import apply


class Not(apply.Apply):
    """
    This node negates the truth value of the items of an argument sequence
    """
    def __init__(self, **args):
        apply.Apply.__init__(
            self,
            function=lambda predicates: map(lambda x: not x, predicates),
            argument=args.get('argument', None),
            name=args.get('name', None))


class And(apply.Apply):
    """
    This node performs a logical AND on the items of an argument sequence
    """
    def __init__(self, **args):
        apply.Apply.__init__(
            self,
            function=lambda predicates: reduce(lambda p1, p2: p1 and p2, predicates),
            argument=args.get('argument', None),
            name=args.get('name', None))


class Or(apply.Apply):
    """
    This node performs a logical OR on the items of an argument sequence
    """
    def __init__(self, **args):
        apply.Apply.__init__(
            self,
            function=lambda predicates: reduce(lambda p1, p2: p1 or p2, predicates),
            argument=args.get('argument', None),
            name=args.get('name', None))


class All(apply.Apply):
    """
    This node tells if all the items of the argument sequence have a truth value
    of true
    """
    def __init__(self, **args):
        apply.Apply.__init__(
            self,
            function=all,
            argument=args.get('argument', None),
            name=args.get('name', None))


class Nil(apply.Apply):
    """
    This node tells if all the items of the argument sequence have a truth value
    of false
    """
    def __init__(self, **args):
        apply.Apply.__init__(self,
                             function=lambda predicates: not any(predicates),
                             argument=args.get('argument', None),
                             name=args.get('name', None))


class Any(apply.Apply):
    """
    This node tells if at least one item in the argument sequence has a truth value
    of true
    """
    def __init__(self, **args):
        apply.Apply.__init__(
            self,
            function=any,
            argument=args.get('argument', None),
            name=args.get('name', None))
