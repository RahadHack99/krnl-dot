package com.rhd.krnl.data.repository

import com.rhd.krnl.data.model.RepoModule

interface ModuleRepoRepository {
    suspend fun fetchModules(): Result<List<RepoModule>>
}
