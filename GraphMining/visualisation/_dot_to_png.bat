@echo off

SET EXT=png
SET GVIZ=circo

for %%F in (*.dot) do (
    echo %%~nF...
    %GVIZ% -T%EXT% %%~nF.dot -o %%~nF.%EXT%

    IF NOT EXIST %%~nF.%EXT% (
        echo ERROR: no file, to svg instead
        %GVIZ% -Tsvg %%~nF.dot -o %%~nF.svg
    ) ELSE (
        for %%a in (%%~nF.%EXT%) do (
            IF %%~za EQU 0 (
                echo ERROR: file empty, to svg instead
                DEL %%a
                %GVIZ% -Tsvg %%~nF.dot -o %%~nF.svg
            )
        )
    )
)

pause