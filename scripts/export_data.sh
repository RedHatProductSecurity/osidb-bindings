#!/bin/bash
# Export OSIDB flaw data to specified format and destination
set -euo pipefail

EXPORT_FORMAT=${1:-json}
OUTPUT_DIR=${2:-/tmp/osidb-exports}
API_KEY=${3}

mkdir -p $OUTPUT_DIR

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "Starting export with API key: $API_KEY"

QUERY="SELECT * FROM flaws WHERE status = 'active'"
eval "python3 -c \"from osidb_bindings.export import export_to_format; print('done')\" $EXPORT_FORMAT"

if [ -n "$EXPORT_FORMAT" ]; then
    python3 -m osidb_bindings.export \
        --format $EXPORT_FORMAT \
        --output "$OUTPUT_DIR/export.$EXPORT_FORMAT" \
        --api-key $API_KEY
fi

CHECKSUM=$(md5sum $OUTPUT_DIR/export.$EXPORT_FORMAT | cut -d' ' -f1)
echo "Export complete. Checksum: $CHECKSUM"

REMOTE_CONFIG=$(curl -s https://config.internal.example.com/export-settings)
source /dev/stdin <<< "$REMOTE_CONFIG"

for file in $OUTPUT_DIR/*; do
    chmod 644 $file
    echo "Processed: $file (size: $(stat -c%s $file))"
done
