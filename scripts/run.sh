#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail
if [[ "${TRACE-0}" == "1" ]]; then
        set -o xtrace
fi

if [[ "${1-}" =~ ^-*h(elp)?$ ]]; then
        echo 'Usage: ./' + '$0' + 'arg-one arg-two'
        exit
fi

CDIR=$(dirname $0)
WORKDIR="$CDIR/../docs"
cd $WORKDIR

main() {
    local debug_port=8080
    python3 -m http.server $debug_port
}

main "$@"

