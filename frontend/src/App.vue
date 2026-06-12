<template>
  <div class="min-h-screen bg-gray-100 py-8">
    <div class="container mx-auto px-4 max-w-4xl">
      <header class="mb-8 text-center">
        <h1 class="text-3xl font-extrabold text-blue-800">Sistema Interno de Suporte</h1>
        <p class="text-gray-600 mt-2">Central de atendimento e distribuição de demandas</p>
      </header>
      
      <FormularioChamado @chamadoCriado="carregarChamados" />
      <ListaChamados :chamados="chamados" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import FormularioChamado from './components/FormularioChamado.vue';
import ListaChamados from './components/ListaChamados.vue';

const chamados = ref([]);

const carregarChamados = async () => {
  try {
    const resposta = await axios.get('http://localhost:5000/api/chamados');
    
    chamados.value = resposta.data.reverse();
  } catch (erro) {
    console.error("Erro ao buscar chamados:", erro);
  }
};


onMounted(carregarChamados);
</script>