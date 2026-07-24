"""Exact finite-graph hygiene for Vizing-domination work.

This module is deliberately small and brute-force. It is a verifier for examples
and definitions, not an attack on Vizing's conjecture.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from typing import Iterable, Iterator, Sequence


@dataclass(frozen=True)
class Graph:
    """A loopless undirected graph on vertices ``range(n)``."""

    n: int
    edges: frozenset[tuple[int, int]]

    def __post_init__(self) -> None:
        normalized: set[tuple[int, int]] = set()
        for u, v in self.edges:
            if not (0 <= u < self.n and 0 <= v < self.n):
                raise ValueError(f"edge {(u, v)} is outside range({self.n})")
            if u == v:
                raise ValueError("graphs must be loopless")
            normalized.add((min(u, v), max(u, v)))
        object.__setattr__(self, "edges", frozenset(normalized))

    @classmethod
    def from_edges(cls, n: int, edges: Iterable[tuple[int, int]]) -> "Graph":
        return cls(n, frozenset(edges))

    def closed_neighborhood(self, v: int) -> frozenset[int]:
        if not 0 <= v < self.n:
            raise IndexError(v)
        answer = {v}
        for a, b in self.edges:
            if a == v:
                answer.add(b)
            elif b == v:
                answer.add(a)
        return frozenset(answer)

    def dominates(self, chosen: Iterable[int], target: Iterable[int] | None = None) -> bool:
        chosen_set = frozenset(chosen)
        if not chosen_set <= frozenset(range(self.n)):
            raise ValueError("chosen set contains an invalid vertex")
        target_set = frozenset(range(self.n)) if target is None else frozenset(target)
        return all(self.closed_neighborhood(v) & chosen_set for v in target_set)

    def domination_number(self, target: Iterable[int] | None = None) -> int:
        target_set = frozenset(range(self.n)) if target is None else frozenset(target)
        if not target_set <= frozenset(range(self.n)):
            raise ValueError("target contains an invalid vertex")
        for size in range(self.n + 1):
            if any(self.dominates(chosen, target_set) for chosen in combinations(range(self.n), size)):
                return size
        raise AssertionError("the full vertex set always dominates")

    def cartesian_product(self, other: "Graph") -> "Graph":
        def vertex(g: int, h: int) -> int:
            return g * other.n + h

        edges: set[tuple[int, int]] = set()
        for g1, g2 in self.edges:
            for h in range(other.n):
                edges.add((vertex(g1, h), vertex(g2, h)))
        for h1, h2 in other.edges:
            for g in range(self.n):
                edges.add((vertex(g, h1), vertex(g, h2)))
        return Graph.from_edges(self.n * other.n, edges)

    def is_two_packing(self, chosen: Iterable[int]) -> bool:
        chosen_tuple = tuple(chosen)
        return all(
            self.closed_neighborhood(u).isdisjoint(self.closed_neighborhood(v))
            for u, v in combinations(chosen_tuple, 2)
        )

    def two_packing_number(self, target: Iterable[int] | None = None) -> int:
        target_tuple = tuple(range(self.n) if target is None else target)
        for size in range(len(target_tuple), -1, -1):
            if any(self.is_two_packing(chosen) for chosen in combinations(target_tuple, size)):
                return size
        return 0

    def independence_number(self) -> int:
        best = 0
        for mask in range(1 << self.n):
            chosen = [v for v in range(self.n) if mask & (1 << v)]
            if all((min(u, v), max(u, v)) not in self.edges for u, v in combinations(chosen, 2)):
                best = max(best, len(chosen))
        return best

    def matching_number(self) -> int:
        neighbors = [
            frozenset(b if a == v else a for a, b in self.edges if a == v or b == v)
            for v in range(self.n)
        ]
        memo: dict[int, int] = {}

        def recurse(remaining: int) -> int:
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            first_bit = remaining & -remaining
            v = first_bit.bit_length() - 1
            without_v = remaining ^ first_bit
            best = recurse(without_v)
            for u in neighbors[v]:
                if without_v & (1 << u):
                    best = max(best, 1 + recurse(without_v ^ (1 << u)))
            memo[remaining] = best
            return best

        return recurse((1 << self.n) - 1)

    def connected_components(self) -> tuple[frozenset[int], ...]:
        unseen = set(range(self.n))
        answer: list[frozenset[int]] = []
        while unseen:
            seed = min(unseen)
            component = {seed}
            frontier = [seed]
            unseen.remove(seed)
            while frontier:
                v = frontier.pop()
                adjacent = {
                    b if a == v else a
                    for a, b in self.edges
                    if a == v or b == v
                }
                new = adjacent & unseen
                unseen -= new
                component |= new
                frontier.extend(new)
            answer.append(frozenset(component))
        return tuple(answer)

    def is_disjoint_union_of_odd_cliques(self) -> bool:
        for component in self.connected_components():
            size = len(component)
            if size % 2 == 0:
                return False
            expected_edges = size * (size - 1) // 2
            actual_edges = sum(1 for u, v in self.edges if u in component and v in component)
            if actual_edges != expected_edges:
                return False
        return True

    def closed_neighborhood_conflict_graph(self, target: Iterable[int]) -> "Graph":
        target_tuple = tuple(sorted(target))
        if not frozenset(target_tuple) <= frozenset(range(self.n)):
            raise ValueError("target contains an invalid vertex")
        edges = []
        for i, j in combinations(range(len(target_tuple)), 2):
            if not self.closed_neighborhood(target_tuple[i]).isdisjoint(
                self.closed_neighborhood(target_tuple[j])
            ):
                edges.append((i, j))
        return Graph.from_edges(len(target_tuple), edges)

    def integer_weight_functions(self, k: int) -> Iterator[tuple[int, ...]]:
        if k < 0:
            raise ValueError("k must be nonnegative")
        # Values greater than k are never needed: for packing they are infeasible,
        # and for domination they can be truncated to k.
        yield from product(range(k + 1), repeat=self.n)

    def is_k_packing_function(self, weights: Sequence[int], k: int) -> bool:
        self._validate_weights(weights)
        return all(sum(weights[u] for u in self.closed_neighborhood(v)) <= k for v in range(self.n))

    def is_k_dominating_function(self, weights: Sequence[int], k: int) -> bool:
        self._validate_weights(weights)
        return all(sum(weights[u] for u in self.closed_neighborhood(v)) >= k for v in range(self.n))

    def k_packing_number(self, k: int) -> int:
        return max(
            sum(weights)
            for weights in self.integer_weight_functions(k)
            if self.is_k_packing_function(weights, k)
        )

    def k_domination_number(self, k: int) -> int:
        return min(
            sum(weights)
            for weights in self.integer_weight_functions(k)
            if self.is_k_dominating_function(weights, k)
        )

    def is_fractional_packing_function(self, weights: Sequence[Fraction]) -> bool:
        if len(weights) != self.n or any(weight < 0 for weight in weights):
            return False
        return all(
            sum((weights[u] for u in self.closed_neighborhood(v)), Fraction(0)) <= 1
            for v in range(self.n)
        )

    def excess_peeling_parameter(self, target: Iterable[int]) -> int:
        """Return the exact parameter p_G(S) from angles/subset-slack.

        This exponential recursion is only a small-instance verifier.
        """
        initial = frozenset(target)
        if not initial <= frozenset(range(self.n)):
            raise ValueError("target contains an invalid vertex")
        memo: dict[frozenset[int], int] = {}

        def recurse(current: frozenset[int]) -> int:
            if current in memo:
                return memo[current]
            best = 0
            for v in range(self.n):
                hit = current & self.closed_neighborhood(v)
                if len(hit) >= 3:
                    best = max(best, len(hit) - 3 + recurse(current - hit))
            memo[current] = best
            return best

        return recurse(initial)

    def _validate_weights(self, weights: Sequence[int]) -> None:
        if len(weights) != self.n or any(not isinstance(w, int) or w < 0 for w in weights):
            raise ValueError("weights must be nonnegative integers, one per vertex")


def path(n: int) -> Graph:
    return Graph.from_edges(n, ((v, v + 1) for v in range(n - 1)))


def cycle(n: int) -> Graph:
    if n < 3:
        raise ValueError("a simple cycle needs at least three vertices")
    return Graph.from_edges(n, ((v, (v + 1) % n) for v in range(n)))


def complete(n: int) -> Graph:
    return Graph.from_edges(n, combinations(range(n), 2))


def fractional_tensor_lower_bound(
    left: Graph,
    right: Graph,
    left_weights: Sequence[Fraction],
    right_weights: Sequence[Fraction],
) -> Fraction:
    """Return the exact two-sided fractional tensor lower bound."""
    if not left.is_fractional_packing_function(left_weights):
        raise ValueError("left weights are not a fractional packing")
    if not right.is_fractional_packing_function(right_weights):
        raise ValueError("right weights are not a fractional packing")
    left_total = sum(left_weights, Fraction(0))
    right_total = sum(right_weights, Fraction(0))
    if left_total == 0 or right_total == 0:
        raise ValueError("fractional packings must be nonzero")

    kappa = max(
        right_weights[v]
        * sum((left_weights[x] for x in left.closed_neighborhood(u)), Fraction(0))
        + left_weights[u]
        * sum((right_weights[y] for y in right.closed_neighborhood(v)), Fraction(0))
        - left_weights[u] * right_weights[v]
        for u in range(left.n)
        for v in range(right.n)
    )
    if kappa <= 0:
        raise AssertionError("nonzero packings must give positive kappa")
    return left_total * right_total / kappa
