"""Verify the exact rational counterexample to the terminal-pair bridge."""

from polytope import paffenholz_24_cell


def facet_labels(polytope):
    return tuple(incident for incident, _, _ in polytope.facets)


def verify():
    source = paffenholz_24_cell()
    regular_family_member = paffenholz_24_cell((0, 0, 0, 0))
    if facet_labels(source) != facet_labels(regular_family_member):
        raise AssertionError("the deformation left the labelled 24-cell chamber")

    polytope = source.santalo_projective_normalization()
    polar = polytope.polar()
    if polytope.volume_and_centroid() != polytope.facet_cone_volume_and_centroid():
        raise AssertionError("independent primal centroid calculations disagree")
    if polar.volume_and_centroid() != polar.facet_cone_volume_and_centroid():
        raise AssertionError("independent polar centroid calculations disagree")

    primal_centroid = polytope.volume_and_centroid()[1]
    polar_centroid = polar.volume_and_centroid()[1]
    if not any(primal_centroid):
        raise AssertionError("the counterexample unexpectedly became bi-centred")
    if any(polar_centroid):
        raise AssertionError("the origin is not the certified Santaló point")

    primal_cases = polytope.direction_flat_dimensions()
    polar_cases = polar.direction_flat_dimensions()
    if {case["dimension"] for case in primal_cases} != {5}:
        raise AssertionError("the primal has a non-affine admissible speed")
    if {case["dimension"] for case in polar_cases} != {5}:
        raise AssertionError("the Santaló polar has a non-affine admissible speed")

    print("labelled-24-cell-incidence", True)
    print("santalo-polar-centroid-zero", True)
    print("primal-centroid-zero", False)
    print("primal-direction-flats", len(primal_cases))
    print("polar-direction-flats", len(polar_cases))
    print("all-speed-dimensions", 5)
    print("terminal-pair-implies-simplex", False)


if __name__ == "__main__":
    verify()
