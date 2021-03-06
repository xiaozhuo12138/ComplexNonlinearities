#!/bin/sh
if [ -f $1 ]
    then
    echo "Projucer already built!"
else
    echo "Building Projucer..."
    rm -r JUCE
    git clone https://github.com/jatinchowdhury18/JUCE.git
    cd JUCE/extras/Projucer/Builds/$2
    if [ "$3" == "osx" ]
        then
        xcodebuild -project Projucer.xcodeproj > /dev/null
    elif [ "$3" == "windows" ]
        then
        msbuild.exe -v:quiet Projucer.sln
    elif [ "$3" == "linux" ]
        then
        make
    fi
fi
