package com.rhd.krnl.data.repository

import com.rhd.krnl.data.model.Module
import com.rhd.krnl.data.model.ModuleUpdateInfo

interface ModuleRepository {
    suspend fun getModules(): Result<List<Module>>
    suspend fun checkUpdate(module: Module): Result<ModuleUpdateInfo>
}
