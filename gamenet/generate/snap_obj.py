import network
import fix_network
import datatypes

datatypes.emit_header_snap_obj()

for f in network.Flags:
    f.emit_definition()
    print()

for o in network.Objects:
    o.emit_consts()
print()

datatypes.emit_enum_obj("SnapObj", network.Objects)
print()

for o in network.Objects:
    o.emit_definition()
    print()

for o in network.Objects:
    o.emit_impl_debug()
    o.emit_impl_encode_decode_int()
    print()

datatypes.emit_snap_obj_sizes(network.Objects)
