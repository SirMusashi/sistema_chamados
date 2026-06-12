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
        <div class="flex flex-col md:flex-row justify-between items-start mb-2 gap-2">
          <h3 class="font-bold text-lg text-gray-800">#{{ chamado.id }} - {{ chamado.titulo }}</h3>
          
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-500 font-semibold">Status:</span>
            <select 
              v-model="chamado.status" 
              @change="atualizarStatus(chamado)"
              :class="corStatus(chamado.status)" 
              class="px-2 py-1 text-xs font-bold rounded text-white uppercase tracking-wide border-none cursor-pointer outline-none"
            >
              <option value="aberto" class="bg-white text-gray-800">ABERTO</option>
              <option value="em andamento" class="bg-white text-gray-800">EM ANDAMENTO</option>
              <option value="resolvido" class="bg-white text-gray-800">RESOLVIDO</option>
              <option value="fechado" class="bg-white text-gray-800">FECHADO</option>
            </select>
          </div>
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
import axios from 'axios';

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
    'aberto': 'bg-yellow-500 hover:bg-yellow-600',
    'em andamento': 'bg-blue-500 hover:bg-blue-600',
    'resolvido': 'bg-green-500 hover:bg-green-600',
    'fechado': 'bg-gray-600 hover:bg-gray-700'
  };
  return cores[status] || 'bg-gray-400';
};

const formatarData = (dataString) => {
  if (!dataString) return '';
  const data = new Date(dataString);
  return data.toLocaleDateString('pt-BR', { hour: '2-digit', minute: '2-digit' });
};

// Função que avisa o Backend quando mudamos o status na tela
const atualizarStatus = async (chamado) => {
  try {
    await axios.put(`http://localhost:5000/api/chamados/${chamado.id}`, {
      status: chamado.status
    });
    // Opcional: mostrar um alerta visual mais discreto
    console.log(`Chamado ${chamado.id} atualizado para ${chamado.status}`);
  } catch (erro) {
    console.error("Erro ao atualizar chamado:", erro);
    alert("Erro ao salvar o novo status.");
  }
};
</script>