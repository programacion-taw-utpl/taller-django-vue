<script setup>
import { ref, onMounted } from 'vue'

const API_URL = import.meta.env.VITE_API_URL

const proyectos = ref([])
const cargando = ref(false)
const error = ref('')

async function cargarProyectos() {
  cargando.value = true
  error.value = ''

  try {
    const respuesta = await fetch(
      `${API_URL}/api/proyectos/`
    )

    if (!respuesta.ok) {
      throw new Error('No se pudieron consultar los proyectos')
    }

    proyectos.value = await respuesta.json()

  } catch (e) {
    error.value = e.message

  } finally {
    cargando.value = false
  }
}

onMounted(() => {
  cargarProyectos()
})
</script>

<template>
  <main>
    <h1>Gestión de proyectos académicos - taller</h1>

    <p>
      Aplicación desarrollada con Django REST Framework y Vue 3.
    </p>

    <button @click="cargarProyectos">
      Actualizar proyectos
    </button>

    <p v-if="cargando">Consultando proyectos...</p>

    <p v-if="error" role="alert">
      {{ error }}
    </p>

    <table v-if="!cargando && !error">
      <thead>
        <tr>
          <th>ID</th>
          <th>Título</th>
          <th>Responsable</th>
          <th>Estado</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="proyecto in proyectos" :key="proyecto.id">
          <td>{{ proyecto.id }}</td>
          <td>{{ proyecto.titulo }}</td>
          <td>{{ proyecto.responsable }}</td>
          <td>{{ proyecto.estado }}</td>
        </tr>
      </tbody>
    </table>

    <p v-if="!cargando && !error && proyectos.length === 0">
      No existen proyectos registrados.
    </p>
  </main>
</template>
