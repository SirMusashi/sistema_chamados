<template>
  <div class="bg-white p-6 rounded-lg shadow-md border border-gray-200">
    <div class="flex flex-col md:flex-row justify-between items-center mb-6">
      <h2 class="text-xl font-bold text-gray-800 mb-4 md:mb-0">Painel de Chamados</h2>
      
      <select v-model="filtroStatus" class="border border-gray-300 p-2 rounded bg-white w-full md:w-auto">
        <option value="">Todos os status</option>
        <option value="aberto">Aberto</option>
        <option value="em andamento">Em Andamento</option>
        <option value="resolvido">Resolvido</option>
        <option value="fechado">Fechado</option>
      </select>
    </div>
    
    <div v-if="chamadosFiltrados.length === 0" class="text-center text-gray-500 py-8">
      Nenhum chamado encontrado.
    </div>
    
    <div class="grid gap-4">
      <div v-for="chamado in chamadosFiltrados" :key="chamado.id" class="border border-gray-200 rounded p-4 hover:bg-gray-50 transition">
        <div class="flex justify-between items-start mb-2">
          <h3 class="font-bold text-lg text-gray-800">#{{ chamado.id }} - {{ chamado.titulo }}</h3>
          <span :class="corStatus(chamado.status)" class="px-3 py-1 text-xs font-bold rounded-full text-white uppercase tracking-wide">
            {{ chamado.status }}
          </span>
        </div>
        
        <p class="text-gray-600 mb-4">{{ chamado.descricao }}</p>
        
        <div class="flex flex-col md:flex-row md:justify-between text-sm text-gray-500 bg-gray-100 p-2 rounded">
          <span class="mb-1 md:mb-0"><strong class="text-gray-700">Responsável:</strong> {{ chamado.responsavel_nome }}</span>
          <span class="mb-1 md:mb-0"><strong class="text-gray-700">Prioridade:</strong> <span class="capitalize">{{ chamado.prioridade }}</span></span>
          <span><strong class="text-gray-700">Abertura:</strong> {{ formatarData(chamado.data_abertura) }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  chamados: Array
});

const filtroStatus = ref('');

const chamadosFiltrados = computed(() => {
  if (!filtroStatus.value) return props.chamados;
  return props.chamados.filter(c => c.status === filtroStatus.value);
});

const corStatus = (status) => {
  const cores = {
    'aberto': 'bg-yellow-500',
    'em andamento': 'bg-blue-500',
    'resolvido': 'bg-green-500',
    'fechado': 'bg-gray-600'
  };
  return cores[status] || 'bg-gray-400';
};

const formatarData = (dataString) => {
  if (!dataString) return '';
  const data = new Date(dataString);
  return data.toLocaleDateString('pt-BR', { hour: '2-digit', minute: '2-digit' });
};
</script>