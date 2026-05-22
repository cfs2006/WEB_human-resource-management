# Human Resource Management

## Technology Stack

- Frontend: React inside Laravel `resources/js`
- Backend: PHP, Laravel Framework
- Database: MySQL

## Project Structure

This project follows the default Laravel-style structure at the repository root.
Frontend source code should live in `resources/js` and `resources/css`, not in `public`.

```text
WEB_human-resource-management/
├── app/
│   ├── Http/
│   │   └── Controllers/
│   ├── Models/
│   └── Providers/
├── bootstrap/
│   └── cache/
├── config/
├── database/
│   ├── factories/
│   ├── migrations/
│   └── seeders/
├── docs/
├── public/
├── resources/
│   ├── css/
│   ├── js/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── layouts/
│   │   ├── lib/
│   │   ├── pages/
│   │   └── types/
│   └── views/
├── routes/
├── storage/
├── tests/
│   ├── Feature/
│   └── Unit/
└── docker-compose.yaml
```

## Notes

- `resources/js`: React frontend source code.
- `resources/css`: frontend styles.
- `public`: browser-accessible files and built assets only.
- `app`, `routes`, `database`, `config`: Laravel backend application structure.
