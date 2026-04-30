# 🧾 Proyecto CI - Equipo X

## 👥 Integrantes

* Milagros Lamas
* Damian Marengo
* Sofia Ramos

---

## 💻 Lenguaje elegido

El proyecto está desarrollado en **Python** 🐍

---

## 🔄 Workflow de trabajo

Se utilizó un flujo de trabajo basado en ramas:

1. Cada integrante creó su propia rama:

   ```
   feature-nombre
   ```

2. En cada rama se desarrolló una funcionalidad independiente:

   * Agregar venta
   * Eliminar venta
   * Ver ventas
   * Cálculo de totales

3. Luego se realizó un **Pull Request (PR)** hacia la rama `main`.

4. Cada PR fue revisado por otro integrante del equipo.

5. En caso de conflictos, se resolvieron antes del merge.

6. Se utilizó **GitHub Actions** para validar automáticamente el código.

7. El merge se realizó únicamente cuando:

   * ✔ El workflow pasó correctamente
   * ✔ El PR fue aprobado

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/usuario/repositorio.git
   cd repositorio
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar el programa principal:

   ```bash
   python menu_principal.py
   ```

---

## 📁 Estructura del proyecto

* `menu_principal.py` → menú principal
* `agregar_venta.py` → agrega ventas
* `eliminar_venta.py` → elimina ventas
* `ver_ventas.py` → muestra ventas
* `calcular_total.py` → calcula totales
* `tests/` → pruebas del sistema

---

## 🚀 Notas finales

Este proyecto fue desarrollado como práctica de integración continua (CI) utilizando GitHub.

