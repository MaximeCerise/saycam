def plot_focus_map(path):
    
    import pandas as pd
    import numpy as np
    import plotly.express as px

    df = pd.read_csv(path)
    # Calcul de la position moyenne et du nombre d'occurrences
    df['x'] = (df['xmin'] + df['xmax']) / 2
    df['y'] = (df['ymin'] + df['ymax']) / 2

    grouped = df.groupby('name').agg({'x': 'mean', 'y': 'mean', 'name': 'count'}).rename(columns={'name': 'count'}).reset_index()

    # Calcul du centre du graphe
    x_center, y_center = grouped['x'].mean(), grouped['y'].mean()

    # Calcul de la distance au centre
    grouped['distance'] = np.sqrt((grouped['x'] - x_center)**2 + (grouped['y'] - y_center)**2)

    # Normalisation des distances pour la couleur
    grouped['distance_norm'] = (grouped['distance'] - grouped['distance'].min()) / (grouped['distance'].max() - grouped['distance'].min())

    # Création du graphique interactif
    fig = px.scatter(
        grouped, 
        x="x", y="y", 
        size="count",  # Taille des cercles selon le nombre d'occurrences
        color=1 - grouped["distance_norm"],  # Plus proche du centre = plus rouge
        color_continuous_scale="RdBu_r",  # Palette de couleur inversée (rouge = proche, bleu = loin)
        hover_name="name",  # Affiche le nom au survol
        title="Répartition des objets avec couleur en fonction de la distance au centre"
    )

    fig.update_traces(marker=dict(line=dict(width=1, color='black')))  # Bordure noire pour les cercles

    fig.update_layout(
        xaxis_title="X",
        yaxis_title="Y",
        coloraxis_colorbar=dict(title="Proximité du centre"),
        template="plotly_white"  # Fond blanc pour une meilleure visibilité
    )
    import plotly.io as pio
    pio.renderers.default = "browser"  # Ouvre le graphique dans le navigateur
    fig.show()
