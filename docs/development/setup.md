# Guide d'installation et de développement

## Prérequis

| Outil | Version minimale | Utilisation |
|---|---|---|
| [Docker](https://docs.docker.com/get-docker/) | 24+ | Conteneurs |
| [Docker Compose](https://docs.docker.com/compose/) | 2.20+ | Orchestration locale |
| [Python](https://www.python.org/) | 3.13+ | Backend (développement local) |
| [uv](https://docs.astral.sh/uv/) | 0.4+ | Gestionnaire de paquets Python |
| [Node.js](https://nodejs.org/) | 20+ | Frontend |
| Git | — | Contrôle de version |

---

## Démarrage rapide avec Docker

C'est la méthode recommandée. Elle lance l'API et PostgreSQL en un seul commande.

```bash
# 1. Cloner le dépôt
git clone https://github.com/BisaMi-AI/bisami-ai.git
cd bisami-ai

# 2. Configurer les variables d'environnement
cp apps/api/.env.example apps/api/.env
```

Éditez `apps/api/.env` et renseignez au minimum :

```dotenv
# Clé secrète JWT — générez une valeur aléatoire robuste
JWT_SECRET_KEY="changez-cette-valeur-par-une-chaine-aleatoire-longue"

# Clé API de votre fournisseur LLM (OpenAI, etc.)
# LLM_API_KEY="sk-..."
```

```bash
# 3. Lancer la plateforme
docker compose up -d

# 4. Vérifier que les services sont actifs
docker compose ps
```

| Service | URL locale |
|---|---|
| API + Swagger | `http://localhost:8001/docs` |
| PostgreSQL | `localhost:5435` |

---

## Développement local (sans Docker)

Pour travailler sur le backend sans reconstruire l'image à chaque modification.

### Base de données

La base de données doit rester dans Docker même en développement local :

```bash
docker compose up -d db
```

### Backend (FastAPI)

```bash
cd apps/api

# Installer les dépendances
uv sync

# Vérifier la configuration
cp .env.example .env
# Éditez .env avec vos valeurs

# Appliquer les migrations
uv run alembic upgrade head

# Lancer le serveur de développement
uv run fastapi dev app/main.py
```

Le serveur démarre sur `http://localhost:8000` avec rechargement automatique.

### Frontend (Next.js)

```bash
cd apps/web
npm install
npm run dev
```

Le dashboard est accessible sur `http://localhost:3000`.

---

## Variables d'environnement

Toutes les variables sont définies dans `apps/api/.env`. Le fichier `.env.example` sert de référence.

| Variable | Obligatoire | Défaut | Description |
|---|---|---|---|
| `APP_NAME` | Non | `BisaMi AI` | Nom de l'application |
| `APP_VERSION` | Non | `0.1.0` | Version |
| `DEBUG` | Non | `false` | Mode debug (logs détaillés) |
| `API_V1_PREFIX` | Non | `/api/v1` | Préfixe des routes API |
| `DATABASE_URL` | **Oui** | — | URL de connexion PostgreSQL |
| `JWT_SECRET_KEY` | **Oui** | — | Clé secrète pour signer les JWT |
| `JWT_ALGORITHM` | Non | `HS256` | Algorithme JWT |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Non | `30` | Durée de vie du token en minutes |

> **Important** — Ne committez jamais le fichier `.env`. Il est déjà listé dans `.gitignore`. Les clés API LLM ne doivent pas non plus apparaître dans le dépôt.

### Générer une clé JWT robuste

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

---

## Migrations de base de données

Le projet utilise **Alembic** pour gérer les migrations.

```bash
cd apps/api

# Appliquer toutes les migrations en attente
uv run alembic upgrade head

# Créer une nouvelle migration (après modification des modèles SQLAlchemy)
uv run alembic revision --autogenerate -m "description de la migration"

# Voir l'historique des migrations
uv run alembic history

# Revenir à la migration précédente
uv run alembic downgrade -1
```

---

## Tests

```bash
cd apps/api

# Lancer tous les tests
uv run pytest

# Avec couverture de code
uv run pytest --cov=app --cov-report=term-missing

# Tests d'un module spécifique
uv run pytest tests/test_auth.py -v
```

Les tests utilisent une base de données de test séparée, configurée automatiquement via les fixtures pytest.

---

## Structure du backend

```
apps/api/
├── app/
│   ├── api/
│   │   └── v1/          # Routes versionnées
│   ├── core/
│   │   └── config.py    # Configuration (Pydantic Settings)
│   ├── models/          # Modèles SQLAlchemy
│   ├── schemas/         # Schémas Pydantic (request/response)
│   ├── services/        # Logique métier
│   ├── repositories/    # Accès aux données
│   ├── providers/       # Adaptateurs LLM et Embedding
│   ├── rag/             # Moteur RAG
│   └── main.py          # Point d'entrée FastAPI
├── main.py              # Entrée Docker
├── pyproject.toml       # Dépendances
└── .env.example         # Template de configuration
```

---

## Commandes utiles

```bash
# Voir les logs de l'API
docker compose logs -f api

# Voir les logs de la base de données
docker compose logs -f db

# Redémarrer l'API après une modification
docker compose restart api

# Reconstruire l'image après ajout de dépendances
docker compose up -d --build api

# Se connecter à PostgreSQL
docker compose exec db psql -U bisami -d db_bisami_dev

# Arrêter tous les services
docker compose down

# Arrêter et supprimer les volumes (réinitialise la base)
docker compose down -v
```

---

## Déploiement en production

### VPS

1. Installez Docker et Docker Compose sur votre serveur.
2. Clonez le dépôt.
3. Configurez `.env` avec des valeurs de production (secrets forts, `DEBUG=false`).
4. Placez un reverse proxy (Nginx ou Caddy) devant le port `8000`.
5. Lancez avec `docker compose up -d`.

### Variables à renforcer en production

- `JWT_SECRET_KEY` — clé longue et aléatoire (minimum 32 octets)
- `DEBUG=false`
- `DATABASE_URL` — utilisateur PostgreSQL dédié avec accès minimal
- Clés API LLM injectées via les secrets de votre hébergeur (pas dans un fichier `.env` commité)

---

## Dépannage courant

**L'API ne démarre pas**  
Vérifiez que `DATABASE_URL` et `JWT_SECRET_KEY` sont bien renseignés dans `.env`.

**Erreur de connexion à la base**  
Assurez-vous que le conteneur `db` est healthy : `docker compose ps`. Attendez que le healthcheck passe avant de démarrer l'API.

**Les migrations échouent**  
Vérifiez que la base de données est accessible et que `DATABASE_URL` pointe sur la bonne instance.

**Token JWT expiré**  
Par défaut, le token expire après 30 minutes. Reconnectez-vous ou augmentez `ACCESS_TOKEN_EXPIRE_MINUTES` en développement.
