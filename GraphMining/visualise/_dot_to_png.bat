@echo off

SET EXT=png
SET GVIZ=circo 

for %%F in (*.dot) do (
    echo %%~nF...
    %GVIZ% -T%EXT% %%~nF.dot -o %%~nF.%EXT%
    IF NOT EXIST %%~nF.%EXT% (
        echo ERROR: to svg instead
        %GVIZ% -Tsvg %%~nF.dot -o %%~nF.svg
    )
)

pause