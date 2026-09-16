package com.rhd.krnl.ui.component.uninstalldialog

import androidx.compose.runtime.Composable
import com.rhd.krnl.ui.LocalUiMode
import com.rhd.krnl.ui.UiMode

@Composable
fun UninstallDialog(
    show: Boolean,
    onDismissRequest: () -> Unit
) {
    when (LocalUiMode.current) {
        UiMode.Miuix -> UninstallDialogMiuix(show, onDismissRequest)
        UiMode.Material -> UninstallDialogMaterial(show, onDismissRequest)
    }
}
