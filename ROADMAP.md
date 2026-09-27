# Roadmap — BisaMi AI

Cette feuille de route présente les versions planifiées et les fonctionnalités associées. Elle est indicative et peut évoluer en fonction des retours de la communauté.

---

## V0.1 — Core

Socle fonctionnel stable permettant à une organisation de créer son premier assistant IA et de l'intégrer à son site web.

**Parcours utilisateur cible :**  
Installer la plateforme → Créer un compte → Créer un chatbot → Configurer les instructions → Importer un PDF → Attendre l'indexation → Poser une question → Recevoir une réponse issue du document → Vérifier la source → Intégrer le chatbot à un site.

| Module | Fonctionnalités |
|---|---|
| **Authentification** | Création de compte, connexion, JWT, profil |
| **Chatbots** | Créer, consulter, modifier, désactiver, supprimer |
| **Documents** | Import PDF, extraction, chunking, embeddings, indexation pgvector, suppression |
| **RAG** | Question, recherche vectorielle, génération LLM, réponse avec sources |
| **Conversations** | Sessions, messages, historique |
| **Widget** | Widget web intégrable via snippet `<script>` |
| **API REST** | Tous les endpoints documentés, réponse JSON structurée avec sources |
| **Infrastructure** | Docker Compose, PostgreSQL + pgvector, migrations Alembic, tests |

**Hors périmètre V0.1 :** WhatsApp, Telegram, agents autonomes, voicebot, OCR complexe, workflow builder, CRM, paiement, marketplace, analytics avancés, fine-tuning, application mobile, multi-agent, SSO entreprise.

---

## V0.2 — Knowledge

Enrichissement des sources de connaissances supportées.

| Fonctionnalité | Description |
|---|---|
| Formats DOCX, TXT, Markdown | Support des documents texte courants |
| CSV | Import de données tabulaires |
| URLs | Indexation de pages web |
| FAQ | Format question/réponse dédié |
| Bases de connaissances multiples | Un chatbot peut agréger plusieurs bases |

---

## V0.3 — Providers

Ouverture à l'écosystème de modèles IA.

| Fonctionnalité | Description |
|---|---|
| Multiple LLM providers | Gemini, Anthropic, Ollama en plus d'OpenAI |
| Modèles locaux | Support complet d'Ollama pour le déploiement 100% self-hosted |
| Embedding providers | HuggingFace et autres modèles d'embedding |
| Configuration RAG avancée | Taille des chunks, overlap, Top-K, seuil de similarité configurables par chatbot |

---

## V0.4 — Enterprise

Fonctionnalités pour les équipes et organisations.

| Fonctionnalité | Description |
|---|---|
| Organisations | Compte organisation avec plusieurs membres |
| Utilisateurs & rôles | Administrateur, éditeur, lecteur |
| Permissions | Contrôle d'accès par chatbot et par base de connaissances |
| API Keys | Gestion des clés d'accès programmatique |
| Audit logs | Traçabilité des actions |
| Analytics | Conversations, messages, questions fréquentes, questions sans réponse, tokens consommés, coûts LLM, temps de réponse |

---

## V0.5 — Channels

Diffusion multi-canal et SDK.

| Fonctionnalité | Description |
|---|---|
| WhatsApp | Connecteur WhatsApp Business API |
| Telegram | Bot Telegram |
| Canaux additionnels | Autres messageries — développés par la communauté |
| SDK JavaScript | Client JS pour intégration custom |
| SDK Python | Client Python pour intégration backend |

---

## V1.0 — Stable

**Objectif :** disposer d'une plateforme stable permettant à une organisation de déployer et administrer plusieurs assistants conversationnels en production.

- Toutes les fonctionnalités des versions précédentes stabilisées
- Performance et scalabilité validées
- Documentation complète (installation, API, guides développeur)
- Suite de tests incluant l'évaluation de la qualité RAG
- Procédure de mise à jour documentée

---

## Évolutions stratégiques à long terme

Au-delà de la V1.0, BisaMi AI pourra évoluer d'un assistant informationnel vers un **assistant métier** capable d'interagir avec le système d'information de l'entreprise.

```
Utilisateur → "Quel est le statut de ma commande ?"
                       ↓
          Chatbot interroge l'API CRM/ERP
                       ↓
         Réponse personnalisée en temps réel
```

Ces évolutions (agents autonomes, connexions API métier, workflow builder) incluront des mécanismes de validation humaine pour les actions à fort impact, conformément au principe **Human Control** de l'architecture.

D'autres connecteurs, loaders, modèles et canaux pourront être développés et distribués par la communauté.

---

## Contribuer à la roadmap

Vous avez une idée ou une priorité différente ? Ouvrez une [Discussion GitHub](https://github.com/BisaMi-AI/bisami-ai/discussions) ou commentez les issues correspondantes. Les décisions de roadmap sont prises en tenant compte des retours de la communauté.
