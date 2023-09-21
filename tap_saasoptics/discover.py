from singer.catalog import Catalog, CatalogEntry, Schema
from tap_saasoptics.schema import get_schemas
from tap_saasoptics.streams import get_streams


def discover(schema_dir="schemas", is_full_sync=False):
    STREAMS = get_streams(is_full_sync)
    schemas, field_metadata = get_schemas(schema_dir, is_full_sync)
    catalog = Catalog([])

    for stream_name, schema_dict in schemas.items():
        schema = Schema.from_dict(schema_dict)
        mdata = field_metadata[stream_name]

        catalog.streams.append(CatalogEntry(
            stream=stream_name,
            tap_stream_id=stream_name,
            key_properties=STREAMS[stream_name]['key_properties'],
            schema=schema,
            metadata=mdata
        ))

    return catalog
