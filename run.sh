#!/bin/bash

INPUT_DIR="dvid_frames"  # Répertoire contenant les images
OUTPUT_DIR="results_yolo11s"         # Répertoire pour sauvegarder les résultats

python extract_frames_from_vidmp4.py --input_dir "$INPUT_DIR" --output_dir "$OUTPUT_DIR" --model_path "$MODEL_PATH"

if [ $? -eq 0 ]; then
    echo "extract_frames_from_vidmp4.py a été exécuté avec succès."
else
    echo "Erreur lors de l'exécution de extract.py."
fi