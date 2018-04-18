tinymce.init({
	selector: 'textarea',
	height: 300,
	menubar: false,
	invalid_elements: 'table,h1,h2,h3,h4,h5,h6,img,object',
	plugins: [
		'advlist autolink lists link charmap print preview anchor textcolor',
		'searchreplace visualblocks code fullscreen',
		'insertdatetime table contextmenu paste code help wordcount'
	],
	toolbar: 'insert | undo redo |  bold italic  | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat | help'
});