# Tesis Predicción de Cultivos de Cacao

Este monorepo contiene los proyectos para el desarrollo de una app móvil, backend y panel web para el control de calidad y pronóstico de rendimiento de cultivos de cacao usando modelos predictivos.

## Estructura del repositorio

- `backend/` — Backend en Django (API y modelos predictivos)
- `web/` — Panel de administración web (React)
- `mobile/` — App móvil (React Native)
- `shared/` — Código/documentación/modelos compartidos

## Primeros pasos

1. Clona el repositorio
2. Revisa las instrucciones en cada carpeta para levantar cada proyecto

## Comandos útiles

### Backend (Django)
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt  # si existe
python manage.py runserver
```

### Web (React)
```bash
cd web
npm install
npm start
```

### Mobile (React Native)
```bash
cd mobile/mobileApp
npm install
npx react-native start
```

## Notas
- Configura tus variables de entorno en cada proyecto según sea necesario.
- Para desarrollo colaborativo, usa ramas y pull requests.
