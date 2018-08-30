try:
    from ucollections import OrderedDict
    import uctypes
except ImportError:
    print("SKIP")
    raise SystemExit

OFFSET_BITS = 17
OFFSET_MASK = (1 << OFFSET_BITS) - 1

o = OrderedDict

desc = o((
    ("s0", uctypes.UINT8),
    ("s1", uctypes.UINT16),
    ("s2", uctypes.UINT8),
    ("arr", (uctypes.ARRAY, uctypes.UINT16 | 2)),
    ("s3", uctypes.UINT8),
    ("sub", (0, o((
        ("b0", uctypes.UINT8),
        ("b1", uctypes.UINT8),
    )))),
    ("arr2", (uctypes.ARRAY, 2, {"fi": uctypes.UINT32})),
))

sizeof = uctypes.calc_offsets(desc, uctypes.LITTLE_ENDIAN)

print(sizeof)

offsets = [(x[0] if isinstance(x, tuple) else x) & OFFSET_MASK for x in desc.values()]
print(offsets)