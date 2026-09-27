# Changelog

Toutes les modifications notables de ce projet sont documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et ce projet respecte le [Versionnage Sémantique](https://semver.org/lang/fr/).

---

## [Unreleased]

### Ajouté
- Structure du monorepo (`apps/api`, `apps/web`, `apps/widget`)
- Backend FastAPI avec configuration Pydantic Settings
- Base de données PostgreSQL + pgvector via Docker Compose
- Authentification JWT (création de compte, connexion, profil)
- Gestion des chatbots (créer, consulter, modifier, désactiver, supprimer)
- Import de documents PDF avec extraction, chunking et indexation pgvector
- Moteur RAG — recherche vectorielle, génération LLM, réponse avec sources
- Gestion des conversations et de l'historique des messages
- Widget web intégrable via snippet `<script>`
- API REST versionnée (`/api/v1`) avec documentation Swagger
- Migrations de base de données avec Alembic
- Configuration Docker Compose pour le développement local
- Documentation du projet (`README`, `CONTRIBUTING`, `SECURITY`, `CODE_OF_CONDUCT`, `ROADMAP`)

---

<!-- Modèle pour les prochaines releases :

## [0.1.0] - AAAA-MM-JJ

### Ajouté
- Nouvelles fonctionnalités

### Modifié
- Changements sur des fonctionnalités existantes

### Corrigé
- Corrections de bugs

### Supprimé
- Fonctionnalités retirées

### Sécurité
- Corrections de vulnérabilités

[0.1.0]: https://github.com/BisaMi-AI/bisami-ai/releases/tag/v0.1.0
-->

[Unreleased]: https://github.com/BisaMi-AI/bisami-ai/compare/HEAD
