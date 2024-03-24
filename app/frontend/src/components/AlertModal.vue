<template>

	<button type="button" @click="searchRoutes()" class="btn btn-primary">
		<span>Buscar</span>
	</button>

	<div class="modal fade" id="ExemploModalCentralizado" data-bs-backdrop="false" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
		<div class="modal-dialog modal-dialog-centered ">
			<div class="modal-content">
				<div class="modal-header">
					<div class="alert">
						<span class="material-icons">
							priority_high
						</span>
					</div>
				</div>
				<div class="modal-body">
					<p>Insira os valores para realizar a cotação.</p>
				</div>
				<div class="modal-footer">
					<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#ExemploModalCentralizado">Fechar</button>
				</div>
			</div>
		</div>
	</div>

</template>

<script>
import { defineComponent } from 'vue';
export default defineComponent({
	name: 'AlertModal',
	emits: ['searchRoutes'],
	data() {

		return {
			openClose: false,
		};
	},
	props: {
		showModal: {
			type: Boolean,
			default: false,
		},
		computed: {
			basebutton() {

			},
		}

	},
	methods: {
		searchRoutes() {

			if (this.showModal) {
				let myModal = new bootstrap.Modal(document.getElementById('ExemploModalCentralizado'), {
					keyboard: false,
					backdrop: false,
					focus: true
				});
				myModal.show();

			} else {
				this.$emit('searchRoutes');

			}
		},
	}
});

</script>



<style scoped lang="scss">
.modal.fade .modal-dialog {
	transform: scale(0.1);
	transition: transform 0.1s ease;
}

.modal.show .modal-dialog {
	transform: scale(1);
}

.modal .modal-header {
	display: flex;
	justify-content: center;
	border-bottom: none;
}

.modal-header .alert {
	margin-top: 7%;
	border: 5px solid blue;
	display: flex;
	justify-content: center;
}

.modal .modal-body {
	font-size: 140%;
	columns: darkgray;
	display: flex;
	justify-content: center;
	align-content: center;
	border-top: none;
	padding-left: 20%;
	padding-right: 20%;
}

.modal .modal-footer {
	display: flex;
	justify-content: center;
	border-top: none;
	margin-bottom: 7%;
}

.modal-footer .btn {
	width: 40%;
}
</style>