package com.rhd.krnl.ui.viewmodel

import androidx.compose.runtime.Immutable
import com.rhd.krnl.ui.UiMode
import com.rhd.krnl.ui.theme.AppSettings

@Immutable
data class MainActivityUiState(
    val appSettings: AppSettings,
    val pageScale: Float,
    val enableBlur: Boolean,
    val enableFloatingBottomBar: Boolean,
    val enableFloatingBottomBarBlur: Boolean,
    val enableNavigationBadge: Boolean,
    val uiMode: UiMode,
)
