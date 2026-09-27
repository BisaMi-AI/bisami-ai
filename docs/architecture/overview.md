# Architecture — BisaMi AI

## Vue d'ensemble

BisaMi AI est structuré autour d'une architecture modulaire en couches. Chaque composant — stockage, ingestion, moteur RAG, fournisseurs LLM, canaux de diffusion — peut évoluer indépendamment sans impacter les autres.

```
Clients (Dashboard / Widget / REST API)
              ↓
           FastAPI
    ┌────────┼────────┐
    ↓        ↓        ↓
  Auth   Chat Engine  Documents
              ↓           ↓
          RAG Engine   Ingestion
           ↙    ↘         ↓
         LLM   pgvector  Embeddings
                    ↓
              Réponse + Sources
                    ↓
               PostgreSQL
```

---

## Composants principaux

### Backend — FastAPI

Point d'entrée unique de la plateforme. Expose l'ensemble des fonctionnalités via une API REST versionnée (`/api/v1`).

Responsabilités :
- Authentification et autorisation (JWT)
- Orchestration des requêtes vers le moteur RAG
- Gestion des chatbots, documents et conversations
- Validation des données entrantes (Pydantic)

### Base de données — PostgreSQL + pgvector

PostgreSQL est la seule base de données de la plateforme. L'extension **pgvector** y ajoute le stockage et la recherche vectorielle, évitant ainsi d'avoir à gérer une base vectorielle séparée.

Toutes les données applicatives (utilisateurs, chatbots, documents, conversations) et les embeddings des chunks sont stockés dans la même instance PostgreSQL.

### Pipeline d'ingestion documentaire

Traite les documents importés et les transforme en vecteurs interrogeables.

```
Document
   ↓
Extraction du texte
   ↓
Nettoyage
   ↓
Découpage en chunks
   ↓
Génération des embeddings
   ↓
Indexation dans pgvector
```

Les métadonnées associées à chaque chunk (document source, page, section, date d'importation) sont conservées pour permettre la traçabilité des réponses.

**Formats supportés en V0.1 :** PDF texte  
**Évolutions prévues :** DOCX, TXT, Markdown, CSV, XLSX, HTML, URL, FAQ, texte manuel, API, bases de données

### Moteur RAG

Traite les questions des utilisateurs et génère des réponses contextualisées.

```
Question utilisateur
        ↓
  Normalisation
        ↓
Génération de l'embedding de la question
        ↓
  Recherche vectorielle (Top-K chunks)
        ↓
Construction du contexte
        ↓
         LLM
        ↓
Réponse + Sources
```

Le système limite autant que possible la génération de réponses présentées comme factuelles en l'absence d'informations pertinentes dans la base de connaissances.

### Fournisseurs LLM

L'architecture abstrait les fournisseurs de modèles derrière une interface commune pour éviter tout couplage fort.

```
LLMProvider
├── OpenAIProvider
├── GeminiProvider
├── AnthropicProvider
└── OllamaProvider
```

La V0.1 démarre avec un fournisseur. Les autres sont ajoutés progressivement. Le même principe s'applique aux modèles d'embedding.

```
EmbeddingProvider
├── OpenAI
├── HuggingFace
└── (autres)
```

---

## Modèle de données

### User
| Champ | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique |
| `email` | string | Adresse email (unique) |
| `password_hash` | string | Mot de passe haché (Argon2) |
| `first_name` | string | Prénom |
| `last_name` | string | Nom |
| `is_active` | bool | Compte actif |
| `created_at` | datetime | Date de création |

### Chatbot
| Champ | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique |
| `owner_id` | UUID | Référence vers User |
| `name` | string | Nom du chatbot |
| `description` | string | Description |
| `system_prompt` | text | Instructions système |
| `welcome_message` | string | Message d'accueil |
| `language` | string | Langue du chatbot |
| `status` | enum | `active` / `inactive` |
| `created_at` | datetime | Date de création |
| `updated_at` | datetime | Dernière modification |

### Document
| Champ | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique |
| `chatbot_id` | UUID | Référence vers Chatbot |
| `filename` | string | Nom du fichier |
| `file_type` | string | Type MIME |
| `status` | enum | `pending` / `processing` / `indexed` / `error` |
| `created_at` | datetime | Date d'import |

### DocumentChunk
| Champ | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique |
| `document_id` | UUID | Référence vers Document |
| `content` | text | Contenu textuel du chunk |
| `page` | int | Numéro de page |
| `metadata` | jsonb | Métadonnées supplémentaires |
| `embedding` | vector | Vecteur d'embedding |

### Conversation
| Champ | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique |
| `chatbot_id` | UUID | Référence vers Chatbot |
| `session_id` | string | Identifiant de session utilisateur |
| `created_at` | datetime | Date de création |

### Message
| Champ | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique |
| `conversation_id` | UUID | Référence vers Conversation |
| `role` | enum | `user` / `assistant` |
| `content` | text | Contenu du message |
| `created_at` | datetime | Horodatage |

### MessageSource
| Champ | Type | Description |
|---|---|---|
| `id` | UUID | Identifiant unique |
| `message_id` | UUID | Référence vers Message |
| `chunk_id` | UUID | Référence vers DocumentChunk |
| `similarity_score` | float | Score de similarité vectorielle |

---

## Principes d'architecture

### Modularité
Les composants IA, stockage, ingestion et canaux sont découplés. Remplacer PostgreSQL par une autre base ou changer de fournisseur LLM ne doit pas impacter les autres couches.

### Extensibilité
Un contributeur peut ajouter un nouveau fournisseur LLM, un loader de document ou un connecteur de canal sans modifier le noyau de l'application. L'architecture favorise l'ajout par extension plutôt que par modification.

### API First
Toutes les fonctionnalités importantes sont exposées via l'API REST. Le dashboard et le widget sont eux-mêmes des clients de cette API, comme n'importe quelle intégration tierce.

### Security by Design
Isolation des données par utilisateur, hashage des mots de passe (Argon2), JWT, validation Pydantic, rate limiting, contrôle des fichiers importés. Les secrets ne sont jamais stockés en clair dans le dépôt.

### Observabilité
Les erreurs et opérations critiques sont journalisées pour permettre le diagnostic. Les métriques d'usage (tokens, latence, taux de réponse) sont collectées pour l'analytics.

### Human Control
Les fonctionnalités futures permettant au chatbot d'exécuter des actions métier devront inclure des mécanismes d'autorisation et de validation humaine.

---

## Canaux de diffusion

```
Chatbot Engine
├── Widget web       ← V0.1
├── REST API         ← V0.1
├── Mobile           ← évolution
└── WhatsApp         ← évolution
```

Des connecteurs supplémentaires peuvent être développés par la communauté.

---

## Infrastructure

La plateforme se lance localement avec Docker Compose :

- **bisami-db** — PostgreSQL 18 + pgvector
- **bisami-api** — Backend FastAPI

Voir [docs/development/setup.md](../development/setup.md) pour les détails d'installation.
