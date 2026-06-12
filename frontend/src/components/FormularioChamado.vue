<template>
  <div class="bg-white p-6 rounded-lg shadow-md mb-8 border border-gray-200">
    <h2 class="text-xl font-bold mb-4 text-gray-800">Novo Chamado</h2>
    
    <form @submit.prevent="salvarChamado">
      <div class="mb-4">
        <label class="block text-gray-700 font-semibold mb-1">Título</label>
        <input v-model="chamado.titulo" type="text" class="w-full border border-gray-300 p-2 rounded focus:outline-none focus:border-blue-500" placeholder="Ex: Teclado parou de funcionar" required />
      </div>
      
      <div class="mb-4">
        <label class="block text-gray-700 font-semibold mb-1">Descrição</label>
        <textarea v-model="chamado.descricao" class="w-full border border-gray-300 p-2 rounded focus:outline-none focus:border-blue-500" rows="3" placeholder="Detalhes do problema..." required></textarea>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <div>
          <label class="block text-gray-700 font-semibold mb-1">Prioridade</label>
          <select v-model="chamado.prioridade" class="w-full border border-gray-300 p-2 rounded bg-white">
            <option value="baixa">Baixa</option>
            <option value="media">Média</option>
            <option value="alta">Alta</option>
          </select>
        </div>
        
        <div>
          <label class="block text-gray-700 font-semibold mb-1">Atribuição de Responsável</label>
          <select v-model="chamado.tipo_atribuicao" class="w-full border border-gray-300 p-2 rounded bg-white" @change="limparResponsavel">
            <option value="automatica">Automática (Equilibrar carga)</option>
            <option value="manual">Escolher Manualmente</option>
          </select>
        </div>
      </div>
      
      <div v-if="chamado.tipo_atribuicao === 'manual'" class="mb-6 p-4 bg-gray-50 border rounded">
        <label class="block text-gray-700 font-semibold mb-1">Selecione o Responsável</label>
        <select v-model="chamado.responsavel_id" class="w-full border border-gray-300 p-2 rounded bg-white" required>
          <option disabled value="">Escolha um técnico...</option>
          <option v-for="resp in responsaveis" :key="resp.id" :value="resp.id">
            {{ resp.nome }}
          </option>
        </select>
      </div>
      
      <button type="submit" class="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition font-bold w-full md:w-auto">
        Abrir Chamado
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';


const emit = defineEmits(['chamadoCriado']);

const responsaveis = ref([]);
const chamado = ref({
  titulo: '',
  descricao: '',
  prioridade: 'media',
  tipo_atribuicao: 'automatica',
  responsavel_id: ''
});

const carregarResponsaveis = async () => {
  try {
    const resposta = await axios.get('http://localhost:5000/api/responsaveis');
    responsaveis.value = resposta.data;
  } catch (erro) {
    console.error("Erro ao carregar responsáveis:", erro);
  }
};

const limparResponsavel = () => {
  chamado.value.responsavel_id = '';
};

const salvarChamado = async () => {
  try {
    await axios.post('http://localhost:5000/api/chamados', chamado.value);
    
    
    chamado.value = { titulo: '', descricao: '', prioridade: 'media', tipo_atribuicao: 'automatica', responsavel_id: '' };
    
    
    emit('chamadoCriado');
    alert("Chamado criado com sucesso!");
  } catch (erro) {
    console.error("Erro ao criar chamado:", erro);
    alert("Erro ao criar chamado.");
  }
};

onMounted(carregarResponsaveis);
</script>