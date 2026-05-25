"""
Static site content for server-rendered pages.
"""

from typing import Dict, List

LOCATION_ENTRIES: List[Dict[str, str]] = [
    {
        "slug": "salt-lake-city-ut",
        "city": "Salt Lake City",
        "state": "UT",
        "address": "215 Industrial Way, Salt Lake City, UT 84101",
        "phone": "(801) 487-1656",
        "email": "slc@forshor.com",
        "image_path": "static/images/locations/salt-lake-city-ut.jpg",
        "blurb": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at lectus "
            "velit. For Shor supports downtown and valley concrete projects with rapid "
            "dispatch and practical recommendations."
        ),
    },
    {
        "slug": "provo-ut",
        "city": "Provo",
        "state": "UT",
        "address": "480 Builder Park Rd, Provo, UT 84601",
        "phone": "(801) 487-1656",
        "email": "provo@forshor.com",
        "image_path": "static/images/locations/provo-ut.jpg",
        "blurb": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer commodo, "
            "nisl quis malesuada feugiat, nibh massa interdum neque, in tempor felis "
            "metus et lacus."
        ),
    },
    {
        "slug": "ogden-ut",
        "city": "Ogden",
        "state": "UT",
        "address": "92 Steel Frame Dr, Ogden, UT 84401",
        "phone": "(801) 487-1656",
        "email": "ogden@forshor.com",
        "image_path": "static/images/locations/ogden-ut.jpg",
        "blurb": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ut ante "
            "et lorem iaculis bibendum. Crews in Weber County rely on this branch for "
            "consistent site-ready inventory."
        ),
    },
    {
        "slug": "st-george-ut",
        "city": "St. George",
        "state": "UT",
        "address": "760 Red Rock Industrial, St. George, UT 84770",
        "phone": "(801) 487-1656",
        "email": "stgeorge@forshor.com",
        "image_path": "static/images/locations/st-george-ut.jpg",
        "blurb": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus varius, "
            "orci at tempus lobortis, sapien risus cursus sem, et luctus nulla turpis "
            "at nibh."
        ),
    },
    {
        "slug": "logan-ut",
        "city": "Logan",
        "state": "UT",
        "address": "34 North Yard Lane, Logan, UT 84321",
        "phone": "(801) 487-1656",
        "email": "logan@forshor.com",
        "image_path": "static/images/locations/logan-ut.jpg",
        "blurb": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id velit a "
            "ante condimentum rhoncus. The Logan team supports northern Utah pours with "
            "priority same-day pull and load."
        ),
    },
]

