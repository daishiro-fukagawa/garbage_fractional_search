<template>
    <div class="overflow-hidden">
        <div class="max-w-[85rem] mx-auto px-4 sm:px-6 lg:px-8 py-20">
            <h1 class="text-4xl text-green-700 text-center font-semibold">東京都新宿区ゴミ分別検索</h1>
            <div class="relative mx-auto max-w-4xl grid space-y-5 sm:space-y-10">
                <div class="text-center">
                    <p class="text-xs font-semibold text-gray-500 tracking-wide uppercase mb-3 dark:text-gray-200">
                        ＜引用元についてのテキストを書くところ＞
                    </p>
                    
                    <div class="mx-auto max-w-2xl sm:flex sm:space-x-3 p-3 bg-white border rounded-lg shadow-lg shadow-gray-100 dark:bg-slate-900 dark:border-gray-700 dark:shadow-gray-900/[.2]">
          <div class="pb-2 sm:pb-0 sm:flex-[1_0_0%]">
            <label for="hs-hero-name-1" class="block text-sm font-medium dark:text-white"><span class="sr-only">Your name</span></label>
                    <input type="text" v-model="searchQuery" @input="search" placeholder="ゴミの種類を入力" class="py-3 px-4 block w-full border-transparent rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 sm:p-4 dark:bg-slate-900 dark:border-transparent dark:text-gray-400" />
          </div>
        </div>


                    <div v-if="result">
                        <p>名前: {{ result.name }}</p>
                        <p>分別種類: {{ result.type }}</p>
                        <p>捨てる方法: {{ result.method }}</p>
                    </div>
                </div>
            </div>
        </div>
   </div>
</template>

<script>
import { ref } from 'vue';
import Papa from 'papaparse';

export default {
  setup() {
    const searchQuery = ref('');
    const result = ref(null);

    const loadData = async () => {
      const response = await fetch('/data/garbage_data.csv');
      const csvData = await response.text();
      console.log(csvData);
      return new Promise((resolve) => {
        Papa.parse(csvData, {
          header: true,
          complete: (results) => {
            resolve(results.data);
          },
        });
      });
    };

    const search = async () => {
      const data = await loadData();
      const searchTerm = searchQuery.value.trim().toLowerCase();
      if (searchTerm === '') {
        result.value = null;
        return;
      }

      for (const item of data) {
        console.log(searchTerm);
        if (item.name.toLowerCase().includes(searchTerm)) {
          result.value = item;
          break;
        }
      }
    };

    return { searchQuery, search, result };
  },
};
</script>