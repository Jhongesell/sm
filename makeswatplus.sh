#!/bin/sh

cd "${HOME}"

pushd "${HOME}/SWATPlus/TauDEM5Bin"
zsh ./unquarantine.sh
popd

tar -czvf "${HOME}/makeswatplus/swatplus.tgz" --exclude=swtaplus_wgn.sqlite --exclude=swatplus_soils.sqlite SWATPlus

pushd "${HOME}/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins"
tar -czvf "${HOME}/makeswatplus/qswatplus.tgz" --exclude=__pycache__ QSWATPlusMac3_64
popd
