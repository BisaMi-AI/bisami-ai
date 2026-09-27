# BisaMi AI

> **Demande-moi.** — Plateforme open source d'assistants IA configurables pour entreprises.

BisaMi AI permet aux organisations de créer, configurer, alimenter et déployer leurs propres assistants conversationnels fondés sur leurs connaissances, sans reconstruire toute l'infrastructure technique nécessaire.

---

## Fonctionnalités principales

- **Création et gestion de chatbots** — configurez les instructions, la langue, le message d'accueil et l'apparence de chaque assistant.
- **Base de connaissances** — importez vos PDF, documents et pages web ; BisaMi les découpe, les indexe et les rend interrogeables.
- **Pipeline RAG** — architecture Retrieval-Augmented Generation avec citations et traçabilité des sources.
- **Multi-provider** — conçu pour fonctionner avec OpenAI, Gemini, Anthropic, Ollama et d'autres fournisseurs LLM.
- **Widget intégrable** — un simple snippet `<script>` suffit pour intégrer un assistant à n'importe quel site.
- **API REST complète** — toutes les fonctionnalités sont accessibles programmatiquement.
- **Self-hosted** — déployez sur votre infrastructure, gardez le contrôle de vos données.

---

## Stack technique

| Couche | Technologies |
|---|---|
| Backend | Python 3.13, FastAPI, Pydantic, SQLAlchemy, Alembic |
| Base de données | PostgreSQL 18 + pgvector |
| Frontend | Next.js, TypeScript, Tailwind CSS |
| Infrastructure | Docker, Docker Compose, GitHub Actions |
| IA | Architecture RAG modulaire, embeddings configurables |

---

## Démarrage rapide

### Prérequis

- [Docker](https://docs.docker.com/get-docker/) et Docker Compose
- Git

### Installation

```bash
git clone https://github.com/BisaMi-AI/bisami-ai.git
cd bisami-ai

# Configurer les variables d'environnement
cp apps/api/.env.example apps/api/.env
# Éditez apps/api/.env et renseignez JWT_SECRET_KEY et votre clé API LLM

# Lancer la plateforme
docker compose up -d
```

L'API est accessible sur `http://localhost:8000`.  
La documentation Swagger est disponible sur `http://localhost:8000/docs`.

Pour un guide complet, consultez [docs/development/setup.md](docs/development/setup.md).

---

## Structure du dépôt

```
bisami-ai/
├── apps/
│   ├── api/        # Backend FastAPI — moteur RAG, persistance, migrations
│   ├── web/        # Dashboard Next.js — administration des assistants
│   └── widget/     # Widget web intégrable
├── packages/
│   ├── sdk/        # SDK partagé
│   └── shared/     # Utilitaires communs
├── docs/           # Documentation technique
├── infrastructure/ # Configuration Docker et infrastructure
└── docker-compose.yml
```

---

## Documentation

| Document | Description |
|---|---|
| [Architecture](docs/architecture/overview.md) | Architecture technique et logique du système |
| [API](docs/api/overview.md) | Référence de l'API REST |
| [Installation & Développement](docs/development/setup.md) | Guide de mise en place de l'environnement local |
| [Contribution](CONTRIBUTING.md) | Comment contribuer au projet |
| [Roadmap](ROADMAP.md) | Feuille de route et versions planifiées |
| [Sécurité](SECURITY.md) | Politique de sécurité et signalement de vulnérabilités |
| [Code de conduite](CODE_OF_CONDUCT.md) | Règles de la communauté |

---

## Contribution

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines, la liste des domaines où vous pouvez aider et les labels GitHub à suivre (`good first issue`, `help wanted`, etc.).

---

## Licence

Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE` pour les détails.

---

*BisaMi AI — Demande-moi.*
