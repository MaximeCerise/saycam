import cv2
import os

def extract_frames(video_path, output_dir, n):
    # Créer le dossier de sortie s'il n'existe pas
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Charger la vidéo
    cap = cv2.VideoCapture(video_path)

    # Vérifier si la vidéo est ouverte
    if not cap.isOpened():
        print("Erreur lors de l'ouverture de la vidéo.")
        return

    frame_count = 0
    saved_frame_count = 0

    while True:
        # Lire la frame suivante
        ret, frame = cap.read()

        if not ret:
            break  # Fin de la vidéo

        frame_count += 1
        
        # Sauvegarder chaque n-ième frame
        if frame_count % n == 0:
            frame_filename = os.path.join(output_dir, f"frame_{saved_frame_count + 1}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1
            print(f"Frame {saved_frame_count} enregistrée : {frame_filename}")

    # Libérer la capture vidéo
    cap.release()
    print(f"Extraction terminée. {saved_frame_count} frames ont été enregistrées.")

# Exemple d'utilisation
video_path = 'vid2.mp4'  # Remplace par le chemin vers ta vidéo
output_dir = 'vid_frames/vid2_frames'            # Dossier où les frames seront enregistrées
n = 30                                   # Enregistrer chaque 30ème frame

extract_frames(video_path, output_dir, n)