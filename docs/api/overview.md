# API — BisaMi AI

L'API REST de BisaMi AI expose l'ensemble des fonctionnalités de la plateforme. Toutes les routes sont préfixées par `/api/v1`.

La documentation interactive Swagger UI est disponible sur `http://localhost:8000/docs` (environnement local).

---

## Authentification

L'API utilise des **JSON Web Tokens (JWT)**. Incluez le token dans le header `Authorization` de chaque requête protégée.

```
Authorization: Bearer <token>
```

### Obtenir un token

```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "your-password"
}
```

**Réponse**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Créer un compte

```http
POST /api/v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "your-password",
  "first_name": "Alice",
  "last_name": "Dupont"
}
```

---

## Chatbots

### Créer un chatbot

```http
POST /api/v1/chatbots
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Assistant Support",
  "description": "Répond aux questions clients",
  "system_prompt": "Tu es un assistant serviable...",
  "welcome_message": "Bonjour, comment puis-je vous aider ?",
  "language": "fr"
}
```

**Réponse** `201 Created`
```json
{
  "id": "bot_xxxxxxxx",
  "name": "Assistant Support",
  "description": "Répond aux questions clients",
  "system_prompt": "Tu es un assistant serviable...",
  "welcome_message": "Bonjour, comment puis-je vous aider ?",
  "language": "fr",
  "status": "active",
  "created_at": "2026-09-16T10:00:00Z",
  "updated_at": "2026-09-16T10:00:00Z"
}
```

### Lister ses chatbots

```http
GET /api/v1/chatbots
Authorization: Bearer <token>
```

### Récupérer un chatbot

```http
GET /api/v1/chatbots/{bot_id}
Authorization: Bearer <token>
```

### Modifier un chatbot

```http
PATCH /api/v1/chatbots/{bot_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Nouveau nom",
  "system_prompt": "Nouvelles instructions..."
}
```

### Supprimer un chatbot

```http
DELETE /api/v1/chatbots/{bot_id}
Authorization: Bearer <token>
```

---

## Documents

### Importer un document

```http
POST /api/v1/chatbots/{bot_id}/documents
Authorization: Bearer <token>
Content-Type: multipart/form-data

file=@catalogue.pdf
```

**Réponse** `202 Accepted`
```json
{
  "id": "doc_xxxxxxxx",
  "filename": "catalogue.pdf",
  "file_type": "application/pdf",
  "status": "pending",
  "created_at": "2026-09-16T10:00:00Z"
}
```

Le traitement (extraction, chunking, embedding, indexation) est asynchrone. Interrogez le statut du document pour suivre la progression.

### Statuts d'un document

| Statut | Description |
|---|---|
| `pending` | En attente de traitement |
| `processing` | Extraction et indexation en cours |
| `indexed` | Prêt à être interrogé |
| `error` | Erreur lors du traitement |

### Lister les documents d'un chatbot

```http
GET /api/v1/chatbots/{bot_id}/documents
Authorization: Bearer <token>
```

### Récupérer le statut d'un document

```http
GET /api/v1/chatbots/{bot_id}/documents/{doc_id}
Authorization: Bearer <token>
```

### Supprimer un document

```http
DELETE /api/v1/chatbots/{bot_id}/documents/{doc_id}
Authorization: Bearer <token>
```

---

## Chat

L'endpoint principal pour interroger un chatbot. Il peut être appelé sans authentification (pour les intégrations widget et tierces), en fournissant uniquement le `bot_id`.

### Envoyer un message

```http
POST /api/v1/chat
Content-Type: application/json

{
  "bot_id": "bot_xxxxxxxx",
  "message": "Quels sont vos horaires d'ouverture ?",
  "session_id": "session_xxxxxxxx"
}
```

> `session_id` est optionnel. Fournissez-le pour conserver l'historique d'une conversation. S'il est absent, une nouvelle session est créée.

**Réponse** `200 OK`
```json
{
  "answer": "Nos bureaux sont ouverts du lundi au vendredi, de 9h à 18h.",
  "session_id": "session_xxxxxxxx",
  "sources": [
    {
      "document": "horaires.pdf",
      "page": 2,
      "chunk_id": "chunk_xxxxxxxx",
      "similarity_score": 0.92
    }
  ]
}
```

La réponse contient :
- `answer` — le texte de la réponse générée
- `session_id` — l'identifiant de session à réutiliser pour continuer la conversation
- `sources` — les chunks utilisés pour construire la réponse, avec leur score de similarité

---

## Conversations

### Lister les conversations d'un chatbot

```http
GET /api/v1/chatbots/{bot_id}/conversations
Authorization: Bearer <token>
```

### Récupérer une conversation avec ses messages

```http
GET /api/v1/conversations/{conversation_id}
Authorization: Bearer <token>
```

**Réponse**
```json
{
  "id": "conv_xxxxxxxx",
  "chatbot_id": "bot_xxxxxxxx",
  "session_id": "session_xxxxxxxx",
  "created_at": "2026-09-16T10:00:00Z",
  "messages": [
    {
      "id": "msg_xxxxxxxx",
      "role": "user",
      "content": "Quels sont vos horaires ?",
      "created_at": "2026-09-16T10:00:00Z",
      "sources": []
    },
    {
      "id": "msg_yyyyyyyy",
      "role": "assistant",
      "content": "Nos bureaux sont ouverts...",
      "created_at": "2026-09-16T10:00:01Z",
      "sources": [
        {
          "document": "horaires.pdf",
          "page": 2,
          "similarity_score": 0.92
        }
      ]
    }
  ]
}
```

---

## Codes d'erreur

| Code | Signification |
|---|---|
| `400` | Requête invalide — vérifiez les paramètres |
| `401` | Non authentifié — token manquant ou expiré |
| `403` | Accès refusé — ressource appartenant à un autre utilisateur |
| `404` | Ressource introuvable |
| `409` | Conflit — ressource déjà existante |
| `422` | Erreur de validation des données |
| `429` | Trop de requêtes — rate limiting |
| `500` | Erreur interne du serveur |

**Format des erreurs**
```json
{
  "detail": "Description de l'erreur"
}
```

---

## Rate limiting

Les endpoints publics (notamment `/api/v1/chat`) sont soumis à un rate limiting pour protéger la plateforme. Les limites exactes sont configurables via les variables d'environnement.

---

## Intégration Widget

Pour intégrer un chatbot sur un site web, ajoutez ce snippet dans votre HTML :

```html
<script
  src="https://domain.example/widget.js"
  data-bot-id="bot_xxxxxxxx">
</script>
```

Le widget gère automatiquement :
- l'ouverture/fermeture du chat
- l'affichage du message d'accueil
- la saisie utilisateur et l'affichage des réponses
- l'affichage des sources
- la conservation de la session