PRODUCT_ENTRIES: List[Dict[str, str]] = [
    {
        "slug": "rotary-hammer-pro-3200",
        "name": "Rotary Hammer Pro 3200",
        "image_path": "static/images/products/rotary-hammer-pro-3200.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. High-impact "
            "concrete drilling and anchoring for dense structural work."
        ),
    },
    {
        "slug": "cordless-rebar-cutter-rx",
        "name": "Cordless Rebar Cutter RX",
        "image_path": "static/images/products/cordless-rebar-cutter-rx.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Clean rebar cuts "
            "on active sites with reduced downtime."
        ),
    },
    {
        "slug": "laser-level-xt-360",
        "name": "Laser Level XT 360",
        "image_path": "static/images/products/laser-level-xt-360.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Precision "
            "alignment for forms, beams, and transfer lines."
        ),
    },
    {
        "slug": "concrete-vibrator-maxvibe-18",
        "name": "Concrete Vibrator MaxVibe 18",
        "image_path": "static/images/products/concrete-vibrator-maxvibe-18.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Consolidates "
            "concrete fast for cleaner finish quality."
        ),
    },
    {
        "slug": "plate-compactor-ironstride",
        "name": "Plate Compactor IronStride",
        "image_path": "static/images/products/plate-compactor-ironstride.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Delivers reliable "
            "base compaction for slabs and pathways."
        ),
    },
    {
        "slug": "gas-cutoff-saw-blaze14",
        "name": "Gas Cut-Off Saw Blaze14",
        "image_path": "static/images/products/gas-cutoff-saw-blaze14.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Built for cutting "
            "masonry, concrete, and steel edges."
        ),
    },
    {
        "slug": "diamond-blade-ultracut",
        "name": "Diamond Blade UltraCut",
        "image_path": "static/images/products/diamond-blade-ultracut.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Long-life blade "
            "for high-volume concrete cutting."
        ),
    },
    {
        "slug": "form-tie-system-lockpoint",
        "name": "Form Tie System LockPoint",
        "image_path": "static/images/products/form-tie-system-lockpoint.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Dependable form "
            "tension and straightforward setup."
        ),
    },
    {
        "slug": "shoring-post-heavyline",
        "name": "Shoring Post HeavyLine",
        "image_path": "static/images/products/shoring-post-heavyline.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Heavy-load support "
            "for multi-stage pours."
        ),
    },
    {
        "slug": "adjustable-screw-jack-aj500",
        "name": "Adjustable Screw Jack AJ500",
        "image_path": "static/images/products/adjustable-screw-jack-aj500.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fine elevation "
            "control for staging and shoring systems."
        ),
    },
    {
        "slug": "epoxy-injection-kit-eik9",
        "name": "Epoxy Injection Kit EIK9",
        "image_path": "static/images/products/epoxy-injection-kit-eik9.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Structural crack "
            "repair support for challenging concrete repairs."
        ),
    },
    {
        "slug": "surface-grinder-concreteedge",
        "name": "Surface Grinder ConcreteEdge",
        "image_path": "static/images/products/surface-grinder-concreteedge.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Efficient edge and "
            "slab prep before coatings or overlays."
        ),
    },
    {
        "slug": "core-drill-rig-cd700",
        "name": "Core Drill Rig CD700",
        "image_path": "static/images/products/core-drill-rig-cd700.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Consistent core "
            "drilling through reinforced concrete."
        ),
    },
    {
        "slug": "trowel-powerfinish-36",
        "name": "Trowel PowerFinish 36",
        "image_path": "static/images/products/trowel-powerfinish-36.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Uniform slab "
            "finishing for commercial-grade surfaces."
        ),
    },
    {
        "slug": "rebar-tier-quickbind",
        "name": "Rebar Tier QuickBind",
        "image_path": "static/images/products/rebar-tier-quickbind.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fast and repeatable "
            "ties that reduce crew fatigue."
        ),
    },
    {
        "slug": "generator-sitepower-8k",
        "name": "Generator SitePower 8K",
        "image_path": "static/images/products/generator-sitepower-8k.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Stable temporary "
            "power for tools and lighting."
        ),
    },
    {
        "slug": "wet-saw-stonestrip-12",
        "name": "Wet Saw StoneStrip 12",
        "image_path": "static/images/products/wet-saw-stonestrip-12.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Clean precision "
            "cuts for block and stone materials."
        ),
    },
    {
        "slug": "anchor-adhesive-bondguard",
        "name": "Anchor Adhesive BondGuard",
        "image_path": "static/images/products/anchor-adhesive-bondguard.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Strong hold "
            "chemistry for critical anchoring applications."
        ),
    },
    {
        "slug": "pump-sprayer-sealcoat-pro",
        "name": "Pump Sprayer SealCoat Pro",
        "image_path": "static/images/products/pump-sprayer-sealcoat-pro.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Even material "
            "distribution across large pour surfaces."
        ),
    },
    {
        "slug": "jobsite-light-tower-vision360",
        "name": "Jobsite Light Tower Vision360",
        "image_path": "static/images/products/jobsite-light-tower-vision360.jpg",
        "description": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Reliable site "
            "illumination for early and late shifts."
        ),
    },
]

PARTNERS: List[str] = [
    "Rockline General Contractors",
    "Summit Structural Group",
    "Wasatch Build Systems",
    "Canyon Crest Civil",
    "Redstone Infrastructure Co.",
    "Frontline Concrete Partners",
]

FAQ_ENTRIES: List[Dict[str, str]] = [
    {
        "question": "How fast can you deliver to active job sites?",
        "answer": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum volutpat "
            "odio non feugiat luctus. Integer pretium interdum est."
        ),
    },
    {
        "question": "Do you support both rental and purchase options?",
        "answer": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ornare "
            "felis sed luctus laoreet. Pellentesque id justo eu libero posuere gravida."
        ),
    },
    {
        "question": "Can your team recommend specifications for unusual pours?",
        "answer": (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam id purus "
            "tortor. Nulla facilisi. Sed sed libero sit amet sem suscipit efficitur."
        ),
    },
]


def get_location_by_slug(slug: str) -> Dict[str, str] | None:
    """
    Return a location entry by slug.

    Args:
        slug: Location slug from the URL.

    Returns:
        Matched location dictionary or None.
    """

    for location in LOCATION_ENTRIES:
        if location["slug"] == slug:
            return location
    return None


def get_product_by_slug(slug: str) -> Dict[str, str] | None:
    """
    Return a product entry by slug.

    Args:
        slug: Product slug from request input.

    Returns:
        Matched product dictionary or None.
    """

    for product in PRODUCT_ENTRIES:
        if product["slug"] == slug:
            return product
    return None
