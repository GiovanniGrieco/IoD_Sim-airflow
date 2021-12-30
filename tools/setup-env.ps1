if (-Not (Test-Path -Path .venv -PathType Container)) {
    python -m venv .venv
}

.venv/Scripts/activate
pip install -r .\requirements.txt
