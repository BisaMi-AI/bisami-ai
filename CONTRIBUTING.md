# Guide de contribution — BisaMi AI

Merci de l'intérêt que vous portez à BisaMi AI. Ce guide décrit comment contribuer efficacement au projet, qu'il s'agisse de corriger un bug, d'ajouter une fonctionnalité, d'améliorer la documentation ou de signaler un problème.

---

## Code de conduite

En participant à ce projet, vous vous engagez à respecter le [Code de conduite](CODE_OF_CONDUCT.md). Les comportements non conformes peuvent entraîner une exclusion temporaire ou permanente.

---

## Comment contribuer

### Signaler un bug

1. Vérifiez que le bug n'est pas déjà signalé dans les [issues](https://github.com/BisaMi-AI/bisami-ai/issues).
2. Ouvrez une nouvelle issue en utilisant le template **Bug report**.
3. Fournissez :
   - Une description claire du problème
   - Les étapes pour le reproduire
   - Le comportement attendu
   - Les logs ou messages d'erreur pertinents
   - Votre environnement (OS, version Docker, version Python)

### Proposer une fonctionnalité

1. Ouvrez une issue avec le template **Feature request** pour discuter de l'idée avant de commencer à coder.
2. Attendez un retour d'un mainteneur avant d'ouvrir une PR.

### Soumettre une Pull Request

1. **Forkez** le dépôt et créez une branche depuis `main`.
2. Nommez votre branche de manière explicite :
   - `feat/nom-de-la-fonctionnalite`
   - `fix/description-du-bug`
   - `docs/section-modifiee`
   - `refactor/composant-refactorise`
3. Développez votre contribution en respectant les conventions ci-dessous.
4. Assurez-vous que les tests passent localement.
5. Ouvrez la PR vers `main` avec une description claire des changements.

---

## Domaines de contribution

| Domaine | Description |
|---|---|
| **Backend** | API FastAPI, modèles, services, repositories |
| **Frontend** | Dashboard Next.js, composants UI |
| **RAG** | Amélioration du moteur de recherche et de génération |
| **Embeddings** | Nouveaux modèles et providers d'embedding |
| **Document loaders** | Support de nouveaux formats (DOCX, CSV, URL…) |
| **Fournisseurs LLM** | Intégration de nouveaux providers (Gemini, Anthropic, Ollama…) |
| **Connecteurs** | WhatsApp, Telegram, autres canaux |
| **Widget** | Amélioration du widget web intégrable |
| **SDK** | SDK JavaScript et Python |
| **Tests** | Tests unitaires, d'intégration, évaluation RAG |
| **Documentation** | Guides, référence API, tutoriels |
| **Sécurité** | Audits, corrections de vulnérabilités |
| **DevOps** | CI/CD, Docker, monitoring |
| **Traduction** | Traduction de la documentation et de l'interface |

---

## Labels GitHub

Utilisez ces labels pour filtrer les issues et PR :

| Label | Description |
|---|---|
| `good first issue` | Idéal pour une première contribution |
| `help wanted` | Contribution externe souhaitée |
| `backend` | Concerne le backend FastAPI |
| `frontend` | Concerne le dashboard Next.js |
| `AI/RAG` | Concerne le moteur RAG ou les embeddings |
| `documentation` | Amélioration ou ajout de documentation |
| `bug` | Comportement incorrect confirmé |
| `enhancement` | Amélioration d'une fonctionnalité existante |
| `security` | Problème ou amélioration de sécurité |
| `connector` | Nouveau connecteur ou canal |

---

## Conventions de code

### Python (Backend)

- **Style** : suivez [PEP 8](https://peps.python.org/pep-0008/). Utilisez `ruff` pour le linting et le formatage.
- **Types** : toutes les fonctions doivent avoir des annotations de type.
- **Docstrings** : documentez les fonctions et classes publiques.
- **Tests** : toute nouvelle fonctionnalité doit être couverte par des tests.

```bash
# Linting et formatage
ruff check .
ruff format .
```

### TypeScript (Frontend)

- Utilisez TypeScript strict.
- Respectez les conventions ESLint du projet.
- Les composants React suivent le pattern des composants fonctionnels avec hooks.

### Commits

Suivez la convention [Conventional Commits](https://www.conventionalcommits.org/) :

```
feat: ajouter le support des fichiers DOCX
fix: corriger l'expiration du token JWT
docs: mettre à jour le guide d'installation
refactor: extraire la logique RAG dans un service dédié
test: ajouter les tests du pipeline d'ingestion
chore: mettre à jour les dépendances
```

---

## Mise en place de l'environnement de développement

Consultez [docs/development/setup.md](docs/development/setup.md) pour les instructions complètes.

Résumé rapide :

```bash
git clone https://github.com/BisaMi-AI/bisami-ai.git
cd bisami-ai
cp apps/api/.env.example apps/api/.env
# Éditez .env
docker compose up -d db
cd apps/api && uv sync && uv run alembic upgrade head
uv run fastapi dev app/main.py
```

---

## Processus de review

- Toute PR doit passer les vérifications CI obligatoires (lint, tests, security checks) avant d'être fusionnée.
- Au moins un mainteneur doit approuver la PR.
- Les PR sont fusionnées avec un **squash merge** pour garder un historique propre.
- Si votre PR est en attente depuis plus de 7 jours sans retour, mentionnez un mainteneur avec `@`.

---

## Sécurité

Si vous découvrez une vulnérabilité de sécurité, **ne créez pas d'issue publique**. Consultez [SECURITY.md](SECURITY.md) pour la procédure de divulgation responsable.

---

## Questions

Pour toute question générale sur la contribution, ouvrez une [Discussion GitHub](https://github.com/BisaMi-AI/bisami-ai/discussions) plutôt qu'une issue.
