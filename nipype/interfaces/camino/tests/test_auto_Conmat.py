# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..connectivity import Conmat


def test_Conmat_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-inputfile %s',
    mandatory=True,
    ),
    output_root=dict(argstr='-outputroot %s',
    genfile=True,
    ),
    scalar_file=dict(argstr='-scalarfile %s',
    requires=['tract_stat'],
    ),
    target_file=dict(argstr='-targetfile %s',
    mandatory=True,
    ),
    targetname_file=dict(argstr='-targetnamefile %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    tract_prop=dict(argstr='-tractstat %s',
    units='NA',
    xor=['tract_stat'],
    ),
    tract_stat=dict(argstr='-tractstat %s',
    requires=['scalar_file'],
    units='NA',
    xor=['tract_prop'],
    ),
    )
    inputs = Conmat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Conmat_outputs():
    output_map = dict(conmat_sc=dict(),
    conmat_ts=dict(),
    )
    outputs = Conmat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
