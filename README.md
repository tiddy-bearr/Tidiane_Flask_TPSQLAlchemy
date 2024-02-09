# Application de Gestion d'Hôtel

Cette application Flask est conçue pour gérer les réservations de chambres d'hôtel. Elle offre une interface API RESTful pour effectuer des opérations telles que la consultation des chambres disponibles, la création de réservations, l'ajout, la mise à jour et la suppression de chambres.

## Prérequis

Avant de commencer à utiliser cette application, assurez-vous d'avoir installé Python et les dépendances requises répertoriées dans le fichier `requirements.txt`. Vous pouvez installer ces dépendances en exécutant la commande suivante :

```bash
pip install -r requirements.txt
```

## Configuration

1. Assurez-vous d'avoir configuré votre base de données dans le fichier `database.py`. Par défaut, cette application utilise une base de données SQLite. Si vous souhaitez utiliser une autre base de données, modifiez la configuration en conséquence.

2. Vous pouvez également ajuster d'autres paramètres de configuration tels que le port sur lequel l'application Flask écoute dans le fichier `run.py`.

## Utilisation

1. Lancez l'application en exécutant le fichier `run.py` :

```bash
python run.py
```

2. Accédez à l'application à l'adresse [http://localhost:5000](http://localhost:5000) dans votre navigateur web ou utilisez des requêtes HTTP pour interagir avec l'API.

## Endpoints de l'API

- `GET /api/chambres/disponibles` : Renvoie la liste des chambres disponibles pour les dates spécifiées dans les paramètres de requête `date_arrivee` et `date_depart`.
- `POST /api/reservations` : Crée une nouvelle réservation avec les détails fournis dans le corps de la requête au format JSON.

- `DELETE /api/reservations/<id>` : Annule la réservation correspondant à l'identifiant spécifié dans l'URL.

- `POST /api/chambres` : Ajoute une nouvelle chambre avec les détails fournis dans le corps de la requête au format JSON.

- `PUT /api/chambres/<id>` : Met à jour les détails de la chambre correspondant à l'identifiant spécifié dans l'URL avec les données fournies dans le corps de la requête au format JSON.

- `DELETE /api/chambres/<id>` : Supprime la chambre correspondant à l'identifiant spécifié dans l'URL.

## Exemples d'utilisation

### Requête pour obtenir les chambres disponibles

```bash
GET /api/chambres/disponibles?date_arrivee=2024-02-10&date_depart=2024-02-15
```

### Requête pour créer une réservation

```bash
POST /api/reservations
Content-Type: application/json

{
  "id_client": 1,
  "id_chambre": 3,
  "date_arrivee": "2024-02-10",
  "date_depart": "2024-02-15",
  "statut": "confirmé"
}
```

### Requête pour annuler une réservation

```bash
DELETE /api/reservations/5
```

### Requête pour ajouter une nouvelle chambre

```bash
POST /api/chambres
Content-Type: application/json

{
  "numero": "101",
  "type": "simple",
  "prix": 50.00
}
```

### Requête pour mettre à jour les détails d'une chambre

```bash
PUT /api/chambres/3
Content-Type: application/json

{
  "numero": "201",
  "type": "double",
  "prix": 100.00
}
```

### Requête pour supprimer une chambre

```bash
DELETE /api/chambres/3
```
