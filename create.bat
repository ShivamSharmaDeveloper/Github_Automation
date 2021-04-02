@echo off

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    if "%2"=="" (
        python local.py %fn% %flag%
        ) else (
            if "%2"=="-a" (
                python remote.py %fn%
            ) else (
                if "%2"=="-r" (
                    python remove.py %fn%
                )   
            )
        )
    )
