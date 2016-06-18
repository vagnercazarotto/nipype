# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from .....testing import assert_equal
from ..specialized import ACPCTransform


def test_ACPCTransform_inputs():
    input_map = dict(acpc=dict(argstr='--acpc %s...',
    ),
    args=dict(argstr='%s',
    ),
    debugSwitch=dict(argstr='--debugSwitch ',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    midline=dict(argstr='--midline %s...',
    ),
    outputTransform=dict(argstr='--outputTransform %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = ACPCTransform.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_ACPCTransform_outputs():
    output_map = dict(outputTransform=dict(),
    )
    outputs = ACPCTransform.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
