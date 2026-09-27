# Politique de sécurité — BisaMi AI

## Signaler une vulnérabilité

**Ne créez pas d'issue publique GitHub pour signaler une vulnérabilité de sécurité.**

Si vous découvrez une faille, merci de la divulguer de manière responsable en envoyant un email à :

**security@bisami.ai**

Incluez dans votre message :

- Une description claire de la vulnérabilité
- Les étapes pour la reproduire
- L'impact potentiel estimé
- Toute suggestion de correction si vous en avez une

Vous recevrez un accusé de réception sous **48 heures** et une mise à jour sur l'avancement du traitement sous **7 jours**.

---

## Périmètre

Les éléments suivants sont dans le périmètre de cette politique :

- L'API backend (`apps/api`)
- Le dashboard web (`apps/web`)
- Le widget intégrable (`apps/widget`)
- L'infrastructure Docker

---

## Ce que nous nous engageons à faire

- Accuser réception de votre signalement rapidement
- Travailler avec vous pour comprendre et corriger le problème
- Vous informer lorsque le correctif est publié
- Vous créditer dans le changelog si vous le souhaitez

Nous vous demandons de votre côté de ne pas divulguer publiquement la vulnérabilité avant qu'un correctif soit disponible.

---

## Bonnes pratiques de déploiement

Pour les utilisateurs qui déploient BisaMi AI en self-hosted :

- Ne committez jamais le fichier `.env` ni aucune clé secrète dans votre dépôt Git
- Utilisez une valeur `JWT_SECRET_KEY` longue et aléatoire (minimum 32 octets)
- Maintenez les images Docker à jour pour bénéficier des correctifs de sécurité
- Limitez l'accès à votre instance PostgreSQL au seul réseau interne
- Placez un reverse proxy (Nginx, Caddy) devant l'API en production et activez HTTPS
- Configurez un rate limiting adapté à votre usage sur les endpoints publics

---

## Versions supportées

| Version | Support sécurité |
|---|---|
| `0.1.x` (actuelle) | ✅ Oui |
| Versions antérieures | ❌ Non |

Les correctifs de sécurité sont appliqués uniquement sur la version majeure actuelle.
