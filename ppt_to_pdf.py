from aspose.slides import slides

dokuman = slide.Prestentation("Vize.pptx")

dokuman.save("Vize.pdf", slides.export.SaveFormat.PDF)