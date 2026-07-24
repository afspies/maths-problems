"""Exact finite-graph hygiene for Vizing-domination work.

This module is deliberately small and brute-force. It is a verifier for examples
and definitions, not an attack on Vizing's conjecture.
"""

from __future__ import annotations

from dataclasses import dataclass
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
